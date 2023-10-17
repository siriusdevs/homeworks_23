"""Module, that has one function "best_wage", homework1."""


def best_wage(
    *departments: tuple[str, dict],
    exclude_deps: tuple[str, ...] = None,
) -> tuple[list[int | float], float]:
    """Find 3 best salaries and their percentage to total amount of payments.

    Args:
        exclude_deps: excluded department's names.
        departments: departments and dictionary of names and salaries.

    Returns:
        tuple: 3 best salaries and their percentage to total amount of payments.
    """
    permitted_wages = []
    exclude_deps = set(exclude_deps) if exclude_deps else ()
    for department, employee in departments:
        if department not in exclude_deps:
            permitted_wages += employee.values()

    if not permitted_wages:
        return [], 0

    total_payments = sum(permitted_wages)
    permitted_wages = sorted(permitted_wages)[:-4:-1]
    permitted_wages = [round(top, 2) for top in permitted_wages]
    percent_best_salary = round(sum(permitted_wages) / total_payments * 100, 2)
    return permitted_wages, percent_best_salary
