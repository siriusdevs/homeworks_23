"""Provides types and functions for solving task_1.

Напишите функцию, которая принимает любые ключевые аргументы, но ожидает,
что название аргумента будет названием отдела компании (str),
а значение для аргумента - словарем, где имена сотрудников (str) служат в качестве ключей,
а зарплаты (float) - в качестве значений. Функция должна возвращать статистику: средняя,
максимальная и медианная зарплата в компании.
Функция также должна принимать опциональный аргумент,
который по умолчанию равен None. Этот аргумент - кортеж названий отделов,
которые нужно включить в статистику (их и только их).
Все числа в выводе функции округлять до второго знака после запятой.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class SalaryStats:
    """A dataclass for denoting basic salary statistics."""

    average: float = 0
    median: float = 0
    maximum: float = 0


# dictionary of employee names to their salaries
Salaries = dict[str, float]
# an optional list of unit names that correspond to unit names in Salaries
Units = Optional[tuple[str, ...]]


def get_salary_stats(units: Units = None, **salaries: Salaries) -> SalaryStats:
    """Compute salary statistics for a given company, optionally including only the specified units.

    Args:
        units: the only units to include in stats. If omitted, defaults to all units
        salaries: dictionary of unit names to Salaries

    Returns:
        Statistics for provided company's salaries.
        If units list (first argument) is provided, the result only includes these specified units.
    """
    unit_salaries = [
        list(unit.values()) for name, unit in salaries.items()
        if units is None or name in units
    ]
    salary_amounts = sum(unit_salaries, start=[])
    return SalaryStats(
        maximum=max(salary_amounts),
        average=round(_average(salary_amounts), 2),
        median=round(_median(salary_amounts), 2),
    ) if salary_amounts else SalaryStats()


def _average(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def _median(nums: list[float]) -> float:
    nums = sorted(nums)
    center = len(nums) // 2
    return (
        nums[center]
        if len(nums) % 2
        else _average(nums[center - 1:center + 1])
    )
