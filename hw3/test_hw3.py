import pytest
from hw3 import StatusError, Checkers, Task, Project, Member, Team


def test_checkers():
    # Test check_type
    assert Checkers.check_type("test", str) is None  # should pass
    with pytest.raises(TypeError):
        Checkers.check_type(123, str)  # should raise TypeError

    # Test check_empty_string
    assert Checkers.check_empty_string("not empty") is None  # should pass
    with pytest.raises(ValueError):
        Checkers.check_empty_string("")  # should raise ValueError

    # Test check_less_than_zero
    assert Checkers.check_less_than_zero(5) is None  # should pass
    with pytest.raises(ValueError):
        Checkers.check_less_than_zero(-1)  # should raise ValueError

def test_task_creation():
    task = Task("Test Task", "Description", "wait")
    assert task.title == "Test Task"
    assert task.description == "Description"
    assert task.status == "wait"

def test_task_invalid_status():
    with pytest.raises(StatusError):
        Task("Test Task", "Description", "invalid_status")

def test_project():
    task1 = Task("Task 1", "Description 1", "wait")
    task2 = Task("Task 2", "Description 2", "in work")
    project = Project("Test Project", [task1, task2])
    assert project.name == "Test Project"
    assert len(project.show_tasks()) == 2

def test_add_and_delete_task_in_project():
    task = Task("New Task", "New Description", "wait")
    project = Project("Test Project", [])
    project.add_task(task)
    assert len(project.show_tasks()) == 1
    project.delete_task(task)
    assert len(project.show_tasks()) == 0

def test_member():
    member = Member("John Doe", 5, 3)
    assert member.name == "John Doe"
    assert member.max_tasks == 5
    assert member.max_projects == 3

def test_team():
    member1 = Member("John Doe", 5, 3)
    member2 = Member("Jane Doe", 4, 2)
    team = Team("Test Team", [member1])
    assert len(team.show_members()) == 1
    team.add_member(member2)
    assert len(team.show_members()) == 2
    team.delete_member(member1)
    assert len(team.show_members()) == 1
