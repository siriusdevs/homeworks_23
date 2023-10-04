"""Module for calculating salary stats."""


def get_salaries(*company: tuple[str, dict], dept_except: tuple[str] = None) -> tuple[list, float]:
    """Count top 3 salaries and those part in all salaries.

    Args:
        *company (Tuple[str, dict]): salaries in departments
        dept_except (Tuple[str], optional): Excluded departments. Defaults to None.

    Returns:
        Tuple[list, float]: top 3 salaries and part of those in '%'
    """
    salaries = []

    for department in company:
        if dept_except is None or (department[0] not in dept_except):
            salaries += list(department[1].values())

    top_3 = sorted(salaries, reverse=True)[:3]
    in_percentage = (sum(top_3) / sum(salaries)) * 100

    return [round(salary, 2) for salary in top_3], round(in_percentage, 2)
