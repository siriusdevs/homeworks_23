"""Salary stats and percents."""


def top_salary(
    *company: tuple[str, list[float]],
    name_departments: list[str] = None,
) -> tuple[list[float], float]:
    """Find top-3 salaries in the company and the ratio of their sum to the total amount of payments.

    Args:
        company: Tuple[str, list[float]] - company departments and their salaries.
        name_departments: list[str] - the names of departments to consider.

    Returns:
        tuple[list[float], float] - top 3 salaries and the ratio
        of their sum to the total amount of payments.
    """
    all_salaries = []

    for department_name, salaries in company:
        if name_departments is None or department_name in name_departments:
            all_salaries.extend([round(salary, 2) for salary in salaries])


    if sum(all_salaries) == 0:
        return [], 0

    top_salaries = sorted(all_salaries, reverse=True)[:3]

    percentage = round(sum(top_salaries) / sum(all_salaries) * 100, 2)

    return top_salaries, percentage
