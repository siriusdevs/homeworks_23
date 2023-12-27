"""Модуль для класса Команда."""


from member import Member


class Team:
    """Класс Команда. Он может добавлять, удалять и показывать участников команды."""

    def __init__(self, team_name: str, list_members: list[Member]) -> None:
        """Инициализация команды.

        Args:
            team_name (str): название команды
            list_members (list[Member]): список участников
        """
        self.team_name, self.list_members = team_name, list_members

    def __str__(self) -> str:
        """Метод строкового представления.

        Returns:
            str: название команды
        """
        return f'{self.team_name}'

    @property
    def team_name(self) -> str:
        """Геттер для названия команды.

        Returns:
            str: название команды
        """
        return self._team_name

    @team_name.setter
    def team_name(self, new_name: str):
        """Сеттер для название команды.

        Args:
            new_name (str): новое название команды

        Raises:
            TypeError: ошибка, если новое название команды не str
        """
        if not isinstance(new_name, str):
            msg = type(new_name).__name__
            raise TypeError(f'{msg} должен быть str!')
        self._team_name = new_name

    @property
    def list_members(self) -> list[Member]:
        """Геттер для списка участников.

        Returns:
            list[Member]: список участников
        """
        return self._list_members

    @list_members.setter
    def list_members(self, new_list_members: list[Member]) -> None:
        """Сеттер для списка участников.

        Args:
            new_list_members (list[Member]): новый список участников

        Raises:
            TypeError: ошибка, если новый список участников не list
            TypeError: ошибка, если в новом списке участников, участник не Member
        """
        if not isinstance(new_list_members, list):
            msg = type(new_list_members).__name__
            raise TypeError(f'{msg} должнен быть list!')
        for member in new_list_members:
            if not isinstance(member, Member):
                msg = type(member).__name__
                raise TypeError(f'{msg} должен быть Member!')
        self._list_members = new_list_members

    def add_member(self, member: Member) -> None | str:
        """Добавить участника в команду.

        Args:
            member (Member): участник

        Raises:
            TypeError: ошибка, если участник не Member

        Returns:
            None | str: возвращает сообщение, если участник уже есть в команде
        """
        if not isinstance(member, Member):
            msg = type(member).__name__
            raise TypeError(f'{msg} должен быть Member!')
        if member not in self.list_members:
            self.list_members.append(member)
        else:
            return f'Участник {member.name} уже есть в команде!'

    def remove_member(self, member: Member) -> None | str:
        """Удалить участника из команды.

        Args:
            member (Member): участник

        Raises:
            TypeError: ошибка, если участник не Member

        Returns:
            None | str: возвращает сообщение, если участника нету в команде
        """
        if not isinstance(member, Member):
            msg = type(member).__name__
            raise TypeError(f'{msg} должен быть Member!')
        if member in self.list_members:
            self.list_members.remove(member)
        else:
            return f'задачи {member.name} нету в проекте!'

    def get_list_member(self) -> list:
        """Получить список всех участников команды.

        Returns:
            list: список всех участников команды
        """
        return [member.name for member in self.list_members]
