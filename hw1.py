"""Module for calculating the top 3 salaries and the ratio."""


def salary_count(
    *company: tuple[str, dict[str, float]],
    excluded_departments: tuple[str] | None,
) -> tuple[list, float]:
    """Calculate the top 3 salaries and the ratio in percents.

    Parameters:
        company: tuple[str, dict[str, float]] - company departments, employees and their salaries.
        excluded_departments: tuple[str] or None is default.

    Returns:
        tuple[list, float] - top 3 salary and the ratio.
    """
    # Create a dictionary to store information about salaries in each department
    all_salaries = []
    excluded_departments = set(excluded_departments) if excluded_departments else set()
    for department, salary in company:
        if excluded_departments is None or department not in excluded_departments:
            all_salaries += salary.values()
    # Sort salaries in descending order
    sorted_salaries = sorted(all_salaries, reverse=True)[:3]
    sum_total = sum(all_salaries)
    # We calculate the ratio of the sum of the last three salaries to the total amount
    if sum_total > 0:
        ratio = round(sum(sorted_salaries) / sum_total * 100, 2)
    else:
        ratio = 0
    return list(sorted_salaries), ratio
