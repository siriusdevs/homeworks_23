"""Модуль тесты hw3."""

import pytest

from member import Member
from project import Project
from task import Task
from team import Team

task1 = Task('Задание1', 'Описание задач', 'выполняется')
task2 = Task('задание2', 'описание задачи', 'завершена')
task3 = Task('задание3', 'описание Задачи', 'приостановлена')

TASK_DATA = (
    (
        ('Задание1', 'Описание задач', 'выполняется'),
        (task1),
    ),
    (
        ('задание2', 'описание задачи', 'завершена'),
        (task2),
    ),
    (
        ('задание3', 'описание Задачи', 'приостановлена'),
        (task3),
    ),
)

project1 = Project('Проект1', [task1, task2])
project2 = Project('Проект2', [task1, task2, task3])

PROJECT_DATA = (
    (
        ('Проект1', [task1, task2]),
        (project1),
    ),
    (
        ('Проект2', [task1, task2, task3]),
        (project2),
    ),
)

ADD_PROJECT_DATA = (
    (
        project1, task3, [task1, task2, task3],
    ),
    (
        project2, task2, [task1, task2, task3],
    ),
)

REMOVE_PROJECT_DATA = (
    (
        project1, task1, [task2, task3],
    ),
    (
        project2, task2, [task1, task3],
    ),
)

member1 = Member('Миша', 3, 3)
member2 = Member('Данил', 5, 6)
member3 = Member('Денис', 9, 8)

MEMBER_DATA = (
    (
        ('Миша', 3, 3),
        (member1),
    ),
    (
        ('Денис', 9, 8),
        (member3),
    ),
)

team1 = Team('команда1', [member1, member2])
team2 = Team('команда2', [member3, member2])

TEAM_DATA = (
    (
        ('команда1', [member1, member2]),
        (team1),
    ),
    (
        ('команда2', [member3, member2]),
        (team2),
    ),
)

ADD_TEAM_DATA = (
    (
        team1, member3, [member1, member2, member3],
    ),
    (
        team2, member1, [member3, member2, member1],
    ),
)

REMOVE_TEAM_DATA = (
    (
        team1, member1, [member2, member3],
    ),
    (
        team2, member2, [member3, member1],
    ),
)

INFORMATION = 'information'
EXPECTED = 'expected'
COMMA = ','


@pytest.mark.parametrize(f'{INFORMATION}{COMMA} {EXPECTED}', TASK_DATA)
def test_task(information: tuple[str], expected: Task) -> None:
    """Тест создание задач.

    Args:
        information (tuple[str]): данные
        expected (Task): задача
    """
    assert str(Task(*information)) == str(expected)


@pytest.mark.parametrize(f'{INFORMATION}{COMMA} {EXPECTED}', PROJECT_DATA)
def test_project(information: tuple[str, list[Task]], expected: Project) -> None:
    """Тест создание проекта.

    Args:
        information (tuple[str, list[Task]]): данные
        expected (Project): проект
    """
    res = Project(*information)
    assert res.get() == expected.get() and str(res) == str(expected)


@pytest.mark.parametrize(f'project{COMMA} task{COMMA} {EXPECTED}', ADD_PROJECT_DATA)
def test_add_project(project: Project, task: Task, expected: list[Task]):
    """Тест добавление задачи в проект.

    Args:
        project (Project): проект
        task (Task): задача
        expected (list[Task]): список задач
    """
    project.add(task)
    assert project.get() == [arg.task_name for arg in expected]


@pytest.mark.parametrize(f'project{COMMA} task{COMMA} {EXPECTED}', REMOVE_PROJECT_DATA)
def test_remove_project(project: Project, task: Task, expected: list[Task]):
    """Тест удаление задачи из проекта.

    Args:
        project (Project): проект
        task (Task): задача
        expected (list[Task]): список задач
    """
    project.remove(task)
    assert project.get() == [arg.task_name for arg in expected]


@pytest.mark.parametrize(f'{INFORMATION}{COMMA} {EXPECTED}', MEMBER_DATA)
def test_member(information: tuple[str], expected: Member) -> None:
    """Тест создание участника.

    Args:
        information (tuple[str]): данные
        expected (Member): участник
    """
    assert str(Member(*information)) == str(expected)


@pytest.mark.parametrize(f'{INFORMATION}{COMMA} {EXPECTED}', TEAM_DATA)
def test_team(information: tuple[str, list[Member]], expected: Team) -> None:
    """Тест создание команды.

    Args:
        information (tuple[str, list[Member]]): данные
        expected (Team): команда
    """
    res = Team(*information)
    assert res.get() == expected.get() and str(res) == str(expected)


@pytest.mark.parametrize(f'team{COMMA} member{COMMA} {EXPECTED}', ADD_TEAM_DATA)
def test_add_team(team: Team, member: Member, expected: list[Member]):
    """Тест добавление участника в команду.

    Args:
        team (Team): команда
        member (Member): участник
        expected (list[Member]): список участников
    """
    team.add(member)
    assert team.get() == [arg.name for arg in expected]


@pytest.mark.parametrize(f'team{COMMA} member{COMMA} {EXPECTED}', REMOVE_TEAM_DATA)
def test_remove_team(team: Team, member: Member, expected: list[Member]):
    """Тест удаление участника из команды.

    Args:
        team (Team): команда
        member (Member): участник
        expected (list[Member]): список участников
    """
    team.remove(member)
    assert team.get() == [arg.name for arg in expected]
