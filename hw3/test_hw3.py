"""Those are the test for hw3."""
from typing import Any

import pytest

import hw3

SAMPLE_DURATION = 14
SAMPLE_DURATION2 = 333
SAMPLE_VALUE = 3.5
VIDEO1 = hw3.VideoFile('Yo', '.mov', (10, 12), 1)
VIDEO2 = hw3.VideoFile('aaaaaaaaa', '.mp4', (10, 12), SAMPLE_DURATION)
VIDEO3 = hw3.VideoFile('Coolname', '.mov', (123, 44), 10)
AUDIO = hw3.AudioFile('aaaa', '.mp3', SAMPLE_DURATION2, 'Jacob')
FILENAME = 'aaaaaaaaa'
VIDEO_FORMAT = '.mp4'
AUDIO_FORMAT = '.mp3'
test_valid_video = (
    (FILENAME, VIDEO_FORMAT, (10, 12), 14, 'VideoFile aaaaaaaaa.mp4'),
    ('Yo', '.mov', (10, 12), 14, 'VideoFile Yo.mov'),
    (
        'Rick Astley - NeverGonnaGiveYouUp',
        VIDEO_FORMAT,
        (1920, 1080),
        196,
        'VideoFile Rick Astley - NeverGonnaGiveYouUp.mp4',
    ),
)

test_valid_audio = (
    (
        FILENAME,
        AUDIO_FORMAT,
        SAMPLE_VALUE,
        'It is how it is',
        'AudioFile aaaaaaaaa.mp3',
    ),
)

test_mediateka_data = (
    (
        [
            VIDEO1,
            VIDEO2,
            AUDIO,
        ],
        f'Mediateka is: {[VIDEO1, VIDEO2, VIDEO3]}',
    ),
)


@pytest.mark.parametrize('filename, filetype, param1, param2, expected', test_valid_video)
def test_comparison_valid_video(
    filename: str,
    filetype: str,
    param1: Any,
    param2: Any,
    expected: str,
) -> None:
    """Test for valid VideoFile instance creation.

    Args:
        filename (str): name of the file instance
        filetype (str): type of the file
        param1 (Any): first parameter of instance
        param2 (Any): second parameter of instance
        expected (str): awaited str representation of instance
    """
    test_str = str(hw3.VideoFile(filename, filetype, param1, param2))
    assert test_str == expected


@pytest.mark.parametrize('files_list, expected', test_mediateka_data)
def test_mediateka(files_list: list[hw3.Mediafile], expected: str) -> None:
    """Test for valid Mediateka work process.

    Args:
        files_list (list[Mediafile]): list of the files in mediateka
        expected (str): awaited result list of files in meidateka
    """
    lib = hw3.Mediateka(files_list)
    lib.append_file(VIDEO3)
    lib.remove_file(AUDIO)
    test_list = lib.get_files_list()
    assert test_list == expected


@pytest.mark.parametrize('filename, filetype, param1, param2, expected', test_valid_audio)
def test_comparison_valid_small(
    filename: str,
    filetype: str,
    param1: Any,
    param2: Any,
    expected: str,
) -> None:
    """Test for valid AudioFile instance creation.

    Args:
        filename (str): name of the file instance
        filetype (str): file type of the file
        param1 (Any): first parameter of the instance
        param2 (Any): second parameter of the instance
        expected (str): awaited str representation of instance
    """
    test_str = str(hw3.AudioFile(filename, filetype, param1, param2))
    assert test_str == expected


@pytest.mark.xfail
def test_for_fail_audio_fst():
    """Test for fail in AudioFile creation with error in fst param."""
    hw3.AudioFile(FILENAME, AUDIO_FORMAT, -1, 'yo')


@pytest.mark.xfail
def test_for_fail_audio_snd():
    """Test for fail in AudioFile creation with error in snd param."""
    hw3.AudioFile(FILENAME, AUDIO_FORMAT, 1000, [])


@pytest.mark.xfail
def test_for_fail_video_first():
    """Test for fail in VideoFile creation with error in fst param."""
    hw3.VideoFile(FILENAME, VIDEO_FORMAT, ('asd', 12), SAMPLE_DURATION)


@pytest.mark.xfail
def test_for_fail_video_snd():
    """Test for fail in VideoFile creation with error in snd param."""
    hw3.VideoFile(FILENAME, VIDEO_FORMAT, (10, 12), -1)
