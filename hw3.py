"""imports an abstract method."""

from abc import ABC, abstractmethod


def check(name, expansion):
    """_summary_.

    Args:
        name (_type_): _description_
        expansion (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
    """
    if not isinstance(name, str):
        raise ValueError('the type should be str')
    if not isinstance(expansion, str):
        raise ValueError('the type should be int')


class MediaFile(ABC):
    """_summary_.

    Args:
        ABC (_type_): _description_

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """

    @abstractmethod
    def __init__(self, name: str, expansion: str) -> None:
        """_summary_.

        Args:
            name (str): _description_
            expansion (str): _description_
        """
        self._name = name
        self._expansion = expansion
        check(self.name, self.expansion)

    @property
    def name(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._name

    @name.setter
    def name(self, new_name) -> None:
        """_summary_.

        Args:
            new_name (_type_): _description_

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_name, str):
            raise TypeError('wrong type')
        self._name = new_name

    @property
    def expansion(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._expansion

    @expansion.setter
    def expension(self, new_expension) -> None:
        """_summary_.

        Args:
            new_expension (_type_): _description_

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_expension, str):
            raise TypeError('the wrong type')
        self._expansion = new_expension


class AudioFile(MediaFile):
    """_summary_.

    Args:
        MediaFile (_type_): _description_
    """

    def __init__(self, name: str, expansion: str, author: str, time: int | float) -> None:
        """_summary_.

        Args:
            name (str): _description_
            expansion (str): _description_
            author (str): _description_
            time (int | float): _description_
        """
        super().__init__(name, expansion)
        self._author = author
        self._time = time

    @property
    def executor(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._author

    @executor.setter
    def executor(self, new_author):
        """_summary_.

        Args:
            new_author (_type_): _description_

        Raises:
            TypeError: wrong type error

        """
        if not isinstance(new_author, str):
            raise TypeError('the wrong type')
        self._author = new_author

    @property
    def time(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._time

    @time.setter
    def time(self, new_time) -> None:
        """_summary_.

        Args:
            new_time (_type_): _description_

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_time, float | int):
            raise TypeError('the wrong type')
        self._time = new_time

    def __str__(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return f'audio_file: {self.name}, {self.expansion}, {self._author}, {self.time}'


class VideoFile(MediaFile):
    """_summary_.

    Args:
        MediaFile (_type_): _description_
    """

    def __init__(self, name: str, expansion: str, resolution: int, duration: int | float) -> None:
        """_summary_.

        Args:
            name (str): _description_
            expansion (str): _description_
            resolution (int): _description_
            duration (int | float): _description_
        """
        super().__init__(name, expansion)
        self._resolution = resolution
        self._duration = duration

    @property
    def resolution(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._resolution

    @resolution.setter
    def resolution(self, new_resolution) -> None:
        """_summary_.

        Args:
            new_resolution (_type_): _description_

        Raises:
            TypeError: wrong type error
        """
        if not isinstance(new_resolution, int):
            raise TypeError('the wrong type')
        self._resolution = new_resolution

    @property
    def duration(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        """_summary_.

        Args:
            new_duration (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(new_duration, int | float):
            raise TypeError(f'the wrong type {new_duration}')
        self.duration = new_duration

    def __str__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return f'Video_file: {self.name}, {self.expansion} {self.resolution}, {self._duration}'


class MediaLibrary:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        self.list_of_media: list = []

    def add_media_file(self, media_file: MediaFile) -> None:
        """_summary_.

        Args:
            media_file: _description_

        Returns:
            _type_: _description_
        """
        self.list_of_media.append(media_file)
        return self.list_of_media

    def remove_media_file(self, media_file: MediaFile) -> None:
        """_summary_.

        Args:
            media_file: _description_

        Returns:
            _type_: _description_
        """
        self.list_of_media.remove(media_file)
        return self.list_of_media

    def __str__(self) -> None:
        """_summary_.

        Returns:
            _type_: _description_
        """
        m_list = [' ; '.join(str(file_list) for file_list in self.list_of_media)]

        return f'{m_list}'
