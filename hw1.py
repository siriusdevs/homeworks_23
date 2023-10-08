"""Module, that has one function "best_wage", homework1."""


def best_wage(departments: list, exclude_deps: tuple = None) -> list[float | int, str]:
    """Find 3 best salaries and their percentage to total amount of payments.

    Args:
        exclude_deps: Tuple[str] - tuple of excluded department's names.
        departments: List[tuple] - tuple of departments and dictionary of names and salaries.

    Returns:
        list[float | str]: 3 best salaries and their percentage to total amount of payments.
    """
    quantity_deps = len(departments)
    if quantity_deps == 0:
        return ['Недостаточно данных для использования функции']
    total_payments = []
    permitted_wages = []

    for dep in departments:
        for _, salary in dep[1].items():
            total_payments += [salary]
            if exclude_deps is None or dep[0] not in exclude_deps:
                permitted_wages += [salary]

    permitted_wages = sorted(permitted_wages, reverse=True)
    possible_len = len(permitted_wages)

    if possible_len >= 3:
        permitted_wages = [round(permitted_wages[top], 2) for top in range(3)]
    else:
        return ['Недостаточно не исключенных отделов для использования функции']

    percent_best_salary = round(sum(permitted_wages) / sum(total_payments) * 100, 2)
    permitted_wages += [f'{percent_best_salary}%']

    return permitted_wages
