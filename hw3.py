"""imports an abstract method."""

from abc import ABC, abstractmethod


def check_media_file(name: str, expansion: str):
    """_summary_.

    Args:
        name (str): the name of the object
        expansion (str): object expansion

    Raises:
        ValueError: type check
    """
    if not isinstance(name, str):
        raise ValueError('the type should be str')
    if not isinstance(expansion, str):
        raise ValueError('the type should be int')


def check_audio_file(author: str, time: int | float):
    """Сheck the type.

    Args:
        author (str): file author
        time (int | float): file time

    Raises:
        TypeError: type check
    """
    if not isinstance(author, str):
        raise TypeError('should be str')
    if not isinstance(time, int | float):
        raise TypeError(' should be int | float')


def check_video_file(resolution: int, duration: int | float):
    """Check.

    Args:
        resolution (int):  file resolution
        duration (int | float): file duration

    Raises:
        TypeError: type check
    """
    if not isinstance(resolution, int):
        raise TypeError('Resolution must be a string.')
    if not isinstance(duration, (int, float)):
        raise TypeError('Duration must be a numeric value.')


class MediaFile(ABC):
    """_summary_.

    Args:
        ABC : inheritance class

    Raises:
        TypeError: checking for the correct type of variable

    Returns:
        nothing
    """

    @abstractmethod
    def __init__(self, name: str, expansion: str) -> None:
        """initialize.

        Args:
            name (str): the name of the object
            expansion (str):  object expansion
        """
        self._name = name
        self._expansion = expansion
        check_media_file(self.name, self.expansion)

    @property
    def name(self) -> None:
        """Returns name.

        Returns:
            name(str): the name of the object
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Redefine name.

        Args:
            new_name (str): the new name of the object

        Raises:
            TypeError: check
        """
        if not isinstance(new_name, str):
            raise TypeError('check')
        self._name = new_name

    @property
    def expansion(self) -> None:
        """Retuns expension.

        Returns:
            expansion: object expansion
        """
        return self._expansion

    @expansion.setter
    def expension(self, new_expension) -> None:
        """Redefine the expansion.

        Args:
            new_expension (str): new expansion

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_expension, str):
            raise TypeError('check')
        self._expansion = new_expension


class AudioFile(MediaFile):
    """creates a class.

    Args:
        MediaFile (_type_): nothing
    """

    def __init__(self, name: str, expansion: str, author: str, time: int | float) -> None:
        """initialize.

        Args:
            name (str): the name of the object
            expansion (str): object expansion
            author (str): the author of the file
            time (int | float): file duration
        """
        super().__init__(name, expansion)
        self._author = author
        self._time = time
        check_audio_file(author, time)

    @property
    def executor(self) -> None:
        """Retuns author.

        Returns:
            author(str): the author of the file
        """
        return self._author

    @executor.setter
    def executor(self, new_author):
        """Do a check and redefine.

        Args:
            new_author (_type_):   the new author of the file

        Raises:
            TypeError: check

        """
        if not isinstance(new_author, str):
            raise TypeError('ty not string')
        self._author = new_author

    @property
    def time(self) -> None:
        """Retuns time.

        Returns:
            self.time : time
        """
        return self._time

    @time.setter
    def time(self, new_time: int | float) -> None:
        """Redefines the time.

        Args:
            new_time (int | float): new time

        Raises:
            TypeError: check
        """
        if not isinstance(new_time, float | int):
            raise TypeError('wrong type')
        self._time = new_time

    def __str__(self) -> None:
        """Return the line.

        Returns:
            str: nothing
        """
        return f' audio_file:{self.name},{self.expansion},{self._author},{self.time}'


class VideoFile(MediaFile):
    """creates a class.

    Args:
        MediaFile (class): class Mediafile
    """

    def __init__(self, name: str, expansion: str, resolution: int, duration: int | float) -> None:
        """Initialize.

        Args:
            name (str):  the name of the object
            expansion (str): expansion object
            resolution (int): file resolution
            duration (int | float): duration file
        """
        super().__init__(name, expansion)
        self._resolution = resolution
        self._duration = duration
        check_video_file(resolution, duration)

    @property
    def resolution(self) -> None:
        """Retuns self._resolution.

        Returns:
            self._resolution: file resolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, new_resolution) -> None:
        """Do a check and redefine.

        Args:
            new_resolution (int): new resolution

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_resolution, int):
            raise TypeError('the wrong type')
        self._resolution = new_resolution

    @property
    def duration(self) -> None:
        """Retuns duration.

        Returns:
            self._duration:  duration
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        """Do a check and redefine.

        Args:
            new_duration (int): new duration

        Raises:
            TypeError: checking for the type of variable
        """
        if not isinstance(new_duration, int | float):
            raise TypeError(f'the wrong type {new_duration}')
        self.duration = new_duration

    def __str__(self) -> str:
        """Output a string representation.

        Returns:
            str: nothing
        """
        return f'Video_file: {self.name}, {self.expansion} {self.resolution}, {self._duration}'


class MediaLibrary:
    """creates a class."""

    def __init__(self) -> None:
        """Initialize."""
        self.list_of_media: list = []

    def add_media_file(self, media_file: MediaFile) -> None:
        """Add it to the list and display it.

        Args:
            media_file(MediaFile): instance of the class

        Returns:
            self.list_of_media : a list with files
        """
        self.list_of_media.append(media_file)
        return self.list_of_media

    def remove_media_file(self, media_file: MediaFile) -> None:
        """Delete the file and display the list.

        Args:
            media_file( MediaFile): instance of the class

        Returns:
            self.list_of_media: a list with files
        """
        self.list_of_media.remove(media_file)
        return self.list_of_media

    def __str__(self) -> None:
        """Output a string representation.

        Returns:
            str: a string with files
        """
        m_list = [' ; '.join(str(file_list) for file_list in self.list_of_media)]

        return f'{m_list}'
