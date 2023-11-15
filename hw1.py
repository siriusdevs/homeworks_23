# --encoding: utf-8
"""Search for three maximum salaries for employees."""

from typing import List, Tuple


def check_sum_salary(
    *args: Tuple[str, List[float]],
    salary_cap: None | float = None,
        ) -> Tuple[List[float], float] | int:
    """Search three max salaries and return their.

    Parameters:
        args: Tuple[str, List[float]] - takes two arguments: name company and all salaries
        salary_cap: None | float - maximum salary

    Returns:
        Tuple[List[float], float] - top three salaries in company and percentage of salary
    """
    if salary_cap is not None and salary_cap < 0:
        salary_cap = 0

    list_all_salaries: List[float] = []
    list_three_max_salaries: List[float] = []

    for ind, argument in enumerate(args):
        if not isinstance(args[ind][0], str):
            raise TypeError('Неверный тип')

        list_all_salaries.extend(args[ind][1])

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

    result_sum = (sum(list_three_max_salaries) / sum(list_all_salaries))
    result_sum = round(result_sum * 100, 2)

    return (list_three_max_salaries, result_sum) if sum(list_all_salaries) > 0 else 0
