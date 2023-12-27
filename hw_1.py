"""Modul for calculation salary statistic"""


def get_salaries(
    *departments: tuple[str, dict[str, float]],
    dept_exp: tuple[str] = None
) -> tuple[list, float]:
    """Calculate the statistic of emploee salaries.

    Args:
        departments (tuple[str, dict[str, float]]):
            All departments with its respective employee names as keys.
        dept_exp (tuple[str], optional): Excluded departments. Defaults to None.

    Returns:
        tuple[list, float]: Top 3 salaries of all departmets and their part of all salaries.
    """
    all_salaries = []
    for department in departments:
        if dept_exp is None or department[0] not in dept_exp:
            all_salaries += list(department[1].values())
    sum_salaries = sum(all_salaries)
    top_3 = sorted(all_salaries, reverse=True)[:3]
    percent_of_top = 0 if sum_salaries == 0 else round(sum(top_3) / sum_salaries, 2)

    return top_3, percent_of_top
