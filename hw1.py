'''Salary stats and percent's'''


def top_salary(*company: tuple[str, list[float]],
               name_departments: [list[str]] = None) -> tuple[list[float], float]:
    """
    Find top 3 salaries in the company, the ratio of the amount of this top to the total amount of
    payments in the company in percentages.

    Args:
        *company: Tuple[str, List[float]] - company departments and their salaries.
        name_departments: List[str] - the name departaments. Usually Optional[List[str]] = None.

    Returns:
        tuple[list[float], float] - top 3 salaries and the ratio  of the amount
        of this top to the total amount of payments.
    """
    all_salaries = []
    for department_name, salaries in company:
        if name_departments is None or department_name in name_departments:
            all_salaries.extend(salaries)

    if not all_salaries or sum(all_salaries) == 0:
        return [], 0.0

    top_salaries = sorted(all_salaries, reverse=True)[:3]

    percentage = round(sum(top_salaries) / sum(all_salaries) * 100, 2)

    return top_salaries, percentage
