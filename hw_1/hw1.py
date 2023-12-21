"""Module with one function that analyses salaries."""
from statistics import median
from typing import Dict, Optional, Tuple


def company_salary_stats(
    exclude_departments: Optional[Tuple[str]] = None, 
    **departments: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate statistics of salaries in the company.

    Args:
    exclude_departments: Optional argument to exclude specific departments from the statistics.
    departments: Keyword arguments where department names are keys and values are dictionaries
                 with employee names (str) as keys and salaries (float) as values.

    Returns: 
    A dictionary containing the average, maximum, and median salaries in the company.
    All numbers are rounded to two decimal places.
    """
    all_salaries = []
    for department, employees in departments.items():
        if exclude_departments and department in exclude_departments:
            continue
        all_salaries.extend(employees.values())
    
    average_salary = round(sum(all_salaries) / len(all_salaries), 2) if all_salaries else 0
    max_salary = round(max(all_salaries), 2) if all_salaries else 0
    median_salary = round(median(all_salaries), 2) if all_salaries else 0

    return {
        "average_salary": average_salary,
        "max_salary": max_salary,
        "median_salary": median_salary
    }