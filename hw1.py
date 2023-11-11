"""Thus module include function statistic_salary."""


from typing import Optional


def statistic_salary(
    *departments: tuple[str, dict[str, float]],
    limit: Optional[int] = None,
) -> tuple[float, float, float]:
    """Fucntion take position argument and optional argument.

    Args:
        departments: position argument, whose take tuple of format (str, dict)
        limit: a numercal limit above which salaries need not be taken

    Returns:
        A tuple with average, max and median salary.
    """
    salaries = []
    if not departments:
        return (0, 0, 0)
    for _, employees in departments:
        for salary in employees.values():
            if limit is None or limit >= salary:
                salaries.append(salary)
    salaries = sorted(salaries)
    stat_salary = []
    len_salaries = len(salaries)
    stat_salary.append(round(sum(salaries) / len_salaries, 2))
    stat_salary.append(round(max(salaries), 2))
    if len_salaries == 0:
        return 0, 0, 0
    if len_salaries % 2 == 1:
        stat_salary.append(round(salaries[len_salaries // 2], 2))
    else:
        middle_index = round(salaries[(len_salaries // 2) - 1], 2)
        scnd_middle_index = round(salaries[len_salaries // 2], 2)
        median_salary = round((middle_index + scnd_middle_index) // 2, 2)
        stat_salary.append(median_salary)

    return tuple(stat_salary)
