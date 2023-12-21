from typing import Any

class StatusError(Exception):
    def __init__(self) -> None:
        super().__init__('Incorrect status entered')

class Checkers():
    def check_type(instance: Any, required_type: type | tuple[type]):
        if not isinstance(instance, required_type):
            raise TypeError(f'Object must be {required_type}, but got other')
        
    def check_empty_string(string: str):
        if len(string) == 0:
            raise ValueError(f'This attribute cannot be empty string')
        
    def check_less_then_zero(amount: int):
        if amount < 0:
            raise ValueError('This attribute cannot be less then 0')


class Task():
    possible_statuses = ('wait', 'in work', 'on review', 'ready')

    def __init__(self, title: str, description: str, status: str) -> None:
        self.title = title
        self.description = description
        self.status = status

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title):
        Checkers.check_type(new_title, str)
        Checkers.check_empty_string(new_title)

        self.__title = new_title

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, new_description):
        Checkers.check_type(new_description, str)
        Checkers.check_empty_string(new_description)
        
        self.__description = new_description

    @property
    def status(self) -> str:
        return self.__status
    
    @status.setter
    def status(self, new_status: str) -> None:
        Checkers.check_type(new_status, str)
        Checkers.check_empty_string(new_status)
        if new_status.lower() not in self.possible_statuses:
            raise StatusError
        self.__status = new_status.lower()
        
class Project():
    def __init__(self, name: str, tasks: list[Task] | tuple[Task]) -> None:
        self.name = name
        self.tasks = tasks
    
    def add_task(self, new_task: Task) -> None:
        Checkers.check_type(new_task, Task)
        self.tasks.append(new_task)

    def delite_task(self, task_to_delite: Task):
        if task_to_delite not in self.tasks:
            raise ValueError(f'This task is not on the task list for project {self.name}')
        self.tasks.remove(task_to_delite)

    def show_tasks(self, filter: None | str = None) -> list[Task]:
        to_show = []
        if filter:
            for task in self.tasks:
                if task.status == filter:
                    to_show.append(task)
        else:
            to_show = self.tasks
        return to_show

class Member():
    def __init__(self, name, max_tasks: int, max_projects: int) -> None:
        self.name = name
        self.max_tasks = max_tasks
        self.max_projects = max_projects

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name) -> None:
        Checkers.check_type(new_name, str)
        Checkers.check_empty_string(new_name)
        self._name = new_name

    @property
    def max_tasks(self):
        return self.__max_tasks
    
    @max_tasks.setter
    def max_tasks(self, new_max):
        Checkers.check_type(new_max, int)
        Checkers.check_less_then_zero(new_max)
        self.__max_tasks = new_max

    @property
    def max_tasks(self):
        return self.__max_tasks
    
    @max_tasks.setter
    def max_tasks(self, new_max):
        Checkers.check_type(new_max, int)
        Checkers.check_less_then_zero(new_max)
        self.__max_tasks = new_max

class Team():
    def __init__(self, name: str, members: list[Member]) -> None:
        self.name = name
        self.members = members

    def add_member(self, new_member: Member) -> None:
        Checkers.check_type(new_member, Member)
        self.members.append(new_member)

    def delite_member(self, member_to_delite: Member):
        if member_to_delite not in self.members:
            raise ValueError(f'This member is not on the members list for team {self.name}')
        self.members.remove(member_to_delite)

    def show_members(self) -> list[Member]:
        return self.members