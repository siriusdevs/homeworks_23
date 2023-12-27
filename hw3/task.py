"""Модуль для класса Задача."""


class Task:
    """Класс Задача."""

    statuses = ('выполняется', 'завершена', 'приостановлена')

    def __init__(self, task_name: str, description: str, status: str) -> None:
        """Инициализировать Задачу.

        Args:
            task_name (str): название задачи
            description (str): описание задачи
            status (str): статус задачи
        """
        self.task_name, self.description, self.status = task_name, description, status

    def __str__(self) -> str:
        """Метод строкового представления.

        Returns:
            str: название, описание, статус задачи
        """
        return f'{self.task_name}, {self.description}, {self.status}'

    @property
    def task_name(self) -> str:
        """Геттер для названия задачи.

        Returns:
            str: название задачи
        """
        return self._task_name

    @task_name.setter
    def task_name(self, new_task_name: str) -> None:
        """Сеттер для названия задачи.

        Args:
            new_task_name (str): новое название задачи

        Raises:
            TypeError: ошибка, если новое имя не str
        """
        if not isinstance(new_task_name, str):
            msg = type(new_task_name).__name__
            raise TypeError(f'{msg} должен быть str!')
        self._task_name = new_task_name

    @property
    def description(self) -> str:
        """Геттер для описания задачи.

        Returns:
            str: описание задачи
        """
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        """Сеттер для описания задачи.

        Args:
            new_description (str): новое описание задачи

        Raises:
            TypeError: ошибка, если новое описание задачи не str
        """
        if not isinstance(new_description, str):
            msg = type(new_description).__name__
            raise TypeError(f'{msg} должен быть str!')
        self._description = new_description

    @property
    def status(self) -> str:
        """Геттер для статуса задачи.

        Returns:
            str: статус задачи
        """
        return self._status

    @status.setter
    def status(self, new_status: str) -> None:
        """Сеттер для статуса задачи.

        Args:
            new_status (str): новый статус задачи

        Raises:
            TypeError: ошибка, если новый статус задачи не str
            ValueError: ошибка, если нового статуса задачи не существует
        """
        if not isinstance(new_status, str):
            msg = type(new_status).__name__
            raise TypeError(f'{msg} должен быть str!')
        if new_status not in self.statuses:
            raise ValueError('Такого статуса нету!')
        self._status = new_status
