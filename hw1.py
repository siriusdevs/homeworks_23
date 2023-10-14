"""Module that analyses salaries."""


def get_salary_statistics(
    minimal_salary: int | float = None,
    **departments: dict[str, dict[str, float]],
) -> tuple[float, float, float]:
    """Calculate statistics on employee salaries.

    Args:
        minimal_salary: int|float - minimal salary which is used in statistics,
        departments: dict - key is department, value is dict - str is name, float is salary.

    Returns:
        tuple: the average, maximum and median salary
        among all of the departments.
    """
    average = 0
    maximum = 0
    median = 0
    salary_list = []

    for department in departments.values():
        for salary in department.values():
            if minimal_salary is None or salary >= minimal_salary:
                salary_list.append(salary)
    salary_list = sorted(salary_list)

    length = len(salary_list)
    half_length = length // 2
    if salary_list:
        average = sum(salary_list) / length
        maximum = max(salary_list)
        if length % 2:
            median = salary_list[half_length]
        else:
            median = (salary_list[half_length - 1] + salary_list[half_length]) / 2

    return tuple(round(stat, 2) for stat in (average, maximum, median))
