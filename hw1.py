# --encoding: utf-8
"""Search for three maximum salaries for employees."""


def three_max_selaries(
    list_salary: list[float],
    cap_salary: float,
) -> tuple[list[float], list[float]]:
    """Search three max salaries and all salaries are less than cap_salary.

    Parameters:
        list_salary: list[float] - all salaries
        cap_salary: None | float - maximum salary

    Returns:
        tuple[list[float], list[float]] - top three salaries and all salaries less than cap_salary
    """
    list_max_salaries: list[float] = []

    for salary in list_salary:
        if salary < cap_salary:
            list_max_salaries.append(salary)
        if len(list_max_salaries) == 3:
            list_salary = list_salary[-list_salary.index(salary)-1:]
            break

    return list_max_salaries, list_salary


def check_sum_salary(
    *departments: tuple[str, list[float]],
    salary_cap: None | float = None,
) -> tuple[list[float], float] | int:
    """Return three max salaries.

    Parameters:
        departments:tuple[str, list[float]] - takes two arguments: name company and all salaries
        salary_cap: None | float - maximum salary

    Returns:
        tuple[list[float], float] - top three salaries in company and percentage of salary

    Raises:
        TypeError: if not isinstance(departments[ind][0], str).
    """
    if salary_cap is not None and salary_cap < 0:
        salary_cap = 0

    list_all_salaries: List[float] = []

    for ind, _ in enumerate(departments):
        if not isinstance(departments[ind][0], str):
            raise TypeError('Не верное название компании, попробуй задать ')

        list_all_salaries.extend(departments[ind][1])

    list_all_salaries.sort(reverse=True)
    list_all_salaries = [salary for salary in list_all_salaries if salary >= 0]

    if salary_cap is not None:
        list_three_max_salaries, list_all_salaries = three_max_selaries(
            list_all_salaries,
            salary_cap,
                )
    else:
        list_three_max_salaries = list_all_salaries[:3]

    sum_all_sal = sum(list_all_salaries)

    return (
        list_three_max_salaries,
        round((sum(list_three_max_salaries) / sum_all_sal)*100, 2),
        ) if sum_all_sal > 0 else 0
