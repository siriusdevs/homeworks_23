"""Файл тестирования классов."""
import unittest

from hw3 import AudioFile, MediaLibrary, VideoFile

DURATION1 = 3.5
DURATION2 = 5.2


class TestMediaLibrary(unittest.TestCase):
    """Тесты для классов AudioFile, VideoFile, MediaLibrary."""

    def setUp(self):
        """Инициализация классов перед выполнением тестов."""
        self.audio_file = AudioFile('audio_song', 'mp3', 'John Doe', DURATION1)
        self.video_file = VideoFile('video_clip', 'mp4', '1080p', DURATION2)
        self.media_library = MediaLibrary()

    def test_add_media_file(self):
        """Тестирование добавления медиафайла в медиатеку."""
        initial_count = len(self.media_library.get_all_media_files())

        self.media_library.add_media_file(self.audio_file)
        updated_count = len(self.media_library.get_all_media_files())

        self.assertEqual(updated_count, initial_count + 1)
        self.assertIn(
            self.audio_file,
            self.media_library.get_all_media_files(),
        )

    def test_remove_media_file(self):
        """Тестирование удаления медиафайла из медиатеки."""
        self.media_library.add_media_file(self.audio_file)
        initial_count = len(self.media_library.get_all_media_files())

        self.media_library.remove_media_file(self.audio_file)
        updated_count = len(self.media_library.get_all_media_files())

        self.assertEqual(updated_count, initial_count - 1)
        self.assertNotIn(
            self.audio_file,
            self.media_library.get_all_media_files(),
        )

    def test_get_all_media_files(self):
        """Тестирование получения списка всех медиафайлов в медиатеке."""
        self.media_library.add_media_file(self.audio_file)
        self.media_library.add_media_file(self.video_file)

        all_media_files = self.media_library.get_all_media_files()

        self.assertIn(self.audio_file, all_media_files)
        self.assertIn(self.video_file, all_media_files)


if __name__ == '__main__':
    unittest.main()
