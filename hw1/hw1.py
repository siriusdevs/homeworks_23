"""hw1.py."""


def calculate_salary(
    limit: float | None = None,
    **departments: dict[str, float],
) -> tuple[float, list[float]]:
    """
    Calculate the percentage of the top 3 salaries
    compared to the total sum of all salaries.

    Args:
        departments: keyword arguments, where values containing employees names and salaries.
        limit: Salary limit to consider. Defaults to None.

    Returns:
        tuple: Percentage of the top 3 salaries and
            a list of rounded top 3 salaries.
    """
    all_salaries = []
    for _, salaries in departments.items():
        all_salaries.extend(salaries.values())

    if limit is not None:
        all_salaries = [salary for salary in all_salaries if salary >= limit]

    all_salaries.sort()

    top_salaries = all_salaries[:3]

    if sum(all_salaries) == 0:
        return ()

    percentage = round((sum(top_salaries) / sum(all_salaries)) * 100, 2)

    rounded_salaries = [round(salary, 2) for salary in top_salaries]

    return percentage, rounded_salaries


(
    calculate_salary(
        IT={'John': 5000.0, 'Jane': 5000.0, 'Bob': 5000.0},
        Phone={'Alex': 2500.66, 'Alice': 2512.1428},
    )
)
