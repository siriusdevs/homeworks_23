"""Module for calculation company salaries statistics."""

company_departments = {
    'HR Department': {
        'John Smith': 50000,
        'Mary Johnson': 55000,
        'David Brown': 48000,
    },
    'Finance Department': {
        'Emily Davis': 60000,
        'Michael Wilson': 62000,
        'Sarah Lee': 55000,
    },
    'Marketing Department': {
        'Jennifer Clark': 58000,
        'Daniel Martinez': 54000,
        'Linda Hall': 56000,
    },
    'Engineering Department': {
        'Robert Taylor': 70000,
        'Susan Miller': 72000,
        'William White': 68000,
    },
    'Sales Department': {
        'Karen Harris': 30000,
        'Richard Jackson': 58000,
        'Patricia Anderson': 61000,
    },
}

ex_company_departments = ('Engineering Department', 'Sales Department')


def work_statistics(company_part: dict, ex_company_part: tuple = None) -> tuple:
    """Calculate the statistics of employees salaries in a company.

    Args:
        company_part (dict): all departments with its respective employee names as keys.
        ex_company_part (tuple): used to exclude certain departments. Defaults to None.

    Returns:
        tuple: top 3 of the lowest salaries of all departments and their percent of all salaries.
    """
    all_salaries = []

    for part, employees in company_part.items():
        if part not in ex_company_part:
            for salary in employees.values():
                all_salaries.append(salary)

    lowest_top = sorted(all_salaries)[:3]
    percent_of_lowest = round(sum(lowest_top) / sum(all_salaries) * 100, 2)

    return (lowest_top, percent_of_lowest)


work_statistics(company_departments, ex_company_departments)
