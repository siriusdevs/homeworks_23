"""This is sollution for homework 3.

Медиатека.
Опишите архитектуру классов для управления медиатекой (коллекцией мультимедийных файлов).
Вам нужно создать следующие классы:

Класс "Медиафайл":
Поля:
Название файла
Расширение файла
Методы:
Геттеры и сеттеры для полей

Класс "Аудиофайл" (наследуется от "Медиафайла"):
Дополнительные поля:
Исполнитель
Длительность
Методы:
Геттеры и сеттеры для дополнительных полей

Класс "Видеофайл" (наследуется от "Медиафайла"):
Дополнительные поля:
Разрешение
Продолжительность
Методы:
Геттеры и сеттеры для дополнительных полей

Класс "Медиатека":
Поля:
Список медиафайлов (массив или список объектов класса "Медиафайл")
Методы:
Добавить медиафайл в медиатеку
Удалить медиафайл из медиатеки
Получить список всех медиафайлов в медиатеке.
"""
from abc import ABC, abstractmethod

VALID_FILETYPES = ('.mp4', '.wav', '.mov', '.jpeg', '.jpg', '.png', '.svg', '.raw', '.mp3')


class InvalidMediafileType(Exception):
    """custom error unsupported or/and unexstining filetypes."""

    def __init__(self, filetype) -> None:
        """Error initialization.

        Args:
            filetype (_type_): given invalid filetype.
        """
        super().__init__(f'{type(filetype).__name__} is invalid filetype')


def filetype_checker(valid_filetypes: tuple[str], filetype: str) -> None:
    """Checker of validity for given filetype.

    Args:
        valid_filetypes (tuple[str]): tuple of valid filetypes
        filetype (str): filetype to check

    Raises:
        ValueError: if filetype does not start with a dot
        ValueError: if was not found in valid filetypes list
    """
    if not filetype.startswith('.'):
        raise ValueError(f'{filetype} does not start with . (dot)')
    if filetype not in valid_filetypes:
        raise ValueError(f'{filetype} does not count as valid MF type')


class Mediafile(ABC):
    """Instance of a mediafile."""

    @abstractmethod
    def __init__(
        self,
        filename: str,
        filetype: str,
    ) -> None:
        """File initialization.

        Args:
            filename (str): name of the instance
            filetype (str): filetype of the instance
        """
        self.filename, self.filetype = filename, filetype

    def __str__(self) -> str:
        """Representation in string for the instance.

        Returns:
            str: Class name, name and filetype of instance
        """
        return f'{self.__class__.__name__} {self.filename}{self.filetype}'

    @property
    def filename(self) -> str:
        """Getter for the filename property of instance.

        Returns:
            str: file name of the file.
        """
        return self._filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """Setter for filename property of instance.

        Args:
            new_filename (str): new filename to set

        Raises:
            TypeError: if the given name is not str
        """
        if not isinstance(new_filename, str):
            raise TypeError(f'{type(new_filename).__name__} was given instead of str')
        self._filename = new_filename

    @property
    def filetype(self) -> str:
        """Getter for the filetype of instance.

        Returns:
            str: filetype of this instance.
        """
        return self._filetype

    @filetype.setter
    def filetype(self, new_filetype: str) -> None:
        """Setter for the filetype of instance.

        Args:
            new_filetype (str): new filetype

        Raises:
            TypeError: if not string given as new filetypes
        """
        if not isinstance(new_filetype, str):
            raise TypeError(f'{type(new_filetype).__name__} was given instead of str')
        filetype_checker(VALID_FILETYPES, new_filetype)
        self._filetype = new_filetype


class AudioFile(Mediafile):
    """Audio file instance."""

    def __init__(
        self,
        filename: str,
        filetype: str,
        duration: int | float,
        author: str,
    ) -> None:
        """Audio file instance initialization.

        Args:
            filename (str): name of the file
            filetype (str): filetype of the file
            duration (int | float): duration of the audio file
            author (str): author/creator of the file
        """
        self.duration, self.author = duration, author
        super().__init__(filename, filetype)

    @property
    def duration(self) -> int | float:
        """Getter for the duration property of instance.

        Returns:
            int|float: duration of the file
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: int | float) -> None:
        """Setter for the duration property of instance.

        Args:
            new_duration (int | float): new value for duration

        Raises:
            TypeError: if not numeric duration given
            ValueError: if negative or 0 duration given
        """
        if not isinstance(new_duration, (int, float)):
            raise TypeError(f'{type(new_duration).__name__} was given instead of int or float')
        if new_duration <= 0:
            raise ValueError('Duration can not be negative or zero')
        self._duration = new_duration

    @property
    def author(self) -> str:
        """Getter for the author property of the instance.

        Returns:
            str: author of the file name
        """
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Setter for the author property of the instance.

        Args:
            new_author (str): new author name

        Raises:
            TypeError: if not string given as value
            ValueError: if empty string passed as value
        """
        if not isinstance(new_author, str):
            raise TypeError(f'{type(new_author).__name__} was given instead of str')
        if not len(new_author):
            raise ValueError('No name was provided.')
        self._author = new_author


