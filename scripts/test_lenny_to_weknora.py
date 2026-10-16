import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('lenny', Path(__file__).with_name('lenny_to_weknora.py'))
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def post(slug='example', episode_id=10):
    return dict(id=episode_id, slug=slug, title='Building products | Jane Doe (CEO)',
                canonical_url='https://www.lennysnewsletter.com/p/' + slug,
                post_date='2026-10-11T12:00:00Z', subtitle='Lessons in product development.',
                podcast_duration=100, body_html='')


class ImportTests(unittest.TestCase):
    def test_archive_uses_podcast_filters_and_reads_final_page(self):
        with patch.object(M, 'request_json', side_effect=[[post()], []]) as request:
            self.assertEqual(len(M.fetch_episodes()), 1)
        self.assertIn('rss_episodes_only=true', request.call_args_list[0].args[0])
        self.assertIn('type=podcast', request.call_args_list[0].args[0])
        self.assertIn('offset=1', request.call_args_list[1].args[0])

    def test_repeated_archive_page_fails(self):
        with patch.object(M, 'request_json', return_value=[post()]):
            with self.assertRaisesRegex(M.ImportError, 'repeated'):
                M.fetch_episodes()

    def test_json_preserves_speakers_and_groups_consecutive_segments(self):
        segments = [dict(speaker='S0', start=0, text='Hello.'),
                    dict(speaker='S0', start=1, text='More.'),
                    dict(speaker='S1', start=65, text='Thanks.')]
        text = M.transcript_from_json(segments, {'S0': 'Lenny', 'S1': 'Jane Doe'})
        self.assertEqual(text, 'Lenny (00:00:00):\nHello. More.\n\nJane Doe (00:01:05):\nThanks.')

    def test_inaccessible_json_falls_back_to_published_transcript(self):
        p = post()
        p['podcastUpload'] = {'transcription': {'cdn_url': 'https://substackcdn.com/t'}}
        p['body_html'] = '<p>Intro</p><h2>Transcript</h2><p>The interview.</p>'
        with patch.object(M, 'request_json', side_effect=M.ImportError('unavailable')):
            self.assertEqual(M.fetch_transcript(p), ('The interview.', 'published'))

    def test_partial_preview_is_rejected(self):
        p = post()
        p['podcastUpload'] = {'transcription': {'cdn_url': 'https://substackcdn.com/t'}}
        with patch.object(M, 'request_json', return_value=[dict(start=0, end=10, text='Preview')]):
            with self.assertRaisesRegex(M.ImportError, 'partial preview'):
                M.fetch_transcript(p)

    def test_vtt_fallback(self):
        p = post()
        p['podcastUpload'] = {'transcription': {'signed_captions': [{'language': 'en', 'url': 'caption'}]}}
        with patch.object(M, 'request_bytes', return_value=b'WEBVTT\n\n00:00:00.000 --> 00:01:40.000\nHello\n'):
            self.assertEqual(M.fetch_transcript(p), ('Hello', 'captions'))

    def test_metadata_and_saved_frontmatter_roundtrip(self):
        p = post()
        metadata = M.episode_metadata(p)
        self.assertEqual(metadata['guest'], 'Jane Doe')
        self.assertEqual(metadata['topic'], 'Building products')
        self.assertEqual(metadata['publish_date'], '2026-10-11')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'transcript.md'
            path.write_text(M.render_document(metadata, 'The transcript', 'published'))
            self.assertEqual(M.read_document_metadata(path, p)['guest'], 'Jane Doe')
            with self.assertRaises(M.ImportError):
                M.read_document_metadata(path, post(episode_id=11))

    def test_safe_paths_and_repeated_guests(self):
        self.assertNotEqual(M.episode_path(Path('/tmp'), post('one')),
                            M.episode_path(Path('/tmp'), post('two')))
        with self.assertRaises(M.ImportError):
            M.episode_path(Path('/tmp'), post('../escape'))

    def test_upload_metadata_and_failure_response(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'transcript.md'
            path.write_text('Transcript')
            with patch.object(M, 'request_json', return_value={'data': {'id': 'k1'}}) as request:
                self.assertEqual(M.upload_document('http://localhost', 'key', 'kb', path,
                                                  M.episode_metadata(post())), 'k1')
                self.assertIn(b"Lenny's Podcast", request.call_args.kwargs['data'])
                self.assertEqual(request.call_args.kwargs['headers']['X-API-Key'], 'key')
            for response in [{'success': False}, {'data': {}}]:
                with patch.object(M, 'request_json', return_value=response):
                    with self.assertRaises(M.ImportError):
                        M.upload_document('http://localhost', 'key', 'kb', path, {})

    def test_list_skips_audited_files_and_promotions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'episodes' / 'old').mkdir(parents=True)
            (root / 'episodes' / 'old' / 'transcript.md').write_text('Existing actual transcript')
            manifest = root / 'map.json'
            manifest.write_text(json.dumps({'episodes': {'old': 'episodes/old/transcript.md'}}))
            posts = [post('old'), post('new'), post('episode-1-welcome-to-my-new-podcast')]
            with patch.object(M, 'fetch_episodes', return_value=posts), patch('builtins.print') as output:
                self.assertEqual(M.main(['--list', '--existing-map', str(manifest),
                                         '--output-dir', str(root / 'episodes')]), 0)
            self.assertIn('selected 1 missing episodes', output.call_args_list[0].args[0])
            self.assertFalse((root / 'episodes' / '.weknora-import-state.json').exists())

    def test_rerun_skips_unchanged_upload_but_new_kb_imports(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / 'map.json'
            manifest.write_text('{"episodes":{}}')
            args = ['--existing-map', str(manifest), '--output-dir', str(root / 'episodes')]
            env = {'WEKNORA_HOST': 'http://localhost', 'WEKNORA_API_KEY': 'secret',
                   'WEKNORA_KNOWLEDGE_BASE_ID': 'kb1'}
            with patch.dict(os.environ, env), patch.object(M, 'fetch_episodes', return_value=[post()]), \
                 patch.object(M, 'request_json', return_value=post()), \
                 patch.object(M, 'fetch_transcript', return_value=('Interview text', 'published')) as download, \
                 patch.object(M, 'upload_document', return_value='k1') as upload, patch('builtins.print'):
                self.assertEqual(M.main(args), 0)
                self.assertEqual(M.main(args), 0)
                self.assertEqual(download.call_count, 1)
                self.assertEqual(upload.call_count, 1)
                with patch.dict(os.environ, {'WEKNORA_KNOWLEDGE_BASE_ID': 'kb2'}):
                    self.assertEqual(M.main(args), 0)
                self.assertEqual(upload.call_count, 2)

    def test_failed_upload_keeps_download_and_does_not_mark_imported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / 'map.json'
            manifest.write_text('{"episodes":{}}')
            args = ['--existing-map', str(manifest), '--output-dir', str(root / 'episodes')]
            env = {'WEKNORA_HOST': 'http://localhost', 'WEKNORA_API_KEY': 'secret',
                   'WEKNORA_KNOWLEDGE_BASE_ID': 'kb'}
            with patch.dict(os.environ, env), patch.object(M, 'fetch_episodes', return_value=[post()]), \
                 patch.object(M, 'request_json', return_value=post()), \
                 patch.object(M, 'fetch_transcript', return_value=('Interview text', 'published')), \
                 patch.object(M, 'upload_document', side_effect=M.ImportError('upload failed')), \
                 patch('builtins.print'):
                self.assertEqual(M.main(args), 1)
            self.assertTrue((root / 'episodes' / 'example' / 'transcript.md').exists())
            self.assertFalse((root / 'episodes' / '.weknora-import-state.json').exists())


if __name__ == '__main__':
    unittest.main()
