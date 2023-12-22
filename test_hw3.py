"""testing module."""
from hw3 import AudioFile, VideoFile, MediaLibrary

import pytest

VIDEO_RESOLUTION = 180
TIME = 300
DURATION = 120


@pytest.fixture
def sample_audio_file():
    """_summary_.

    Returns:
        _type_: _description_
    """
    return AudioFile('audio_name', 'mp3', 'author_name', DURATION)


@pytest.fixture
def sample_video_file():
    """_summary_.

    Returns:
        _type_: _description_
    """
    return VideoFile('video_name', 'mp4', VIDEO_RESOLUTION, TIME)


@pytest.fixture
def sample_media_library():
    """_summary_.

    Returns:
        _type_: _description_
    """
    return MediaLibrary()


def test_audio_file_init(sample_audio_file):
    """_summary_.

    Args:
        sample_audio_file (_type_): _description_
    """
    assert sample_audio_file.name == 'audio_name'
    assert sample_audio_file.expansion == 'mp3'
    assert sample_audio_file.executor == 'author_name'
    assert sample_audio_file.time == DURATION


def test_video_file_init(sample_video_file):
    """_summary_.

    Args:
        sample_video_file (_type_): _description_
    """
    assert sample_video_file.name == 'video_name'
    assert sample_video_file.expansion == 'mp4'
    assert sample_video_file.resolution == VIDEO_RESOLUTION
    assert sample_video_file.duration == TIME


def test_media_library_add_remove(sample_media_library, sample_audio_file, sample_video_file):
    """_summary_.

    Args:
        sample_media_library (_type_): _description_
        sample_audio_file (_type_): _description_
        sample_video_file (_type_): _description_
    """
    assert len(sample_media_library.list_of_media) == 0

    sample_media_library.add_media_file(sample_audio_file)
    sample_media_library.add_media_file(sample_video_file)

    assert len(sample_media_library.list_of_media) == 2

    sample_media_library.remove_media_file(sample_audio_file)
    assert len(sample_media_library.list_of_media) == 1
    assert sample_audio_file not in sample_media_library.list_of_media
