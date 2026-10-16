#!/usr/bin/env python3
"""Download missing Lenny's Podcast transcripts and import them into WeKnora.

Python 3.9+, curl. See scripts/README-lenny-importer.md for usage.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.lennysnewsletter.com"
ARCHIVE_URL = SITE + "/api/v1/archive"
PUBLIC_HOSTS = {"www.lennysnewsletter.com", "substackcdn.com"}


class ImportError(RuntimeError):
    """An expected import failure with a useful user-facing message."""

class TranscriptHTMLParser(HTMLParser):
    """Extract the semantic blocks after an article's Transcript heading."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.active = False
        self.blocks: list[str] = []
        self.block_tag: str | None = None
        self.buffer: list[str] = []
        self.strong_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h2", "h3", "p", "li", "blockquote"} and self.block_tag is None:
            self.block_tag = tag
            self.buffer = []
        elif self.block_tag and tag in {"strong", "b"}:
            self.buffer.append("**")
            self.strong_depth += 1
        elif self.block_tag and tag == "br":
            self.buffer.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.block_tag and tag in {"strong", "b"} and self.strong_depth:
            self.buffer.append("**")
            self.strong_depth -= 1
            return
        if tag != self.block_tag:
            return

        text = re.sub(r"[ \t\r\f\v]+", " ", "".join(self.buffer)).strip()
        block_tag = self.block_tag
        self.block_tag = None
        self.buffer = []
        self.strong_depth = 0

        heading_text = text.replace("**", "").strip()
        if block_tag == "h2" and re.fullmatch(r"Transcript:?", heading_text, re.IGNORECASE):
            self.active = True
            return
        if not self.active or not text:
            return
        prefix = {"h2": "## ", "h3": "### ", "li": "- ", "blockquote": "> "}.get(block_tag, "")
        self.blocks.append(prefix + text)

    def handle_data(self, data: str) -> None:
        if self.block_tag:
            self.buffer.append(data)

def transcript_from_html(body_html: str | None) -> str | None:
    if not body_html:
        return None
    parser = TranscriptHTMLParser()
    parser.feed(body_html)
    text = "\n\n".join(parser.blocks).strip()
    return text or None

def transcript_from_vtt(raw_vtt: str) -> str | None:
    paragraphs: list[str] = []
    cue_lines: list[str] = []

    def flush() -> None:
        if not cue_lines:
            return
        cue = html.unescape(" ".join(cue_lines))
        cue = re.sub(r"<[^>]+>", "", cue)
        cue = re.sub(r"\s+", " ", cue).strip()
        cue_lines.clear()
        if cue and (not paragraphs or paragraphs[-1] != cue):
            paragraphs.append(cue)

    for line in raw_vtt.replace("\ufeff", "").splitlines():
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped == "WEBVTT" or "-->" in stripped or stripped.isdigit():
            continue
        elif stripped.startswith(("NOTE", "STYLE", "REGION")):
            flush()
        else:
            cue_lines.append(stripped)
    flush()
    return "\n\n".join(paragraphs) or None

def api_base(host: str) -> str:
    host = host.rstrip("/")
    return host if host.endswith("/api/v1") else f"{host}/api/v1"

def encode_multipart(file_path: Path, metadata: dict[str, Any]) -> tuple[bytes, str]:
    boundary = f"----lenny-{uuid.uuid4().hex}"
    chunks: list[bytes] = []

    def field(name: str, value: str) -> None:
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode("utf-8"),
                b"\r\n",
            ]
        )

    field("metadata", json.dumps(metadata, ensure_ascii=False))
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'.encode(),
            b"Content-Type: text/markdown; charset=utf-8\r\n\r\n",
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    return b"".join(chunks), boundary

def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"uploaded": {}}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ImportError(f"Could not read state file {path}: {exc}") from exc
    if not isinstance(state, dict) or not isinstance(state.get("uploaded", {}), dict):
        raise ImportError(f"Invalid import state: {path}")
    state.setdefault("uploaded", {})
    return state

