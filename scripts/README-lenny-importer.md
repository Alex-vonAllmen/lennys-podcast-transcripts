# Lenny’s Podcast → local transcripts → WeKnora

`lenny_to_weknora.py` adapts the Dwarkesh importer to Lenny’s archive. It discovers
archive episodes, downloads public transcript JSON (with published HTML and
English captions as fallbacks), writes YAML frontmatter plus timestamped text,
and uploads Markdown through the same WeKnora file API.

Requirements: Python 3.9+, `curl`, internet access; WeKnora ingestion credentials
for uploads. No Python packages or model router are required.

## Preview

Run from the repository root:

```sh
python3 scripts/lenny_to_weknora.py --list
python3 scripts/lenny_to_weknora.py --dry-run --limit 1
```

`--list` only reads the archive and local files. `--dry-run`, matching the Dwarkesh
script’s convention, **writes downloaded files** but does not upload. For a
preview outside the collection:

```sh
python3 scripts/lenny_to_weknora.py --dry-run --limit 1 \
  --output-dir /tmp/lenny-preview/episodes
```

The default output is this repository’s `episodes/` directory. New episodes use
`episodes/<archive-slug>/transcript.md`; archive slugs avoid collisions for repeat
guests. Existing files are never overwritten.

## Import

Supply the same environment variables as the Dwarkesh importer, using the
credentials and knowledge-base ID for **Lenny’s Podcast**:

```sh
export WEKNORA_HOST='http://127.0.0.1:18081'
export WEKNORA_KNOWLEDGE_BASE_ID='YOUR_LENNY_KNOWLEDGE_BASE_ID'
# Set WEKNORA_API_KEY in the shell using your existing secret-loading method.
python3 scripts/lenny_to_weknora.py --limit 1
python3 scripts/lenny_to_weknora.py
```

The final command processes all gaps and any newly published episodes. To select
a single missing episode instead:

```sh
python3 scripts/lenny_to_weknora.py --slug episode-2-julie-zhuo
```

The uploader uses `X-API-Key` and
`POST /api/v1/knowledge-bases/<id>/knowledge/file`, like the reference script.
A returned knowledge ID means WeKnora accepted the file; indexing is asynchronous.
The script does not create a knowledge base or retrieve credentials.

## Existing collection and repeat runs

`lenny-existing-episodes.json` contains the 290 archive-to-file matches verified
against transcript text on October 16, 2026. This mapping is necessary because
several old files have wrong dates, titles, or video IDs. Existing mapped files
are skipped, leaving the 73 missing episodes identified by that audit. The two
promotional entries are excluded. If a mapped file is removed, its episode
becomes eligible for download. This mapping is for the original collection;
when writing to an empty alternative output directory, all archive episodes are
eligible unless constrained by `--limit` or `--slug`.

Newly downloaded files are reused for later uploads. Successful uploads are
recorded in `episodes/.weknora-import-state.json`, keyed by server, knowledge base,
episode slug, and file hash. An unchanged upload is skipped. A failed upload
leaves the local transcript available for retry. Ambiguous upload failures are
not retried automatically; a server duplicate response is accepted on rerun.
Previously mapped collection files are neither rewritten nor uploaded by this
script. `--list` lists only gaps that still need a local download.

Frontmatter includes guest, title, publication date, source URL, archive ID and
slug, topic, source description/summary, YouTube ID/URL when available, duration,
channel, and transcript source. Descriptions remain empty when the source has no
subtitle. No view counts, keywords, or missing metadata are invented. Speaker
labels are preserved from Substack’s published speaker mapping.

The downloader only uses publicly accessible source URLs. Inaccessible episodes
are reported as failures, processing continues, and the command exits nonzero.
Timed JSON/caption transcripts covering less than 90% of the published duration
are rejected to avoid treating a short preview as a complete transcript.

## Verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts \
  -p 'test_lenny_to_weknora.py' -v
```

Tests cover pagination/filtering, extraction/fallbacks, partial previews,
frontmatter, existing-file matching, upload failures, and resumable imports.
Live download-only checks were performed for Josh Woodward (October 11, 2026)
and Julie Zhuo (June 7, 2022) in a temporary directory. No live WeKnora upload
was performed during script development.
