"""Provides types and functions for solving task_1.

Напишите функцию, которая принимает любые ключевые аргументы, но ожидает,
что название аргумента будет названием отдела компании (str),
а значение для аргумента - словарем, где имена сотрудников (str) служат в качестве ключей,
а зарплаты (float) - в качестве значений. Функция должна возвращать статистику: средняя,
максимальная и медианная зарплата в компании.
Функция также должна принимать опциональный аргумент,
который по умолчанию равен None. Этот аргумент - кортеж названий отделов,
которые нужно включить в статистику (их и только их). В
се числа в выводе функции округлять до второго знака после запятой.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class SalaryStats:
    """A dataclass for denoting basic salary statistics."""

    average: float = 0
    median: float = 0
    maximum: float = 0


def get_salary_stats(units: Optional[tuple[str]] = None, **kwargs) -> SalaryStats:
    """Compute salary statistics for a given company, optionally including only the specified units.

    Args:
        units: the only units to include in stats. If omitted, defaults to all units
        kwargs: dictionary of unit names to dictionaries of employee names to their salaries

    Returns:
        Statistics for provided company's salaries.
        If units list (first argument) is specified, the result only includes these units.
    """
    return SalaryStats()