def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def request_bytes(url: str, *, data: bytes | None = None,
                  headers: dict[str, str] | None = None, method: str | None = None) -> bytes:
    # Substack rejects Python's HTTP client on some public CDN/archive routes.
    if data is None and urlsplit(url).hostname in PUBLIC_HOSTS:
        result = subprocess.run(
            ["curl", "--fail", "--silent", "--show-error", "--location",
             "--max-time", "60", "--retry", "2", url], capture_output=True,
        )
        if result.returncode:
            raise ImportError(f"Could not fetch public source {url.split('?')[0]} (curl exit {result.returncode})")
        return result.stdout
    try:
        request = Request(url, data=data, headers=headers or {}, method=method)
        with urlopen(request, timeout=120) as response:
            return response.read()
    except HTTPError as exc:
        # Do not retry uploads: the server may have accepted the first request.
        if exc.code == 409:
            raise ImportError("HTTP 409: duplicate document") from exc
        raise ImportError(f"HTTP {exc.code} from {url.split('?')[0]}") from exc
    except (URLError, TimeoutError) as exc:
        raise ImportError(f"Could not reach {url.split('?')[0]}") from exc


def request_json(url: str, **kwargs: Any) -> Any:
    try:
        return json.loads(request_bytes(url, **kwargs))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ImportError(f"Expected JSON from {url.split('?')[0]}") from exc


def fetch_episodes() -> list[dict[str, Any]]:
    episodes = []
    seen = set()
    offset = 0
    while True:
        query = urlencode(dict(sort="new", offset=offset, limit=50,
                               type="podcast", rss_episodes_only="true"))
        posts = request_json(f"{ARCHIVE_URL}?{query}")
        if not isinstance(posts, list):
            raise ImportError("Unexpected podcast archive response")
        if not posts:
            return episodes
        fresh = [p for p in posts if p.get("slug") not in seen]
        if not fresh:
            raise ImportError("Archive pagination repeated a page")
        for post in fresh:
            if not post.get("slug"):
                raise ImportError("Archive entry has no slug")
            seen.add(post["slug"])
            episodes.append(post)
        offset += len(posts)


def timestamp(seconds: float) -> str:
    total = max(0, int(seconds))
    return f"{total // 3600:02}:{total % 3600 // 60:02}:{total % 60:02}"


def transcription_info(post: dict[str, Any]) -> list[dict[str, Any]]:
    uploads = [post.get("podcastUpload"), post.get("videoUpload"),
               (post.get("videoUpload") or {}).get("extractedAudio")]
    return [u["transcription"] for u in uploads if u and u.get("transcription")]


def transcript_from_json(segments: Any, speakers: dict[str, str]) -> str:
    if not isinstance(segments, list):
        raise ImportError("Unexpected transcript JSON: expected a list of segments")
    turns = []
    for segment in segments:
        text = str(segment.get("text") or "").strip()
        if not text:
            continue
        speaker = speakers.get(segment.get("speaker"), segment.get("speaker") or "Speaker")
        if turns and turns[-1][0] == speaker:
            turns[-1][2].append(text)
        else:
            turns.append((speaker, float(segment.get("start") or 0), [text]))
    return "\n\n".join(f"{speaker} ({timestamp(start)}):\n{' '.join(texts)}"
                        for speaker, start, texts in turns)


def validate_coverage(post: dict[str, Any], end: float) -> None:
    upload = post.get("podcastUpload") or {}
    expected = (upload.get("full_podcast_info") or {}).get("duration") or post.get("podcast_duration") or 0
    if expected and end < float(expected) * 0.9:
        raise ImportError("Transcript covers less than 90% of the episode; refusing a partial preview")


def read_document_metadata(path: Path, post: dict[str, Any]) -> dict[str, Any]:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ImportError(f"Existing file has no generated frontmatter: {path}")
    try:
        metadata = {key: json.loads(value) for line in parts[1].strip().splitlines()
                    for key, value in [line.split(":", 1)]}
    except (ValueError, TypeError) as exc:
        raise ImportError(f"Existing file has invalid generated frontmatter: {path}") from exc
    if metadata.get("archive_id") != post["id"] or metadata.get("slug") != post["slug"]:
        raise ImportError(f"Existing file does not identify this archive episode: {path}")
    return metadata


