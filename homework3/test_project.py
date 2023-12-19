"""Module include tests on Project with Task and description."""
import pytest
from hw3 import Project, Task

task_project = [
    Task('Homework', 'Solve and add hw on github', 'in progress'),
    Task('Pet the cat', 'Its tough to pay attention to the worlds mst blvd animal', 'not started'),
    Task('Getting a masters student to write code', 'No comments', 'In progress'),
    Task('To disprove the big bang theory', 'Theres nothing here', 'not started'),
]

projects = (
    ('Typical Plan day', [task_project[0], task_project[2]]),
    ('Grigoryans plan', [task_project[3], task_project[0]]),
    ('Typical day in Sirius', [task_project[3]]),
)

my_project = (Project('Hell', [Task('Work in VK', 'nc', 'in progress')]))

my_startup = (
    (
        Project('FEDYASYS', [Task('HW', 'start', 'done'), Task('Test', 'write', 'in progress')]),
        "['HW']",
    ),
    (
        Project('Typical Plan day', [Task('Pet the cat', 'some', 'done'), Task(
            'Getting a masters student to write code', 'write', 'not started',
            ),
        ]),
        "['Pet the cat']",
    ),
)


@pytest.mark.parametrize('title, tasks', projects)
def test_task_param(title: str, tasks: list[Task]) -> None:
    """Check parameters.

    Args:
        title (str): name of project
        tasks (list[Task]): project tasks
    """
    project = Project(title, tasks)
    assert project.title == title and project.tasks == tasks


@pytest.mark.parametrize('task', task_project)
def test_append(task: Task) -> None:
    """Function which test add Task and remove Task.

    Args:
        task (Task): task object type Task
    """
    my_project.add_task(task)
    assert my_project.tasks[-1] == task

    my_project.remove_task(task)
    assert task not in my_project.tasks


@pytest.mark.parametrize('project, expected', my_startup)
def test_filtered(project: Project, expected: str) -> None:
    """Function which checking work filtered_task.

    Args:
        project (Project): object type Project
        expected (str): expected result
    """
    assert project.filtered_task('done') == expected
