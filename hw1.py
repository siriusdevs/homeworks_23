"""Module for solving task_1: functions and datatypes for salary statistics.

Task_1:
Напишите функцию, которая принимает любое количество позиционных аргументов,
где каждый аргумент - это кортеж формата
(название отдела компании (str),
{словарь фамилий сотрудников этого отдела (str) и их зарплат (float)}).

Функция должна возвращать статистику:
топ 3 зарплат в компании списком,
отношение суммы этого топа ко всему размеру выплат в компании, в процентах.

Функция также должна принимать опциональный аргумент, который по умолчанию равен None.
Этот аргумент - кортеж названий отделов, которые нужно включить в статистику (их и только их).
Все числа в выводе функции округлять до второго знака после запятой.
"""
from dataclasses import dataclass, field
from typing import Optional


class AbsenceError(Exception):
    """Exception raised when something missed."""


@dataclass
class SalaryStats:
    """Data class for some salary statistics.

    Args:
        top_salaries: top-X the highest salaries
        top_salaries_percent: percentage of top salaies amount from all salaries amount
    """

    # mutable default [] is not allowed, use field with default_factory
    top_salaries: list[float, ...] = field(default_factory=list)
    top_salaries_percent: float = 0


ROUND_UP_TO = 2
# number of salaries in the top
TOP_X = 3

# abbreviations of annotations (Deps = Departments)
# department in format (department name, {employee last name: salary, ...})
Deps = tuple[str, dict[str, float]]
# departments, that only used in statictics calculations
UsedDeps = Optional[tuple[str, ...]]
Salaries = list[float, ...]


def get_salary_stats(*deps: Deps, used_deps: UsedDeps = None) -> SalaryStats:
    """Get statistics for salaries in specified departments.

    Args:
        deps: list[Deps] - all departments
        used_deps: departments, that only used in statictics calculations.\
                If not specified, defaults to all deps.

    Returns:
        salaries statistics in SalaryStats format
    """
    # get list of all salaries
    all_salaries = []
    # convert tuple to set for speed boost
    used_deps_set = set(used_deps) if used_deps is not None else None
    for dep_name, dep_salaries in deps:
        # if current department name is used in calculations
        if used_deps_set is None or dep_name in used_deps_set:
            # dep_salaries is dict in format {employee last name: salary, ...}
            all_salaries += dep_salaries.values()

    top_salaries = _get_top(all_salaries, TOP_X)
    percents = _get_percents(top_salaries, all_salaries)

    return SalaryStats(
        top_salaries=[round(el, ROUND_UP_TO) for el in top_salaries],
        top_salaries_percent=round(percents, ROUND_UP_TO),
    )


def _get_top(all_salaries: Salaries, top_x: int) -> Salaries:
    # sort salaries in ascending order
    sorted_salaries = sorted(all_salaries, reverse=True)
    # return top-X the highest salaries
    return sorted_salaries[:top_x]


def _get_percents(top_salaries: Salaries, all_salaries: Salaries) -> float:
    if not all_salaries:
        raise AbsenceError('No one salary was found.')
    if sum(all_salaries) == 0:
        raise ValueError('All salaries are 0.')
    return sum(top_salaries) / sum(all_salaries) * 100
