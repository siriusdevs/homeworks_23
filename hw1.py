"""Salary analysis."""


def get_best_salaries(ignored_depts: tuple = None, **dept_employees) -> tuple:
    """Calculate employee salary statistics.

    Args:
        ignored_depts (tuple): contain dept names ignored when calculating statistics.
        dept_employees: the key is the name of the department, the value is a dictionary.

    Returns:
        tuple: the first element is a list of 3 salaries,
        and the second element is a float number.
    """
    employees = []
    salaries_sum = 0

    for dept, employees_salaries in dept_employees.items():
        if ignored_depts is None or dept not in set(ignored_depts):
            for salary in employees_salaries.values():
                employees.append(round(salary, 2))
                salaries_sum += employees[-1]

    if not employees:
        return [], 0

    best_salaried_employees = sorted(employees, reverse=True)[:3]
    best_salaries_sum = sum(best_salaried_employees)

    percent = round((best_salaries_sum / salaries_sum) * 100, 2)

    return best_salaried_employees, percent
