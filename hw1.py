"""Module for calculating the salary stats"""


def calculate_salary_stats(salary_limit: float = None, **kwargs: dict) -> dict[str, tuple]:
    """Сreates salary statistics in the company.

    Args:
        salary_limit(float): limit below which salary is not taken into account
        kwargs: the function expects arg name - departament name, value - employees

    Returns:
        dict: Dictionary in which the key is the name of the company, and the value is statistics

    """
    statistics = dict()
    for departament_name, employees in kwargs.items():
        employees_salaries = employees.values()
        if salary_limit is not None:
            employees_salaries = [salary for salary in employees_salaries if salary > salary_limit]
        all_salary = sum(employees_salaries)
        top_salaries = sorted(employees_salaries)[-3:][::-1]
        all_top_salary = sum(top_salaries)
        all_to_top_salary = round(((all_top_salary / all_salary) * 100), 2)
        statistics[departament_name] = (top_salaries, all_to_top_salary)
    return statistics
