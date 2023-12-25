"""Архитектура классов для медиатеки."""
from typing import List


class MediaFile(object):
    """Класс, представляющий базовый медиафайл."""

    def __init__(self, filename: str, extension: str):
        """
        Инициализирует новый экземпляр класса MediaFile.

        Args:
            filename (str): название медиафайла
            extension (str): расширение медиафайла
        """
        self._filename = filename
        self._extension = extension

    @property
    def filename(self) -> str:
        """
        Возвращает название файла.

        Returns:
            _filename (str): название файла
        """
        return self._filename

    @filename.setter
    def filename(self, filename_value: str):
        """
        Устанавливает название файла.

        Args:
            filename_value (str): значение названия файла

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(filename_value, str):
            raise TypeError(
                'Значение {0} должно быть str, а не {1}'.format(
                    filename_value, type(filename_value).filename,
                ),
            )
        self._filename = filename_value

    @property
    def extension(self) -> str:
        """
        Возвращает расширение файла.

        Returns:
            extension (str): расширение файла
        """
        return self._extension

    @extension.setter
    def extension(self, extension_value: str):
        """
        Устанавливает расширение файла.

        Args:
            extension_value (str): значение расширения файла

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(extension_value, str):
            raise TypeError(
                'Значение {0} должно быть str, а не {1}'.format(
                    extension_value, type(extension_value).extension,
                ),
            )
        self._extension = extension_value


class AudioFile(MediaFile):
    """Класс, представляющий аудиофайл."""

    def __init__(
        self,
        filename: str,
        extension: str,
        artist: str,
        duration: float,
    ):
        """
        Инициализирует новый экземпляр класса AudioFile.

        Args:
            filename (str): название аудиофайла
            extension (str): расширение аудиофайла
            artist (str): имя исполнителя
            duration (float): длительность аудиофайла
        """
        super().__init__(filename, extension)
        self._artist = artist
        self._duration = duration

    @property
    def artist(self) -> str:
        """
        Возвращает исполнителя аудиофайла.

        Returns:
            _artist (str): исполнитель аудиофайла
        """
        return self._artist

    @artist.setter
    def artist(self, artist_value: str):
        """
        Устанавливает исполнителя аудиофайла.

        Args:
            artist_value (str): значение имени исполнителя аудиофайла

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(artist_value, str):
            raise TypeError(
                'Значение {0} должно быть str, а не {1}'.format(
                    artist_value, type(artist_value).name,
                ),
            )
        self._artist = artist_value

    @property
    def duration(self) -> float:
        """
        Возвращает длительность аудиофайла.

        Returns:
            duration(float): длительность аудиофайла
        """
        return self._duration

    @duration.setter
    def duration(self, duration_value: float):
        """
        Устанавливает длительность аудиофайла.

        Args:
            duration_value (float): значение длительности аудиофайла

        Raises:
            TypeError: если значение не является str
            ValueError: если значение меньше 0
        """
        if not isinstance(duration_value, float):
            raise TypeError(
                'Значение {0} должно быть float, а не {1}'.format(
                    duration_value, type(duration_value).duration,
                ),
            )
        if duration_value <= 0:
            raise ValueError('Значение должно быть положительным числом.')
        self._duration = duration_value


class VideoFile(MediaFile):
    """Класс, представляющий видеофайл."""

    def __init__(
        self,
        filename: str,
        extension: str,
        resolution: str,
        duration: float,
    ):
        """
        Инициализирует новый экземпляр класса VideoFile.

        Args:
            filename (str): название видеофайла
            extension (str): расширение видеофайла
            resolution (str): разрешение видеофайла
            duration (float): длительность видеофайла
        """
        super().__init__(filename, extension)
        self._resolution = resolution
        self._duration = duration

    @property
    def resolution(self) -> str:
        """
        Возвращает разрешение видеофайла.

        Returns:
            resolution (str): разрешение видеофайла
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution_value: str):
        """
        Устанавливает разрешение видеофайла.

        Args:
            resolution_value (str): значение разрешения видеофайла

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(resolution_value, str):
            raise TypeError(
                'Имя {0} должно быть str, а не {1}'.format(
                    resolution_value, type(resolution_value).resolution,
                ),
            )
        self._resolution = resolution_value

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность видеофайла.

        Returns:
            duration (float): продолжительность видеофайла
        """
        return self._duration

    @duration.setter
    def duration(self, duration_value: float):
        """
        Устанавливает продолжительность видеофайла.

        Args:
            duration_value (float): значение продолжительности видеофайла

        Raises:
            TypeError: если значение не является str
            ValueError: если длительность меньше 0
        """
        if not isinstance(duration_value, float):
            raise TypeError(
                'Имя {0} должно быть float, а не {1}'.format(
                    duration_value, type(duration_value).duration,
                ),
            )
        if duration_value <= 0:
            raise ValueError('Значение должно быть положительным числом')
        self._duration = duration_value


class MediaLibrary(object):
    """Класс, представляющий медиатеку."""

    def __init__(self):
        """Инициализирует новый экземпляр класса MediaLibrary."""
        self._media_files = []

    def add_media_file(self, media_file: MediaFile):
        """
        Добавляет медиафайл в медиатеку.

        Args:
            media_file (MediaFile): объект медиафайла
        """
        self._media_files.append(media_file)

    def remove_media_file(self, media_file: MediaFile):
        """
        Удаляет медиафайл из медиатеки.

        Args:
            media_file (MediaFile): объект медиафайла
        """
        if media_file in self._media_files:
            self._media_files.remove(media_file)

    def get_all_media_files(self) -> List[MediaFile]:
        """
        Возвращает список всех медиафайлов в медиатеке.

        Returns:
            _media_files: список всех медиафайлов
        """
        return self._media_files
