"""Module for calculating average, max, median salary for employees."""
from typing import Optional, Sequence, TypeAlias


def get_median(sequence: Sequence[float | int]) -> float | int:
    """Calculate median in transmitted sequence.

    Args:
        sequence: Sequence of any int or float item.

    Returns:
        median value of items.
    """
    length = len(sequence)
    centre_index = (length - 1) // 2

    if length == 0:
        return 0

    if length % 2 == 1:
        return float(sequence[centre_index])

    return (sequence[centre_index] + sequence[centre_index + 1]) / 2


Employees: TypeAlias = dict[str, float]  # name, salary

CompanyInfo: TypeAlias = tuple[float, float, float]  # average, maximum and median salary
CompaniesInfo: TypeAlias = dict[str, CompanyInfo]  # company name, company statistic


def calculate_companies_info(min_salary: Optional[int | float] = None, **companies: Employees) \
        -> CompaniesInfo:
    """Calculate average, maximum and medium salary for each company.

    Args:
        min_salary: The lower limit of salaries that we consider, default - None.
        companies: \
            Companies that we consider salaries in, \
            They have to be given through keyword params.

    Returns:
        Calculated average, maximum and medium salary in each company,
        result is a tuple with three float value.
    """
    salaries_in_companies: CompaniesInfo = {}

    for company_name, employees in companies.items():
        salary_sum: float = 0
        max_salary: float = 0
        filtered_salaries: list[float] = []

        for salary in employees.values():
            if (min_salary is not None) and (salary < min_salary):
                continue

            salary_sum += salary
            max_salary = salary if max_salary < salary else max_salary
            filtered_salaries.append(salary)

        salaries_length = len(filtered_salaries)
        average_salary = (salary_sum / salaries_length) if (salaries_length > 0) else 0

        total = tuple(round(info_salary, 2) for info_salary in (
            average_salary,
            max_salary,
            get_median(filtered_salaries),
        ))

        # for mypy
        if len(total) != 3:
            continue

        salaries_in_companies[company_name] = total

    return salaries_in_companies
