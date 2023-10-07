"""Module, that has one function "best_wage", homework1."""


def best_wage(departments: list, exclude_depart: tuple = None) -> list[float | str]:
    """Find 3 best salaries and their percentage to total amount of payments.

    Args:
        exclude_depart: Tuple[str] - tuple of excluded department's names.
        departments: List[tuple] - tuple of departments and dictionary of names and salaries.

    Returns:
        list[float | str]: 3 best salaries and their percentage to total amount of payments.
    """
    total_payments = []
    permitted_salaries = []

    for dep in departments:
        for _, salary in dep[1].items():
            total_payments += [salary]
            if exclude_depart is None or dep[0] not in exclude_depart:
                permitted_salaries += [salary]

    permitted_salaries = sorted(permitted_salaries, reverse=True)
    num_top = 3
    best_salaries = []

    best_salaries += [round(permitted_salaries[top], 2) for top in range(num_top)]
    percent_best_salary = round(sum(best_salaries) / sum(total_payments) * 100, 2)
    best_salaries += [f'{percent_best_salary}%']

    return best_salaries
