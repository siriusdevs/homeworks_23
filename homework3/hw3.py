"""This module include class architecture."""
from typing import Any


def check(new_value, classes: tuple[type] | type[Any]):
    """Check if the given `new_value` is an instance of the provided `classes`.

    Parameters:
        new_value: The value to check.
        classes: A tuple or a single type representing the expected class(es).

    Raises:
        TypeError: If `new_value` is not an instance of `classes`.
    """
    if not isinstance(new_value, classes):
        value_class = type(new_value).__name__
        if isinstance(classes, tuple):
            classnames = [class_.__name__ for class_ in classes]
        else:
            classnames = classes.__name__
        raise TypeError(f'{new_value} of {value_class} should be as {classnames}')


class Task:
    """A class that represents an object with a title, description, and state."""

    _states = ['in progress', 'done', 'not started']

    def __init__(self, title: str, description: str, state: str) -> None:
        """Initialize a new instance of the class with the specified title, description, and state.

        Parameters:
            title (str): The title of the object.
            description (str): The description of the object.
            state (str): A string representing the state of the object.
        """
        self.title = title
        self.description = description
        self.state = state

    @property
    def title(self) -> str:
        """
        Get the self.title of the object.

        Returns:
            str: The title of the object.
        """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """
        Setter method for the title attribute.

        Parameters:
            new_title (str): The new title to be set.
        """
        check(new_title, str)
        self._title = new_title

    @property
    def description(self) -> str:
        """Get the description of the object.

        Returns:
            The description of the object.
        """
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        check(new_description, str)
        self._description = new_description

    @property
    def state(self) -> str:
        """
        Return the state of the object.

        Returns:
            A string representing the state of the object.
        """
        return self._state

    @state.setter
    def state(self, new_state: str) -> None:
        """
        Set the state of the object.

        Args:
            new_state (str): The new state to be set.

        Raises:
            ValueError: If the new_state is not a valid state.

        """
        check(new_state, str)
        if new_state.lower() not in self._states:
            raise ValueError(f'{new_state} is not in list, states include: {self._states}')
        self._state = new_state


class Project:
    """A class that represents an object with a title, description, and state."""

    _statuses = ['in progress', 'done', 'not started', 'all']

    def __init__(self, title: str, tasks: list[Task]) -> None:
        """Initialize an instance of the class.

        Args:
            title (str): The title of the instance.
            tasks (list[Task]): A list of tasks associated with the instance.
        """
        self.title, self.tasks = title, tasks

    def add_task(self, new_task: Task):
        """
        Add a new task to the task list.

        Parameters:
            new_task (Task): The new task to be added.

        Return:
            None
        """
        check(new_task, Task)
        if new_task not in self.tasks:
            self.tasks.append(new_task)

    def remove_task(self, cur_task: Task):
        """
        Remove a task from the task list.

        Parameters:
            cur_task (Task): The task to be removed.

        Raises:
            ValueError: If the task is not in the task list.
        """
        if cur_task not in self.tasks:
            raise ValueError(f'Task: {cur_task} not in tasks!')
        self.tasks.remove(cur_task)

    def filtered_task(self, status: str) -> list:
        """
        Filter tasks based on the given status.

        Parameters:
            status (str): The status to filter the tasks by.

        Returns:
            list: A list of tasks that match the given status.

        Raises:
            ValueError: If the given status is not found in the list of available statuses.
        """
        filtered = []
        if status.lower() not in self._statuses:
            raise ValueError(f'Filtered status {status} is not found, use: {self._statuses}!')
        if status.lower() == 'all':
            return self.tasks
        for task in self.tasks:
            if task.state is status:
                filtered.append(task.title)
        return f'{[item for item in filtered]}'


class Participant:
    """A class that represents Participant."""

    def __init__(self, name: str, max_tsk: int, max_proj: int) -> None:
        """Initialize a new instance of the class.

        Args:
            name (str): The name of the object.
            max_tsk (int): The maximum number of tasks.
            max_proj (int): The maximum number of projects.

        Return:
            None
        """
        self.name, self.max_tsk, self.max_proj = name, max_tsk, max_proj

    @property
    def name(self) -> str:
        """Get the name of the object.

        Returns:
            A string representing the name of the object.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the object.

        Args:
            new_name (str): The new name for the object.
        """
        check(new_name, str)
        self._name = new_name

    @property
    def max_tsk(self):
        """
        Get the maximum tsk value.

        Returns:
            int: The maximum tsk value.
        """
        return self._max_tsk

    @max_tsk.setter
    def max_tsk(self, new_max: int) -> None:
        """
        Set the maximum number of tasks.

        Parameters:
            new_max (int): The new maximum number of tasks.

        Return:
            None

        Raises:
            ValueError: If the new maximum number of tasks is less than 1.
        """
        check(new_max, int)
        if new_max >= 0:
            raise ValueError(f'Maximum task >= 1, not be {new_max}')
        self._max_tsk = new_max

    @property
    def max_proj(self):
        """
        Get the maximum projection value.

        Returns:
            float: The maximum projection value.
        """
        return self._max_proj

    @max_proj.setter
    def max_proj(self, new_max: int) -> None:
        """Set the maximum number of tasks.

        Args:
            new_max (int): The new maximum number of tasks.

        Raises:
            ValueError: if new_max >= 0
        """
        check(new_max, int)
        if new_max >= 0:
            raise ValueError(f'Maximum task >= 1, not be {new_max}')
        self._max_proj = new_max


class Team:
    """A class that represents Team."""

    def __init__(self, title: str, members: list[Participant]) -> None:
        """Initialize a new instance of the class.

        Args:
            title (str): The title of the instance.
            members (list[Participant]): The list of participants.

        Return:
            None
        """
        self.title, self.members = title, members

    def add_member(self, member: Participant) -> None:
        """
        Add a member to the team.

        Parameters:
            member (Participant): The participant to be added to the team.

        Raises:
            ValueError: if member not in self.members
        """
        check(member, Participant)
        if member not in self.members:
            self.members.append(member)
        else:
            raise ValueError('This member in team members')

    def remove_member(self, member: Participant) -> None:
        """
        Remove a member from the list of participants.

        Args:
            member (Participant): The member to be removed.

        Return:
            None

        Raises:
            ValueError: If the member is not in the list of participants.

        Example:
            remove_member(participant)
        """
        if member not in self.members:
            raise ValueError(f'Member: {member} not in members!')
        self.members.remove(member)

    def __str__(self) -> str:
        """Str representation of the object.

        Returns:
            The string representation of the object.
        """
        members_name = [member.name for member in self.members]
        return f'Members {self.title}: {members_name}'
