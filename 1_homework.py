"""Calculate salary."""

from typing import Tuple


def get_top_salaries(*args: Tuple[str, list], departments: Tuple[str] = None) -> tuple:
    top_salaries = []
    if departments:
        args = list(filter(lambda arg: arg[0] in departments, args))
    required_salaries = [salaries[1] for salaries in args]
    for salaries in required_salaries:
        top_salaries.extend(salaries)
    top_salaries.sort(reverse=True)
    percent = sum(top_salaries[:3]) / sum(top_salaries) * 100
    return top_salaries[:3], round(percent, 2)
