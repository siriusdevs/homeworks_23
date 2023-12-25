# --encoding: utf-8
"""Search for three maximum salaries for employees."""


def check_sum_salary(
    *departments: tuple[str, list[float]],
    salary_cap: None | float = None,
) -> tuple[list[float], float] | int:
    """Return three max salaries.

    Parameters:
        departments: Tuple[str, List[float]] - takes two arguments: name company and all salaries
        salary_cap: None | float - maximum salary

    Returns:
        Tuple[List[float], float] - top three salaries in company and percentage of salary

    Raises:
        TypeError: if not isinstance(departments[ind][0], str).
    """
    if salary_cap is None or salary_cap < 0:
        salary_cap = float('inf')

    list_all_salaries: list[float] = []

    for ind, _ in enumerate(departments):
        if not isinstance(departments[ind][0], str):
            raise TypeError('Не верное название компании, попробуй задать ')

        list_all_salaries.extend(departments[ind][1])

    list_all_salaries.sort(reverse=True)
    list_all_salaries = [
        round(salary, 2)
        for salary in list_all_salaries
        if 0 <= salary < salary_cap
    ]
    list_three_max_salaries = list_all_salaries[:3]

    sum_all_sal = sum(list_all_salaries)

    return (
        list_three_max_salaries,
        round((sum(list_three_max_salaries) / sum_all_sal)*100, 2),
        ) if sum_all_sal > 0 else 0
