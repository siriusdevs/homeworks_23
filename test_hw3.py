"""testing module."""
import pytest

from hw3 import AudioFile, MediaLibrary, VideoFile, check_media_file

DURATION = 13.2


@pytest.mark.parametrize('name, expansion', [('file1', 'mp5'), ('file2', 'mp4')])
def test_check_valid_types(name: str, expansion: str):
    """Protest types.

    Args:
        name (str): file name
        expansion (str): file expansion
    """
    assert check_media_file(name, expansion) is None


@pytest.mark.parametrize('name, expansion', [(1, 'mp1'), ('file2', 123)])
def test_check_invalid_types(name: str, expansion: str):
    """Protect incorrect types.

    Args:
        name (str): file name
        expansion (str): file expansion
    """
    with pytest.raises(ValueError):
        check_media_file(name, expansion)


@pytest.mark.parametrize(
    'name, expansion, author, time',
    [('audio1', 'mp2', 'author1', 5), ('audio2', 'wav', 'author2', 10)],
        )
def test_audio_file_creation(name: str, expansion: str, author: str, time: int | float):
    """Test the audio file.

    Args:
        name (str): file name
        expansion (str): file expansion
        author (str): file author
        time (int | float): file time
    """
    audio_file = AudioFile(name, expansion, author, time)
    assert audio_file.name == name
    assert audio_file.expansion == expansion
    assert audio_file.executor == author
    assert audio_file.time == time


@pytest.mark.parametrize(
    'name, expansion, resolution, duration',
    [('video3', 'mp4', 1080, 15.5), ('video4', 'avi', 720, 20)],
        )
def test_video_file_creation(name: str, expansion: str, resolution: int, duration: int | float):
    """Test video file.

    Args:
        name (str): file name
        expansion (str): file expansion
        resolution (int): file resolutional
        duration (int | float): file duration
    """
    video_file = VideoFile(name, expansion, resolution, duration)
    assert video_file.name == name
    assert video_file.expansion == expansion
    assert video_file.resolution == resolution
    assert video_file.duration == duration


def test_media_library_add_remove_files():
    """Add to media and deleate."""
    media_library = MediaLibrary()

    audio_file = AudioFile('audio1', 'mp3', 'author1', 5)
    video_file = VideoFile('video2', 'mp4', 1000, DURATION)

    media_library.add_media_file(audio_file)
    media_library.add_media_file(video_file)

    assert len(media_library.list_of_media) == 2

    media_library.remove_media_file(audio_file)

    assert len(media_library.list_of_media) == 1
    assert video_file in media_library.list_of_media
    assert audio_file not in media_library.list_of_media


@pytest.mark.parametrize(
    'name, expansion, resolution, duration',
    [('video1', 'mp7', '1080p', 15)],
    )
def test_invalid_resolution_type(
    name: str, expansion: str, resolution: int, duration: int | float,
        ):
    """Test_invalid.

    Args:
        name (str): file name
        expansion (str): expansion file
        resolution (int): file resolution
        duration (int | float): duration file
    """
    with pytest.raises(TypeError):
        VideoFile(name, expansion, resolution, duration)


@pytest.mark.parametrize('name, expansion, resolution, duration', [('video1', 'mp6', 1080, '15s')])
def test_invalid_duration_type(name, expansion, resolution, duration):
    """Check for invalidity.

    Args:
        name (str): _description_
        expansion (int): _description_
        resolution (int): _description_
        duration (int | float): _description_
    """
    with pytest.raises(TypeError):
        VideoFile(name, expansion, resolution, duration)

