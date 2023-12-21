"""HW3 tests."""
from typing import Any

import pytest

from hw3 import Audiofile, MediaLibrary, Videofile

FILE_LENGTH = 120
NAME = "test_filename"
CODEC = "mp999"
AUTHOR = "test2"


@pytest.fixture
def audiofile(request: Any) -> Audiofile | Exception:
    """
    Audiofile fixture.

    Args:
        request (Any): pytest

    Returns:
        Audiofile | Exception
    """
    try:
        return Audiofile(*request.param)
    except Exception:
        return Exception


@pytest.fixture
def videofile(request) -> Videofile | Exception:
    """
    Videofile fixture.

    Args:
        request (Any): pytest

    Returns:
        Videofile | Exception
    """
    try:
        return Videofile(*request.param)
    except Exception:
        return Exception


@pytest.fixture
def medialibrary() -> MediaLibrary:
    """
    Game fixture.

    Returns:
        MediaLibrary
    """
    medialibrary_temp = MediaLibrary()
    medialibrary_temp.add_mediafile(
        Audiofile(NAME, CODEC, AUTHOR, FILE_LENGTH),
    )
    medialibrary_temp.add_mediafile(Videofile("test_videofile2", "mp4", FILE_LENGTH, "1920x1080"))
    return medialibrary_temp


TEST_AUDIOFILE = (
    ("test_audiofile", "mp3", "test_author", FILE_LENGTH),
    ("test_audiofile2", "mp3", "test_author2", FILE_LENGTH),
)


@pytest.mark.parametrize("audiofile", TEST_AUDIOFILE, indirect=True)
def test_audiofile(audiofile: Audiofile) -> None:  # noqa: WPS442
    """
    Test Audiofile class.

    Args:
        audiofile (Audiofile): Audiofile fixture

    Asserts:
        True if parameters are correct
    """
    for attr, attr_value in audiofile.__dict__.items():  # noqa: WPS609
        assert getattr(audiofile, attr) == attr_value


TEST_AUDIOFILE_FAIL = (
    ("test_audiofile", "mp3", 123, FILE_LENGTH),
    ("test_audiofile2", "mp33", "test_author", -FILE_LENGTH),
)


@pytest.mark.parametrize("audiofile", TEST_AUDIOFILE_FAIL, indirect=True)
def test_audiofile_fail(audiofile: Audiofile) -> None:  # noqa: WPS442
    """
    Test Audiofile class when its constructor fails.

    Args:
        audiofile (Audiofile): Audiofile fixture

    Asserts:
        True if fixture returns Exception
    """
    assert audiofile == Exception


TEST_VIDEOFILE = (
    ("test_videofile", "mp4", FILE_LENGTH, "1920x1080"),
    ("test_videofile20", "mp999", FILE_LENGTH, "100x1000"),
)


@pytest.mark.parametrize("videofile", TEST_VIDEOFILE, indirect=True)
def test_videofile(videofile: Videofile) -> None:  # noqa: WPS442
    """
    Test Videofile class.

    Args:
        videofile (Videofile): Videofile fixture

    Asserts:
        True if parameters are correct
    """
    for attr, attr_value in videofile.__dict__.items():  # noqa: WPS609
        assert getattr(videofile, attr) == attr_value


TEST_VIDEOFILE_FAIL = (
    ("test_videofile", "mp4", -FILE_LENGTH, "1920x1080"),
    ("test_videofile2", "mp5", FILE_LENGTH, "1920"),
    ("test_videofile2", "mp6", FILE_LENGTH, 1920),
)


@pytest.mark.parametrize("videofile", TEST_VIDEOFILE_FAIL, indirect=True)
def test_videofile_fail(videofile: Videofile) -> None:  # noqa: WPS442
    """
    Test Videofile class when its constructor fails.

    Args:
        videofile (Videofile): Videofile fixture

    Asserts:
        True if fixture returns Exception
    """
    assert videofile == Exception


def test_media_library_add(medialibrary: MediaLibrary) -> None:  # noqa: WPS442
    """
    Test MediaLibrary add_mediafile.

    Args:
        medialibrary (MediaLibrary): MediaLibrary fixture

    Asserts:
        True if operation succeeds
    """
    initial_len = len(medialibrary.mediafiles)
    medialibrary.add_mediafile(
        Audiofile(NAME, CODEC, AUTHOR, FILE_LENGTH),
    )
    assert len(medialibrary.mediafiles) == initial_len + 1


def test_media_library_remove(medialibrary: MediaLibrary) -> None:  # noqa: WPS442
    """
    Test Medialibrary remove_mediafile.

    Args:
        medialibrary (MediaLibrary): MediaLibrary fixture

    Asserts:
        True if operation succeeds
    """
    initial_len = len(medialibrary.mediafiles)
    temp_file = Audiofile(NAME, CODEC, AUTHOR, FILE_LENGTH)
    medialibrary.add_mediafile(temp_file)
    medialibrary.remove_mediafile(temp_file)
    assert len(medialibrary.mediafiles) == initial_len
