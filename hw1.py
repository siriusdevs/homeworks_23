"""Module for calculating the lowest 3 salaries and their part of all payments."""


def lowest_salaries(*args, salary_limit: float = None) -> tuple:
    """Calculate lowest salaries and their ratio to all payments.

    Args:
        args: tuple of tuples with company department name, \
            and dictionary of surnames of employees and their salaries.
        salary_limit: numerical limit above which salaries should not be taken.

    Returns:
        tuple: contains list of all employee salaries and \
            the percentage of three lowest salaries from all payments.

    """
    if salary_limit == 0:
        return (0, 0, 0, 0)
    total_payments = 0
    salaries = []
    for department in args:
        staff = department[1]
        for _, salary in staff.items():
            total_payments += salary
            if salary_limit is None:
                salaries.append(salary)
            elif salary < salary_limit:
                salaries.append(salary)

    salaries = sorted(salaries)[:3]
    ratio_lowest = sum(sorted(salaries)[:3]) / total_payments
    return (*salaries, round(ratio_lowest, 2))
