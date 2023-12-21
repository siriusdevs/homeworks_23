"""Module include tests on Task and description."""
import pytest

from hw3 import Task

tasks = (
    ('Homework', 'Solve and add hw on github', 'In progress'),
    ('Chill', 'Get some relaxation, man.', 'Done'),
    ('Check hw', 'You, Albert Andreevich, are sleeping, and Im doing my homework.', 'done'),
    )


@pytest.mark.parametrize('title, description, state', tasks)
def test_task_param(title: str, description: str, state: str) -> None:
    """Check parameters.

    Args:
        title (str): name of task
        description (str): description of task
        state (str): state of task in list: in progress, done, not started
    """
    task = Task(title, description, state)
    assert task.title == title and task.description == description and task.state == state


@pytest.mark.xfail(raises=TypeError)
def test_invalid_type():
    """Check setter work."""
    with pytest.raises(TypeError):
        Task('Hw', 4, 'done')
    with pytest.raises(TypeError):
        Task(4, 'Assert data', 'in progress')


@pytest.mark.xfail(raises=ValueError)
def test_invalid_value():
    """Check setter work."""
    with pytest.raises(ValueError):
        Task('TAA', 'Work', 'Work is not wolf')
    with pytest.raises(ValueError):
        Task('GVA', 'Check wi-fi', 'Kommutattor is kommutating')
