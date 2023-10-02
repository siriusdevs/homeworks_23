"""Homework about company's salary."""


def salary_info(
    *departments: tuple[str, dict[str, float]],
    excluded: tuple[str] | None = None,
) -> tuple[list, float]:
    """Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        departments: tuple[str, dict[str, float]] - departments, employees and their salaries.
        excluded: tuple[str] - excluded company.

    Returns:
        tuple[list, float] - top 3 salaries and the ratio for company.
    """
    salaries = []
    incident = excluded if excluded else []
    for department in departments:
        if department[0] not in incident:
            salaries += department[1].values()
    our_salary = sorted(salaries)[:3]
    salary_percent = sum(our_salary) / (sum(salaries) or 1) * 100
    return [round(salary, 2) for salary in our_salary], round(salary_percent, 2)
