"""Module for calculating the salary stats."""


def calculate_salary_stats(salary_limit: float = None, **kwargs: dict) -> tuple:
    """Сreates salary statistics in the company.

    Args:
        salary_limit(float): limit below which salary is not taken into account
        kwargs: the function expects arg name - departament name, value - employees

    Returns:
        tuple: (top 3 salaries, ratio of top salaries to total salary)

    """
    all_salaries = []

    for salaries in kwargs.values():
        for salary in salaries.values():
            if salary_limit is not None:
                if salary > salary_limit:
                    all_salaries.append(salary)
            else:
                all_salaries.append(salary)

    top_salaries = sorted(all_salaries, reverse=True)[:3]

    ratio = round(sum(top_salaries) / (sum(all_salaries)) * 100, 2)

    return (top_salaries, ratio)
