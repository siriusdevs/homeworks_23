"""Homework about company's salary."""


def salary_info(
    *departaments: tuple[str, dict[str, float]],
    excluded: tuple[str] | None = None,
) -> tuple[list, float]:
    """Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        departaments: tuple[str, dict[str, float]] - departments, employees and their salaries.
        excluded: tuple[str] - excluded company.

    Returns:
        tuple[list, float] - top 3 salaries and the ratio for company.
    """
    list_of_values = []
    for departament in departaments:
        incident = excluded if excluded else []
        if departament[0] not in incident:
            list_of_values += departament[1].values()
    sum_of_all_salary = sum(list_of_values)
    our_salary = sorted(list_of_values)[:3]
    salary_percent = sum(our_salary) / (sum_of_all_salary or 1) * 100
    return [round(salary, 2) for salary in our_salary], round(salary_percent, 2)
