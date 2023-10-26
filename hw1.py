"""A module that includes the function of calculating salaries."""


def get_stats(
    *departments: tuple[str, dict[str, float]],
    limit: float = None,
) -> tuple[float, float, float]:
    """Get the statistics for salaries in a company.

    Args:
        departments:
            tuple[str, dict[str, float]] - Tuples,
            that include the names of company departments,
            dictionary of the surnames of employees and their salaries.
        limit:
            float - An optional parameter to filter out salaries below a certain limit.

    Returns:
        A tuple containing the maximum salary, average salary, and median salary.
    """
    all_sls = []
    for _, employees in departments:
        for salary in employees.values():
            if limit is None or salary >= limit:
                all_sls.append(salary)
    if not all_sls:
        return (0, 0, 0)
    count_salaries = len(all_sls)
    average_salary = round(sum(all_sls) / count_salaries, 2)
    max_salary = round(max(all_sls), 2)
    if count_salaries % 2 == 1:
        median_salary = round(sorted(all_sls)[count_salaries // 2], 2)
    else:
        median_elements = sorted(all_sls)[count_salaries // 2 - 1]
        median_elements += sorted(all_sls)[count_salaries // 2]
        median_salary = round(median_elements / 2, 2)
    return max_salary, average_salary, median_salary
