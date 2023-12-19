"""HW1."""
ROUND_TO = 2

Department = tuple[str, list[float]]
Stats = tuple[float, float, float]


def statistics(*departments: Department, department_names: tuple[str] = None) -> Stats:
    """Сalculates the average, maximum and median salary of employees.

    Args:
        departments: all departments
        department_names: names of departments that need to be included in the statistics

    Raises:
        ValueError: if entered an empty salary or all salaries is zero

    Returns:
        statistics of average, maximum and median salaries
    """
    all_salaries = []
    for name, salaries in departments:
        if department_names is None or name in department_names:
            all_salaries += salaries
    all_salaries.sort()

    if not all_salaries:
        raise ValueError('You entered an empty salary')
    if sum(all_salaries) == 0:
        raise ValueError('Salaries should not be 0')

    max_salary = max(all_salaries)
    average_salary = sum(all_salaries) / len(all_salaries)

    if len(all_salaries) % 2 == 0:
        median_index = len(all_salaries) // 2
        median_salary = (all_salaries[median_index - 1] + all_salaries[median_index]) / 2
    else:
        median_index = len(all_salaries) // 2
        median_salary = all_salaries[median_index]
    return (
        round(average_salary, ROUND_TO),
        round(max_salary, ROUND_TO),
        round(median_salary, ROUND_TO),
    )
