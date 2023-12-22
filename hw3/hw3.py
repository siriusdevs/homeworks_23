from typing import Any, List, Union


class StatusError(Exception):
    """Exception raised for errors in the input status."""

    def __init__(self) -> None:
        super().__init__('Incorrect status entered')


class Checkers:
    """A utility class for performing various checks."""

    @staticmethod
    def check_type(instance: Any, required_type: Union[type, tuple[type, ...]]):
        """Check if an object is of a specified type.

        Args:
            instance: The object to check.
            required_type: The type or tuple of types to check against.

        Raises:
            TypeError: If the object is not of the required type.
        """
        if not isinstance(instance, required_type):
            raise TypeError(f'Object must be {required_type}, got {type(instance)}.')

    @staticmethod
    def check_empty_string(string: str):
        """Check if a string is empty.

        Args:
            string: The string to check.

        Raises:
            ValueError: If the string is empty.
        """
        if not string:
            raise ValueError('This attribute cannot be an empty string.')

    @staticmethod
    def check_less_than_zero(amount: int):
        """Check if a number is less than zero.

        Args:
            amount: The number to check.

        Raises:
            ValueError: If the number is less than zero.
        """
        if amount < 0:
            raise ValueError('This attribute cannot be less than 0.')


class Task:
    """A class representing a task with a title, description, and status."""

    possible_statuses = ('wait', 'in work', 'on review', 'ready')

    def __init__(self, title: str, description: str, status: str) -> None:
        self.title = title
        self.description = description
        self.status = status

    @property
    def title(self) -> str:
        """Get the title of the task."""
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        """Set the title of the task, ensuring it's a non-empty string."""
        Checkers.check_type(new_title, str)
        Checkers.check_empty_string(new_title)
        self.__title = new_title

    @property
    def description(self) -> str:
        """Get the description of the task."""
        return self.__description

    @description.setter
    def description(self, new_description: str) -> None:
        """Set the description of the task, ensuring it's a non-empty string."""
        Checkers.check_type(new_description, str)
        Checkers.check_empty_string(new_description)
        self.__description = new_description

    @property
    def status(self) -> str:
        """Get the status of the task."""
        return self.__status

    @status.setter
    def status(self, new_status: str) -> None:
        """Set the status of the task, ensuring it's valid."""
        Checkers.check_type(new_status, str)
        Checkers.check_empty_string(new_status)
        if new_status.lower() not in self.possible_statuses:
            raise StatusError
        self.__status = new_status.lower()


class Project:
    """A class representing a project consisting of multiple tasks."""

    def __init__(self, name: str, tasks: Union[List[Task], tuple[Task, ...]]) -> None:
        self.name = name
        self.tasks = list(tasks)

    def add_task(self, new_task: Task) -> None:
        """Add a new task to the project."""
        Checkers.check_type(new_task, Task)
        self.tasks.append(new_task)

    def delete_task(self, task_to_delete: Task) -> None:
        """Delete a task from the project."""
        if task_to_delete not in self.tasks:
            raise ValueError(f'This task is not in the task list for project {self.name}')
        self.tasks.remove(task_to_delete)

    def show_tasks(self, filter: Union[None, str] = None) -> List[Task]:
        """Display tasks in the project, optionally filtered by status."""
        if filter:
            return [task for task in self.tasks if task.status == filter]
        return self.tasks


class Member:
    """A class representing a member with a task and project limit."""

    def __init__(self, name: str, max_tasks: int, max_projects: int) -> None:
        self.name = name
        self.max_tasks = max_tasks
        self.max_projects = max_projects

    @property
    def name(self) -> str:
        """Get the name of the member."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of the member, ensuring it's a non-empty string."""
        Checkers.check_type(new_name, str)
        Checkers.check_empty_string(new_name)
        self._name = new_name

    @property
    def max_tasks(self) -> int:
        """Get the maximum number of tasks for the member."""
        return self.__max_tasks

    @max_tasks.setter
    def max_tasks(self, new_max: int) -> None:
        """Set the maximum number of tasks for the member, ensuring it's non-negative."""
        Checkers.check_type(new_max, int)
        Checkers.check_less_than_zero(new_max)
        self.__max_tasks = new_max

    @property
    def max_projects(self) -> int:
        """Get the maximum number of projects for the member."""
        return self.__max_projects

    @max_projects.setter
    def max_projects(self, new_max: int) -> None:
        """Set the maximum number of projects for the member, ensuring it's non-negative."""
        Checkers.check_type(new_max, int)
        Checkers.check_less_than_zero(new_max)
        self.__max_projects = new_max


class Team:
    """A class representing a team consisting of multiple members."""

    def __init__(self, name: str, members: List[Member]) -> None:
        self.name = name
        self.members = members

    def add_member(self, new_member: Member) -> None:
        """Add a new member to the team."""
        Checkers.check_type(new_member, Member)
        self.members.append(new_member)

    def delete_member(self, member_to_delete: Member) -> None:
        """Delete a member from the team."""
        if member_to_delete not in self.members:
            raise ValueError(f'This member is not in the members list for team {self.name}')
        self.members.remove(member_to_delete)

    def show_members(self) -> List[Member]:
        """Display members of the team."""
        return self.members


