"""HW3 module."""

import re
from abc import ABC


class Mediafile(ABC):
    """Mediafile class."""

    def __init__(self, filename: str, extension: str):
        """
        Initialize Mediafile.

        Args:
            filename: str - name of the file
            extension: str - file extension
        """
        self.filename = filename
        self.extension = extension

    @property
    def filename(self) -> str:
        """
        Return filename.

        Returns:
            str - name of the file
        """
        return self._filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """
        Set filename.

        Args:
            new_filename: str - name of the file

        Raises:
            TypeError: if value is not a string
        """
        if not isinstance(new_filename, str):
            raise TypeError("filename must be a string")
        self._filename = new_filename

    @property
    def extension(self) -> str:
        """
        Return extension.

        Returns:
            str - file extension
        """
        return self._extension

    @extension.setter
    def extension(self, new_extension: str) -> None:
        """
        Set extension.

        Args:
            new_extension: str - file extension

        Raises:
            TypeError: if value is not a string
        """
        if not isinstance(new_extension, str):
            raise TypeError("extension must be a string")
        self._extension = new_extension


class Audiofile(Mediafile):
    """Audiofile class."""

    __match_args__ = ("filename", "extension", "author", "length")

    def __init__(self, filename: str, extension: str, author: str, length: int):
        """
        Initialize Audiofile.

        Args:
            filename: str - name of the file
            extension: str - file extension
            author: str - author of the audio
            length: int - length of the audio in seconds
        """
        super().__init__(filename, extension)
        self.author = author
        self.length = length

    def __str__(self) -> str:
        """
        Return string representation of Audiofile.

        Returns:
            str - string representation
        """
        return f"{self.filename}.{self.extension} by {self.author} ({self.length} seconds)"

    @property
    def author(self) -> str:
        """
        Return author.

        Returns:
            str - author of the audio
        """
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """
        Set author.

        Args:
            new_author: str - author of the audio

        Raises:
            TypeError: if value is not a string
        """
        if not isinstance(new_author, str):
            raise TypeError("Author must be a string")
        self._author = new_author

    @property
    def length(self) -> int:
        """
        Return length.

        Returns:
            int - length of the audio in seconds
        """
        return self._length

    @length.setter
    def length(self, new_length: int) -> None:
        """
        Set length.

        Args:
            new_length: int - length of the audio in seconds

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal 0
        """
        if not isinstance(new_length, int):
            raise TypeError("Length must be an integer")
        if new_length <= 0:
            raise ValueError("Length must be greater than 0")
        self._length = new_length


class Videofile(Mediafile):
    """Videofile class."""

    __match_args__ = ("filename", "extension", "length", "resolution")

    def __init__(self, filename: str, extension: str, length: int, resolution: str):
        """
        Initialize Videofile.

        Args:
            filename: str - name of the file
            extension: str - file extension
            length: int - length of the video in seconds
            resolution: str - resolution of the video
        """
        super().__init__(filename, extension)
        self.length = length
        self.resolution = resolution

    def __str__(self) -> str:
        """
        Return string representation of Videofile.

        Returns:
            str - string representation
        """
        return f"{self.filename}.{self.extension} ({self.length} seconds, {self.resolution})"

    @property
    def length(self) -> int:
        """
        Return length.

        Returns:
            int - length of the video in seconds
        """
        return self._length

    @length.setter
    def length(self, new_length: int) -> None:
        """
        Set length.

        Args:
            new_length: int - length of the video in seconds

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal 0
        """
        if not isinstance(new_length, int):
            raise TypeError("Length must be an integer")
        if new_length <= 0:
            raise ValueError("Length must be greater than 0")
        self._length = new_length

    @property
    def resolution(self) -> str:
        """
        Return resolution.

        Returns:
            str - resolution of the video
        """
        return self._resolution

    @resolution.setter
    def resolution(self, new_resolution: str) -> None:
        """
        Set resolution.

        Args:
            new_resolution: str - resolution of the video

        Raises:
            TypeError: if value is not a string
            ValueError: if value is not in the format 'WIDTHxHEIGHT'
        """
        if not isinstance(new_resolution, str):
            raise TypeError("Resolution must be a string")
        if re.match(r"^\d+x\d+$", new_resolution) is None:
            raise ValueError("Invalid resolution format. Use 'WIDTHxHEIGHT'")
        self._resolution = new_resolution


class MediaLibrary:
    """MediaLibrary class."""

    def __init__(self) -> None:
        """Initialize MediaLibrary."""
        self._mediafiles = []

    @property
    def mediafiles(self) -> list[Mediafile]:
        """
        Return mediafiles.

        Returns:
            list[Mediafile] - list of mediafiles
        """
        return self._mediafiles

    def add_mediafile(self, mediafile: Mediafile) -> None:
        """
        Add mediafile to the library.

        Args:
            mediafile: Mediafile - mediafile to be added

        Raises:
            ValueError: if mediafile is not an instance of Audiofile or Videofile
        """
        match mediafile:
            case Audiofile(filename, extension, author, length):
                self._mediafiles.append(mediafile)
            case Videofile(filename, extension, length, resolution):
                self._mediafiles.append(mediafile)
            case _:
                raise ValueError("Invalid mediafile type")

    def remove_mediafile(self, mediafile: Mediafile) -> None:
        """
        Remove mediafile from the library.

        Args:
            mediafile: Mediafile - mediafile to be removed
        """
        self._mediafiles.remove(mediafile)
