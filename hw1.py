from typing import Tuple


def get_salaries(*agrs: Tuple[str, dict], dep_except: Tuple[str] = None) -> Tuple[list, float]:
    """Function for count top 3 salaries and those part in all salaries

    Args:
        *args (Tuple[str, dict]): salaries in departments
        dep_except (Tuple[str], optional): Excluded departments. Defaults to None.

    Returns:
        Tuple[list, float]: top 3 salaries and part of those in '%'
    """
    top_salary = []
    all_salaries = 0
    dep_except = '' if dep_except is None else dep_except

    for dep in agrs:
        if not(dep[0] in dep_except):
            top_salary += list(dep[1].values())
            all_salaries += sum(dep[1].values())

    top_3 = sorted(top_salary, reverse=True)[:3]
    in_percentage = (sum(top_3) / all_salaries) * 100

    return [round(i, 2) for i in top_3], round(in_percentage, 2)
