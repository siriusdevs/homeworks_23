"""Module for calculating the top 3 salaries and the ratio."""


def salary_count(
    *args: tuple[str, dict[str, float]],
    excluded_departments: tuple[str] | None,
) -> tuple[list, float]:
    """Calculate the top 3 salaries and the ratio in percents.

    Parameters:
        args: tuple[str, dict[str, float]] - company departments, employees and their salaries.
        excluded_departments: tuple[str] or None is default.

    Returns:
        tuple[list, float] - top 3 salary and the ratio.
    """
    # Create a dictionary to store information about salaries in each department
    department_salaries = {}

    for department, salary in args:
        if excluded_departments is None or department not in excluded_departments:
            department_salaries[department] = salary

    all_salaries = []
    for salaries in department_salaries.values():
        all_salaries.extend(salaries.values())
    # Sort salaries in descending order
    sorted_salaries = sorted(all_salaries, reverse=True)[:3]
    # We calculate the ratio of the sum of the last three salaries to the total amount
    ratio = round((sum(sorted_salaries) / sum(all_salaries)) * 100, 2)

    return list(sorted_salaries), ratio
