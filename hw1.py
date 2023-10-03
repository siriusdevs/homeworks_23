"""This is the main code for first homework."""
from typing import Tuple


def get_salary_stats(data_salaries: dict, department: str, limit: int = None) -> Tuple:
    """Block of code that is designed to search for top 3 salaries in chosen department and etc.

    Args:
        data_salaries: dictionary of dictionaries that includes departments and salaries data.
        department: string that tells us which department we are looking for.
        limit: default is None, sets up limit for salary, everything above is ignored.

    Returns:
        Tuple: tuple with top 3 salaries and ratio of this 3 salaries to all of them in department.

    """
    data_raw = data_salaries[department]
    salaries_list = data_raw.values()
    sum_salaries = sum(salaries_list)
    if limit is not None:
        salaries_list = [elem for elem in salaries_list if elem <= limit]
    salaries = []
    for elem in salaries_list:
        salaries.append(elem)
    for salary in salaries:
        salaries.remove(salary)
        salary = round(salary, 2)
        salaries.append(salary)
    salaries = sorted(salaries, reverse=True)
    top3salariessum = sum(salaries[:3])
    ratio = round(top3salariessum / sum_salaries * 100, 2)
    return (tuple(salaries[:3])), ratio
