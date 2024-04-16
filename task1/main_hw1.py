"""This is module for salary statistic calculation."""


from typing import Optional


def salary_calculation_statistic(
    *arguments: tuple[str, list[float]],
    limit: Optional[float] = None,
) -> tuple[float, float, float]:
    """Salary statistic calculation function.

    Args:
        arguments (tuple[str, list[float]]): giving arguments.
        limit (Optional[float], optional): limit. Defaults to None.

    Returns:
        tuple[float, float, float]: tuple of salary.
    """
    salaries = []

    for _, employees in arguments:
        for salary in employees:
            if limit is None or limit >= salary:
                salaries.append(salary)

    len_salaries = len(salaries)

    if len_salaries == 0:
        return 0, 0, 0

    salaries = sorted(salaries)
    stat_salary = []
    stat_salary.append(round(sum(salaries) / len_salaries, 2))
    stat_salary.append(round(max(salaries), 2))

    if len_salaries % 2 == 1:
        stat_salary.append(round(salaries[len_salaries // 2], 2))

    else:
        middle_index = round(salaries[(len_salaries // 2) - 1], 2)
        scnd_middle_index = round(salaries[len_salaries // 2], 2)
        median_salary = round((middle_index + scnd_middle_index) // 2, 2)
        stat_salary.append(median_salary)

    return tuple(stat_salary)
