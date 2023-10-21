"""A module that includes the function of calculating salaries"""

SALARY_LIMIT = 20


def get_stats(*departments: tuple[str, dict[str, float]], limit: float = None) -> tuple[float, float, float]:
    """
    Get the statistics for salaries in a company.

    Args:
        departments: tuple[str, dict[str, float]] - Tuples,
        that include the names of company departments,
        dictionary of the surnames of employees and their salaries.
        limit: float - An optional parameter to filter out salaries below a certain limit.

    Returns:
        A tuple containing the maximum salary, average salary, and median salary.
    """
    all_salaries = []
    for department in departments:
        for _, salary in department[1].items():
            if limit is None or salary >= limit:
                all_salaries.append(salary)
    if not all_salaries:
        return {'average_salary': 0, 'max_salary': 0, 'median_salary': 0}
    average_salary = round(sum(all_salaries) / len(all_salaries), 2)
    max_salary = round(max(all_salaries), 2)
    if len(all_salaries) % 2 == 1:
        median_salary = round(sorted(all_salaries)[len(all_salaries) // 2], 2)
    else:
        lower_middle = sorted(all_salaries)[len(all_salaries) // 2 - 1]
        upper_middle = sorted(all_salaries)[len(all_salaries) // 2]
        median_salary = round((lower_middle + upper_middle) / 2, 2)
    return max_salary, average_salary, median_salary
