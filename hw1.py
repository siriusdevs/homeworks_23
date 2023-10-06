"""Module for calculating salary stats."""


def get_salaries(*company: tuple, dept_except: tuple[str] = None) -> tuple[list, float]:
    """Count top 3 salaries and those part in all salaries.

    Args:
        company (tuple): salaries in departments.
        dept_except (tuple[str], optional): Excluded departments. Defaults to None.

    Returns:
        tuple[list, float]: top 3 salaries and part of those in '%'.
    """
    salaries = []

    for department in company:
        if dept_except is None or (department[0] not in dept_except):
            salaries += list(department[1].values())

    top_three = sorted(salaries, reverse=True)[:3]
    in_percentage = (sum(top_three) / sum(salaries)) * 100

    return [round(salary, 2) for salary in top_three], round(in_percentage, 2)
