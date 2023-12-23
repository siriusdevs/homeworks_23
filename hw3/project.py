"""Модуль для класса Проект."""


from task import Task


class Project:
    """Класс Проект. Он может добавлять, удалять и показывать задачи проекта."""

    def __init__(self, project_name: str, task_list: list[Task]) -> None:
        """Инициализация проекта.

        Args:
            project_name (str): название проекта
            task_list (list[Task]): список задач
        """
        self.project_name, self.task_list = project_name, task_list

    def __str__(self) -> str:
        """Метод строкового представления.

        Returns:
            str: название проекта
        """
        return f'{self.project_name}'

    @property
    def project_name(self) -> str:
        """Геттер для названия проекта.

        Returns:
            str: название проекта
        """
        return self._project_name

    @project_name.setter
    def project_name(self, new_project_name: str) -> None:
        """Сеттер для названия проекта.

        Args:
            new_project_name (str): новое название проекта

        Raises:
            TypeError: ошибка, если новое название проекта не str
        """
        if not isinstance(new_project_name, str):
            msg = type(new_project_name).__name__
            raise TypeError(f'{msg} должен быть str!')
        self._project_name = new_project_name

    @property
    def task_list(self) -> list[Task]:
        """Геттер для списка задач.

        Returns:
            list[Task]: список задач
        """
        return self._task_list

    @task_list.setter
    def task_list(self, new_task_list: list[Task]) -> None:
        """Сеттер для списка задач.

        Args:
            new_task_list (list[Task]): новый список задач

        Raises:
            TypeError: ошибка, если новый список задач не list
            TypeError: ошибка, если в новом списке задач, задача не Task
        """
        if not isinstance(new_task_list, list):
            msg = type(new_task_list).__name__
            raise TypeError(f'{msg} должен быть list!')
        for task in new_task_list:
            if not isinstance(task, Task):
                msg = type(task).__name__
                raise TypeError(f'{msg} должен быть Task!')
        self._task_list = new_task_list

    def add(self, task: Task) -> None | str:
        """Добавить задачу в проект.

        Args:
            task (Task): задача

        Raises:
            TypeError: ошибка, если задача не Task

        Returns:
            None | str: возвращает сообщение, если задача уже есть в проекте
        """
        if not isinstance(task, Task):
            msg = type(task).__name__
            raise TypeError(f'{msg} должен быть Task!')
        if task not in self.task_list:
            self.task_list.append(task)
        else:
            return f'задача {task.task_name} уже есть в проекте!'

    def remove(self, task: Task) -> None | str:
        """Удалить задачу из проекта.

        Args:
            task (Task): задача

        Raises:
            TypeError: ошибка, если задача не Task

        Returns:
            None | str: возвращает сообщение, если задачи нету в проекте
        """
        if not isinstance(task, Task):
            msg = type(task).__name__
            raise TypeError(f'{msg} должен быть Task!')
        if task in self.task_list:
            self.task_list.remove(task)
        else:
            return f'задачи {task.task_name} нету в проекте!'

    def get(self, filt: str = None) -> None | list:
        """получить список всех задач в проекте с возможностью передачи фильтра статуса задач.

        Args:
            filt (str): Фильтер по статусу. Значение по умолчанию None.

        Returns:
            None | list: возвращает список задач в проекте по фильтру или None,\
                        если фильтр не проходит
        """
        if filt not in Task.statuses and filt is not None:
            return None
        res = [task.task_name for task in self.task_list if task.status == filt or filt is None]
        if res:
            return res
        return None
