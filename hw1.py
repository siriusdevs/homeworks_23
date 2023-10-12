"""Module for calculating the salary stats."""


def calculate_salary(
    salary_limit: float = None,
    **departaments: dict[str, dict],
) -> tuple[list, float]:
    """Сreates salary statistics in the company.

    Args:
        salary_limit(float): limit below which salary is not taken into account
        departaments: the function expects arg name - departament name, value - employees

    Returns:
        tuple: (top 3 salaries, ratio of top salaries to total salary)

    """
    all_salaries = []

    for employees in departaments.values():
        for salary in employees.values():
            if salary_limit is None or salary > salary_limit:
                all_salaries.append(salary)

    top_salaries = sorted(all_salaries, reverse=True)[:3]

    sum_salaries = sum(all_salaries)

    if sum_salaries == 0:
        ratio = 0
    else:
        ratio = round(sum(top_salaries) / (sum(all_salaries)) * 100, 2)

    return top_salaries, ratio
