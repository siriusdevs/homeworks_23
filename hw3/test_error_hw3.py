"""Модуль тесты на ошибки hw3."""

import pytest

from member import Member
from project import Project
from task import Task
from team import Team

task1 = Task('Задание1', 'Описание задач', 'выполняется')
task2 = Task('задание2', 'описание задачи', 'завершена')
task3 = Task('задание3', 'описание Задачи', 'приостановлена')

project1 = Project('Проект1', [task1, task2])
project2 = Project('Проект2', [task1, task2, task3])

member1 = Member('Миша', 3, 3)
member2 = Member('Данил', 5, 6)
member3 = Member('Денис', 9, 8)

team1 = Team('команда1', [member1, member2])
team2 = Team('команда2', [member3, member2])

INVALID_TASK_DATA = (
    (
        15, 'text1', 'Завершена', TypeError,
    ),
    (
        'text2', 21, 'выполняется', TypeError,
    ),
    (
        'text3', 'text4', 33, TypeError,
    ),
    (
        'text5', 'text6', 'прыгает', ValueError,
    ),
)

INVALID_PROJECT_DATA = (
    (
        15, [task1, task2], TypeError,
    ),
    (
        'text7', (task1, task2), TypeError,
    ),
    (
        'text8', [task1, 'task2'], TypeError,
    ),
)

INVALID_ADD_PROJECT_DATA = (
    (
        project1, 31, TypeError,
    ),
    (
        project2, 'task2', TypeError,
    ),
)

INVALID_REMOVE_PROJECT_DATA = (
    (
        project1, 1, TypeError,
    ),
    (
        project2, 'task2', TypeError,
    ),
)

INVALID_MEMBER_DATA = (
    (
        25, 3, 5, TypeError,
    ),
    (
        'Саша', 4, '4', TypeError,
    ),
    (
        'саша', 4, 2, ValueError,
    ),
)

INVALID_TEAM_DATA = (
    (
        25, [member1, member2], TypeError,
    ),
    (
        'text9', (member1, member2), TypeError,
    ),
    (
        'text10', [member1, 'member2'], TypeError,
    ),
)

INVALID_ADD_TEAM_DATA = (
    (
        team1, 133, TypeError,
    ),
    (
        team2, 'member1', TypeError,
    ),
)

INVALID_REMOVE_TEAM_DATA = (
    (
        team1, 33, TypeError,
    ),
    (
        team2, 'member2', TypeError,
    ),
)


@pytest.mark.parametrize('name, description, status, error', INVALID_TASK_DATA)
def test_setter_task(name: str, description: str, status: str, error: Exception):
    """Тест сеттера задачи на ошибки.

    Args:
        name (str): название задачи
        description (str): описание
        status (str): статус
        error (Exception): ошибка
    """
    with pytest.raises(error):
        Task(name, description, status)


@pytest.mark.parametrize('name, list_task, error', INVALID_PROJECT_DATA)
def test_setter_project(name: str, list_task: list[Task], error: Exception):
    """Тест сеттера проетка на ошибки.

    Args:
        name (str): название проекта
        list_task (list[Task]): список задач
        error (Exception): ошибка
    """
    with pytest.raises(error):
        Project(name, list_task)


@pytest.mark.parametrize('project, task, error', INVALID_ADD_PROJECT_DATA)
def test_invalid_add_project(project: Project, task: Task, error: Exception):
    """Тест добавление задачи к проекту на ошибки.

    Args:
        project (Project): проект
        task (Task): задача
        error (Exception): ошибка
    """
    with pytest.raises(error):
        project.add(task)


@pytest.mark.parametrize('project, task, error', INVALID_REMOVE_PROJECT_DATA)
def test_invalid_remove_project(project: Project, task: Task, error: Exception):
    """Тест удаление задачи из проекта на ошибки.

    Args:
        project (Project): проект
        task (Task): задача
        error (Exception): ошибка
    """
    with pytest.raises(error):
        project.remove(task)


@pytest.mark.parametrize('name, max_count_tasks, max_count_projects, eror', INVALID_MEMBER_DATA)
def test_setter_member(name: str, max_count_tasks: int, max_count_projects, eror: Exception):
    """Тест сеттера участника на ошибки.

    Args:
        name (str): имя участника
        max_count_tasks (int): максимальное количетсво задач
        max_count_projects (_type_): максимальное количество проектов
        eror (Exception): ошибка
    """
    with pytest.raises(eror):
        Member(name, max_count_tasks, max_count_projects)


@pytest.mark.parametrize('name, list_member, error', INVALID_TEAM_DATA)
def test_setter_team(name: str, list_member: list[Member], error: Exception):
    """Тест сеттера команды на ошибки.

    Args:
        name (str): название команды
        list_member (list[Member]): список участников
        error (Exception): ошибка
    """
    with pytest.raises(error):
        Team(name, list_member)


@pytest.mark.parametrize('team, member, error', INVALID_ADD_TEAM_DATA)
def test_invalid_add_team(team: Team, member: Member, error: Exception):
    """Тест добавление участника к команде на ошибки.

    Args:
        team (Team): команда
        member (Member): участник
        error (Exception): ошибка
    """
    with pytest.raises(error):
        team.add(member)


@pytest.mark.parametrize('team, member, error', INVALID_REMOVE_TEAM_DATA)
def test_invalid_remove_team(team: Team, member: Member, error: Exception):
    """Тест удаление участника из команды на ошибки.

    Args:
        team (Team): команда
        member (Member): участник
        error (Exception): ошибка
    """
    with pytest.raises(error):
        team.remove(member)