def fetch_transcript(post: dict[str, Any]) -> tuple[str, str]:
    failures = []
    for info in transcription_info(post):
        if info.get("cdn_url"):
            try:
                segments = request_json(info["cdn_url"])
                text = transcript_from_json(segments, info.get("speaker_map") or {})
                if text:
                    validate_coverage(post, max(float(s.get("end") or 0) for s in segments))
                    return text, "substack-transcription"
            except ImportError as exc:
                failures.append(str(exc))
    text = transcript_from_html(post.get("body_html"))
    if text:
        return text, "published"
    for info in transcription_info(post):
        # English only: do not silently substitute a translated transcript.
        for caption in info.get("signed_captions") or []:
            if caption.get("language") == "en" and caption.get("url"):
                try:
                    vtt = request_bytes(caption["url"]).decode("utf-8-sig")
                    text = transcript_from_vtt(vtt)
                    if text:
                        ends = re.findall(r"-->\s*(\d+:\d{2}:\d{2}[.,]\d+)", vtt)
                        if not ends:
                            raise ImportError("Captions contain no valid timestamps")
                        hours, minutes, seconds = ends[-1].replace(",", ".").split(":")
                        validate_coverage(post, int(hours) * 3600 + int(minutes) * 60 + float(seconds))
                        return text, "captions"
                except ImportError as exc:
                    failures.append(str(exc))
    detail = f" ({'; '.join(failures)})" if failures else ""
    raise ImportError("No accessible transcript or English captions" + detail)


def episode_metadata(post: dict[str, Any], transcript: str = "") -> dict[str, Any]:
    title = post.get("title") or post["slug"]
    topic, separator, guest = title.rpartition(" | ")
    if separator:
        guest = re.sub(r"\s*\(.*", "", guest).strip()
    else:
        topic, guest = title, ""
    if not guest:
        names = []
        for info in transcription_info(post):
            for name in (info.get("speaker_map") or {}).values():
                if name and "lenny" not in name.lower() and not name.startswith("SPEAKER_") and name not in names:
                    names.append(name)
        guest = " & ".join(names)
    if not guest:
        names = re.findall(r"^([^\n:]+)\s+\(\d+:\d+(?::\d+)?\):", transcript, re.M)
        guest = " & ".join(dict.fromkeys(n.strip() for n in names
                                        if "lenny" not in n.lower() and not n.startswith(("Speaker", "SPEAKER_"))))
    youtube = re.search(r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]{11})', post.get("body_html") or "")
    video_id = youtube[1] if youtube else ""
    seconds = float(post.get("podcast_duration") or 0)
    return dict(guest=guest, title=title, publish_date=(post.get("post_date") or "")[:10],
                source=post.get("canonical_url") or f"{SITE}/p/{post['slug']}",
                slug=post["slug"], archive_id=post["id"], topic=topic,
                description=post.get("subtitle") or "", summary=post.get("subtitle") or "",
                youtube_url=f"https://www.youtube.com/watch?v={video_id}" if video_id else "",
                video_id=video_id, duration_seconds=seconds, duration=timestamp(seconds),
                channel="Lenny's Podcast")


def render_document(metadata: dict[str, Any], transcript: str, source: str) -> str:
    metadata = {**metadata, "transcript_source": source}
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in metadata.items()]
    lines += ["---", "", f"# {metadata['title']}", "", "## Transcript", "", transcript, ""]
    return "\n".join(lines)


def episode_path(output_dir: Path, post: dict[str, Any]) -> Path:
    slug = post["slug"]
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", slug):
        raise ImportError("Unsafe episode slug")
    # Use the archive slug to avoid collisions between repeat guests.
    return output_dir / slug / "transcript.md"


