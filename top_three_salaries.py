"""Function for calculating the top 3 salaries and its percentage of all salaries."""

from typing import List, Tuple


def calculate_salary(*departments: Tuple[str, List[float]], lim: float = None):
    """Calculate the top 3 salaries and its percentage of all salaries.

    Args:
        departments: Tuple[str, List[float]] department name and list of salaries.
        lim: float numerical limit which default is None.

    Returns:
        tuple: top 3 salaries.
        float: percentage of top 3 salaries to all salaries.

    """
    salaries = []

    for department in departments:
        _, department_salaries = department

        for salary in department_salaries:
            if lim is not None:
                if salary <= lim:
                    salaries.append(round(salary, 2))
            else:
                salaries.append(round(salary, 2))

    salaries.sort(reverse=True)
    total_top_salary = sum(salaries[:3])
    total_salary_payments = sum(salaries)

    if total_salary_payments == 0:
        return [], 0

    total_salaries_percentage = (total_top_salary / total_salary_payments) * 100

    return (salaries[:3], round(total_salaries_percentage, 2))
