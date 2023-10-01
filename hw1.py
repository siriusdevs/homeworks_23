from typing import TypeAlias, Sequence, Optional


def get_median(items: Sequence[float | int]) -> float:
    """Calculate median in transmitted sequence.

    Args:
        items: Sequence of any int or float item.

    Returns:
        median value of items.
    """
    length = len(items)
    centre_index = (length - 1) // 2

    if length == 0:
        return 0.0

    if length % 2 == 1:
        return float(items[centre_index])

    return (items[centre_index] + items[centre_index + 1]) / 2


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

    result: CompaniesInfo = dict()

    for company_name, employees in companies.items():
        salary_sum = 0
        max_salary = 0
        filtered_salaries: list[float] = list()

        for salary in employees.values():
            if (min_salary is not None) and (salary < min_salary):
                continue

            salary_sum += salary
            max_salary = salary if max_salary < salary else max_salary
            filtered_salaries.append(salary)

        salaries_length = len(filtered_salaries)
        average = salary_sum / salaries_length if salaries_length > 0 else 0
        median = get_median(filtered_salaries)

        # it has a redundancy for mypy (static type checker)
        total = tuple(round(salary, 2) for salary in [average, max_salary, median])
        result[company_name] = (total[0], total[1], total[2])

    return result