def upload_document(host: str, key: str, kb_id: str, path: Path,
                    metadata: dict[str, Any]) -> str:
    body, boundary = encode_multipart(path, {**metadata, "podcast": "Lenny's Podcast"})
    try:
        response = request_json(
            f"{api_base(host)}/knowledge-bases/{quote(kb_id, safe='')}/knowledge/file",
            headers={"X-API-Key": key, "Content-Type": f"multipart/form-data; boundary={boundary}"},
            data=body, method="POST",
        )
    except ImportError as exc:
        if str(exc).startswith("HTTP 409:"):
            return "duplicate"
        raise
    if not isinstance(response, dict) or response.get("success") is False:
        raise ImportError("WeKnora rejected the upload")
    knowledge = response.get("data", response)
    if not isinstance(knowledge, dict) or not knowledge.get("id"):
        raise ImportError("WeKnora response did not include a knowledge ID")
    return str(knowledge["id"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "episodes")
    parser.add_argument("--existing-map", type=Path, default=Path(__file__).with_name("lenny-existing-episodes.json"))
    parser.add_argument("--limit", type=int, help="Process the newest N missing episodes")
    parser.add_argument("--slug", help="Process one archive slug")
    parser.add_argument("--list", action="store_true", help="List missing episodes; do not write or upload")
    parser.add_argument("--dry-run", action="store_true", help="Download and write transcripts without uploading")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.limit is not None and args.limit < 1:
        raise ImportError("--limit must be at least 1")
    host = os.environ.get("WEKNORA_HOST", "").rstrip("/")
    key = os.environ.get("WEKNORA_API_KEY", "")
    kb = os.environ.get("WEKNORA_KNOWLEDGE_BASE_ID", "")
    if not args.dry_run and not args.list:
        missing = [name for name, value in [("WEKNORA_HOST", host), ("WEKNORA_API_KEY", key),
                                            ("WEKNORA_KNOWLEDGE_BASE_ID", kb)] if not value]
        if missing:
            raise ImportError("Missing environment variables: " + ", ".join(missing))
    try:
        existing = json.loads(args.existing_map.read_text())["episodes"]
    except (OSError, ValueError, KeyError) as exc:
        raise ImportError(f"Cannot read audited episode mapping: {args.existing_map}") from exc
    posts = fetch_episodes()
    selected = []
    for post in posts:
        if args.slug and post["slug"] != args.slug:
            continue
        old_path = existing.get(post["slug"])
        if old_path and (args.output_dir.parent / old_path).is_file():
            continue
        # Archive promotions are not interview transcripts.
        if post["slug"] in {"episode-1-welcome-to-my-new-podcast", "announcing-a-brand-new-podcast-how"}:
            continue
        selected.append(post)
    if args.slug and not any(p["slug"] == args.slug for p in posts):
        raise ImportError(f"Episode not found in archive: {args.slug}")
    if args.list:
        selected = [p for p in selected if not episode_path(args.output_dir, p).exists()]
    if args.limit:
        selected = selected[:args.limit]
    print(f"Found {len(posts)} archive entries; selected {len(selected)} missing episodes")
    if args.list:
        for post in selected:
            print(f"{post['post_date'][:10]}  {post['title']}  {post['canonical_url']}")
        return 0
    state_path = args.output_dir / ".weknora-import-state.json"
    state = load_state(state_path)
    scope = hashlib.sha256(f"{api_base(host)}\n{kb}".encode()).hexdigest()
    uploaded = downloaded = skipped = failed = 0
    for index, post in enumerate(selected, 1):
        try:
            path = episode_path(args.output_dir, post)
            # Fetch fresh post metadata so signed transcript URLs are current.
            full_post = request_json(f"{SITE}/api/v1/posts/{quote(post['slug'], safe='')}")
            if full_post.get("slug") != post["slug"] or full_post.get("id") != post["id"]:
                raise ImportError("Post identity differs from the archive entry")
            if not path.exists():
                transcript, source = fetch_transcript(full_post)
                metadata = episode_metadata(full_post, transcript)
                document = render_document(metadata, transcript, source)
                path.parent.mkdir(parents=True, exist_ok=True)
                # Never overwrite an existing transcript, including on failed imports.
                with path.open("x", encoding="utf-8") as file:
                    file.write(document)
                downloaded += 1
            else:
                metadata = read_document_metadata(path, post)
            print(f"[{index}/{len(selected)}] {post['slug']}: saved", flush=True)
            if args.dry_run:
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            state_key = f"{scope}:{post['slug']}"
            if state["uploaded"].get(state_key, {}).get("sha256") == digest:
                skipped += 1
                continue
            knowledge_id = upload_document(host, key, kb, path, metadata)
            state["uploaded"][state_key] = dict(file=str(path.relative_to(args.output_dir)),
                knowledge_id=knowledge_id, sha256=digest,
                uploaded_at=datetime.now().astimezone().isoformat(timespec="seconds"))
            save_state(state_path, state)
            uploaded += 1
            print(f"  WeKnora: {knowledge_id}", flush=True)
        except (ImportError, OSError, ValueError, IndexError, TypeError, KeyError) as exc:
            failed += 1
            print(f"  FAILED {post['slug']}: {exc}", file=sys.stderr, flush=True)
    print(f"Done: {downloaded} downloaded, {uploaded} uploaded, {skipped} unchanged, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ImportError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
