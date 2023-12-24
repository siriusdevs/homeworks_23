"""Модуль для класса Участник."""


class Member:
    """Класс Участник."""

    def __init__(self, name: str, max_count_tasks: int, max_count_projects: int) -> None:
        """Инициализация участника.

        Args:
            name (str): имя участника
            max_count_tasks (int): максимальное количество задач
            max_count_projects (int): максимальное количество проектов
        """
        self.name = name
        self.max_count_tasks = max_count_tasks
        self.max_count_projects = max_count_projects

    def __str__(self) -> str:
        """Метод строкового представления.

        Returns:
            str: имя, максимальное количество задач/проектов участника
        """
        return f'{self.name}, макс задач/проетов: {self.max_count_tasks}/{self.max_count_projects}'

    @property
    def name(self) -> str:
        """Геттер для имени участника.

        Returns:
            str: имя участника
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Сеттер для имени участника.

        Args:
            new_name (str): новое имя участника

        Raises:
            TypeError: ошибка, если новое имя участника не str
            ValueError: ошибка, если новое имя участника начинается не с заглавной
        """
        if not isinstance(new_name, str):
            msg = type(new_name).__name__
            raise TypeError(f'{msg} должен быть str!')
        if new_name != new_name.title():
            raise ValueError(f'{new_name} должно быть с большой буквы!')
        self._name = new_name

    @property
    def max_count_tasks(self) -> int:
        """Геттер для максимального количества задач участника.

        Returns:
            int: максимальное количество задач
        """
        return self._max_count_tasks

    @max_count_tasks.setter
    def max_count_tasks(self, new_value: int) -> None:
        """Сеттер для максимального количества задач участника.

        Args:
            new_value (int): новое максимальное количество задач участника

        Raises:
            TypeError: ошибка, если новое значение не int
            ValueError: ошибка, если новое значение меньше 0
        """
        if not isinstance(new_value, int):
            msg = type(new_value).__name__
            raise TypeError(f'{msg} должно быть int!')
        if new_value <= 0:
            raise ValueError(f'{new_value} должно быть не меньше 0!')
        self._max_count_tasks = new_value

    @property
    def max_count_projects(self) -> int:
        """Геттер для максимального количества проектов участника.

        Returns:
            int: максимальное количество проектов
        """
        return self._max_count_projects

    @max_count_projects.setter
    def max_count_projects(self, new_value: int) -> None:
        """Сеттер для максимального количества проектов участника.

        Args:
            new_value (int): новое максимальное количество проектов участника

        Raises:
            TypeError: ошибка, если новое значение не int
            ValueError: ошибка, если новое значение меньше 0
        """
        if not isinstance(new_value, int):
            msg = type(new_value).__name__
            raise TypeError(f'{msg} должно быть int!')
        if new_value <= 0:
            raise ValueError(f'{new_value} должно быть не меньше 0!')
        self._max_count_projects = new_value
