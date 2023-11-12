# --encoding: utf-8
"""
Search for three maximum salaries for employees.
"""

from typing import Tuple, List


def check_sum_solary(*args: Tuple[str, List[float]], salary_cap: None or float = None) ->\
        Tuple[List[float], float] or int:
    """
    Function searches three max salaries and return their.
     if salary_cap is less than 0, then it will be equal to 0.
    Args:
        args: Tuple[str, List[float]] - takes two arguments: name company and all salaries
        salary_cap: Any - maximum salary
    Returns:
        Tuple[List[float], float] - top three salaries in company and percentage of salary
    """
    if salary_cap is not None and salary_cap < 0:
        salary_cap = 0
    list_all_salaries: List[float] = list()
    list_three_max_salaries: List[float] = list()

    for i in range(len(args)):
        list_all_salaries.extend(args[i][1])

    list_all_salaries.sort(reverse=True)

    list_all_salaries = [salary for salary in list_all_salaries if salary >= 0]

    if salary_cap is not None:
        for salary in list_all_salaries:

            if salary < salary_cap:
                list_three_max_salaries.append(salary)

            if len(list_three_max_salaries) == 3:
                list_all_salaries = list_all_salaries[-list_all_salaries.index(salary)-1:]
                break
    else:
        list_three_max_salaries.extend(list_all_salaries[:3])

    return (list_three_max_salaries,
            round((sum(list_three_max_salaries) / sum(list_all_salaries))*100, 2))\
        if sum(list_all_salaries) > 0 else 0
