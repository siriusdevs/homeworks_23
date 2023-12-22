"""A module for testing hw3.py."""
import pytest

from hw3 import Checkers, Member, Project, StatusError, Task, Team


def test_checkers():
    """
    Test the Checkers utility class.

    This test includes the check_type, check_empty_string, and check_less_than_zero methods.
    """
    assert Checkers.check_type('test', str) is None  # should pass
    with pytest.raises(TypeError):
        test_for_error = 123
        Checkers.check_type(test_for_error, str)  # should raise TypeError

    assert Checkers.check_empty_string('not empty') is None  # should pass
    with pytest.raises(ValueError):
        Checkers.check_empty_string('')  # should raise ValueError

    assert Checkers.check_less_than_zero(5) is None  # should pass
    with pytest.raises(ValueError):
        Checkers.check_less_than_zero(-1)  # should raise ValueError


def test_task_creation():
    """
    Test the creation of a Task instance.

    This test verifies that a Task is created with correct title, description, and status.
    """
    task = Task('Test Task', 'Description', 'wait')
    assert task.title == 'Test Task'
    assert task.description == 'Description'
    assert task.status == 'wait'


def test_task_invalid_status():
    """
    Test the Task creation with an invalid status.

    This test expects a StatusError to be raised for an invalid task status.
    """
    with pytest.raises(StatusError):
        Task('Test Task', 'Description', 'invalid_status')


def test_project():
    """
    Test the creation and basic functionality of a Project instance.

    This test checks project creation and the ability to display tasks.
    """
    task1 = Task('Task 1', 'Description 1', 'wait')
    task2 = Task('Task 2', 'Description 2', 'in work')
    project = Project('Test Project', [task1, task2])
    assert project.name == 'Test Project'
    assert len(project.show_tasks()) == 2


def test_add_and_delete_task_in_project():
    """
    Test adding and deleting a task in a project.

    This test verifies that tasks can be added to and deleted from a project.
    """
    task = Task('New Task', 'New Description', 'wait')
    project = Project('Test Project', [])
    project.add_task(task)
    assert len(project.show_tasks()) == 1
    project.delete_task(task)
    assert not project.show_tasks()


def test_member():
    """
    Test the creation of a Member instance.

    This test verifies that a Member is created with correct name, max tasks, and max projects.
    """
    member = Member('John Doe', 5, 3)
    assert member.name == 'John Doe'
    assert member.max_tasks == 5
    assert member.max_projects == 3


def test_team():
    """
    Test the creation and basic functionality of a Team instance.

    This test checks team creation, adding and deleting members.
    """
    member1 = Member('John Doe', 5, 3)
    member2 = Member('Jane Doe', 4, 2)
    team = Team('Test Team', [member1])
    assert len(team.show_members()) == 1
    team.add_member(member2)
    assert len(team.show_members()) == 2
    team.delete_member(member1)
    assert len(team.show_members()) == 1
