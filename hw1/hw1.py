"""hw1.py."""


def calculate_salary(
    limit: float | None = None,
    **departments: dict[str, float],
) -> tuple[float, list[float]]:
    """
    Подсчитывает статистику по зарплатам в отделах.

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
    sum_salary = sum(all_salaries)
    if sum(all_salaries) > 0:
        percentage = round((sum_salary / sum_salary) * 100, 2)

        rounded_salaries = [round(salary, 2) for salary in top_salaries]

        return percentage, rounded_salaries
    elif sum(all_salaries) < 0:
        percentage = round((sum(top_salaries) / sum_salary) * 100, 2)

        rounded_salaries = [round(salary, 2) for salary in top_salaries]

        return percentage, rounded_salaries
    elif sum(all_salaries) == 0:
        return 0, [0, 0, 0]
    return ()


(
    calculate_salary(
        IT={'John': 0, 'Jane': 0, 'Bob': 0},
        Phone={'Alex': 0, 'Alice': 0},
    )
)