class VideoFile(Mediafile):
    """Video file instance."""

    def __init__(
        self,
        filename: str,
        filetype: str,
        resolution: tuple[int, int],
        duration: int | float,
    ) -> None:
        """Video file instance initialization.

        Args:
            filename (str): name of the file
            filetype (str): filetype of the file
            resolution (tuple[int, int]): frame resolution
            duration (int | float): duration of the video
        """
        self.resolution, self.duration = resolution, duration
        super().__init__(filename, filetype)

    @property
    def resolution(self) -> tuple[int, int]:
        """Getter for the resolution property of the instance.

        Returns:
            tuple[int, int]: height and width of the frame
        """
        return self._resolution

    @resolution.setter
    def resolution(self, new_resolution: tuple[int, int]):
        """Setter for the resolution property of the instance.

        Args:
            new_resolution (tuple[int, int]): new height and width of the frame

        Raises:
            TypeError: if not tuple given (list is not good for this scenario)
            TypeError: if not int value in tuple given
            ValueError: if given resolution negative or equals 0
        """
        if not isinstance(new_resolution, tuple):
            raise TypeError(f'{type(new_resolution).__name__} was given instead of tuple')
        for dimmension in new_resolution:
            if not isinstance(dimmension, int):
                raise TypeError(f'{type(dimmension).__name__} was given instead of int')
            if dimmension <= 0:
                raise ValueError('Resolution can not be above or equal 0')
        self._resolution = new_resolution

    def get_total_points(self) -> str:
        """Fun function to get total count of points in frame.

        Returns:
            str: count of the points in the frame
        """
        return f'Total points in frame: {sum(self._resolution)}'

    @property
    def duration(self) -> int | float:
        """Getter for the duration property of the instance.

        Returns:
            int|float: duration of the video
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: int | float) -> None:
        """Setter for the duration property of the instance.

        Args:
            new_duration (int | float): new duration of the video

        Raises:
            TypeError: if not numeric duration given
            ValueError: if given duration is negative or equals 0
        """
        if not isinstance(new_duration, (int, float)):
            raise TypeError(f'{type(new_duration).__name__} was given instead of int or float')
        if new_duration <= 0:
            raise ValueError('Duration can not be negative or zero')
        self._duration = new_duration


class Mediateka:
    """Storage for all mediafiles instances."""

    def __init__(self, library: list[Mediafile]) -> None:
        """Mediateka instance initialization.

        Args:
            library (list[Mediafile]): library of Mediafiles stored inside
        """
        self.library = library

    def append_file(self, new_file: Mediafile) -> None:
        """Func that adds file to the library.

        Args:
            new_file (Mediafile): file to add to the library

        Raises:
            TypeError: if not Mediafile given as file to append
            ValueError: if given file already exists
        """
        if not isinstance(new_file, Mediafile):
            raise TypeError(f'{type(new_file).__name__} was given and not Mediafile')
        if new_file in self.library:
            raise ValueError(f'File <{new_file}> already exists')
        self.library.append(new_file)

    def remove_file(self, file_to_remove: Mediafile) -> None:
        """Func that removes given file from library.

        Args:
            file_to_remove (Mediafile): file to remove from library

        Raises:
            TypeError: if not Mediafile was given to remove
            ValueError: if given file does not exist in library
        """
        if not isinstance(file_to_remove, Mediafile):
            raise TypeError(f'{type(file_to_remove).__name__} was given and not Mediafile')
        if file_to_remove not in self.library:
            raise ValueError(f'There is no file <{file_to_remove}> is not in Mediateka')
        self.library.remove(file_to_remove)

    def get_files_list(self) -> list[Mediafile]:
        """Getter of the library list.

        Returns:
            list[Mediafile]: Mediateka itself
        """
        return f'Mediateka is: {self.library}'
