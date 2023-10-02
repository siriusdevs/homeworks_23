"""Module for calculation company salaries statistics."""


def work_statistics(company_part: dict, ex_company_part: tuple = None) -> tuple:
    """Calculate the statistics of employees salaries in a company.

    Args:
        company_part (dict): all departments with its respective employee names as keys.
        ex_company_part (tuple): used to exclude certain departments, defaults to None.

    Returns:
        tuple: top 3 of the lowest salaries of all departments and their percent of all salaries.
    """
    all_salaries = []

    for part, employees in company_part.items():
        if part not in ex_company_part:
            for salary in employees.values():
                all_salaries.append(salary)

    lowest_top = sorted(all_salaries)[:3]

    percent_of_lowest = 0
    if sum(all_salaries) != 0:
        percent_of_lowest = round(sum(lowest_top) / sum(all_salaries) * 100, 2)

    return lowest_top, percent_of_lowest
