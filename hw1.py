"""Thus module include function statistic_salary."""


from typing import Optional


def statistic_salary(*args, limit: Optional[int] = None) -> tuple:
    """Fucntion take position argument and optional argument.

    Args:
        args: position argument, whose take tuple of format (str, dict)
        limit: a numercal limit above which salaries need not be taken

    Returns:
        A tuple with average, max and median salary.
    """
    salary = []
    if not args[0]:
        return (0, 0, 0)
    for data_salary in args:
        for salaries in data_salary[1].values():
            if limit is None or limit >= salaries:
                salary.append(salaries)
    salary = sorted(salary)
    stat_salary = []
    len_salary = len(salary)
    stat_salary.append(round(sum(salary) / len_salary, 2))
    stat_salary.append(round(max(salary), 2))
    if len_salary % 2 == 1:
        stat_salary.append(round(salary[len_salary // 2], 2))
    else:
        stat_salary.append(round(
            (round(salary[(len_salary // 2)-1], 2)
             + round(salary[len_salary // 2], 2)
             ) // 2, 2,
             ))

    return tuple(stat_salary)
