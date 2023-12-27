"""Function for calculate statistic."""


def salary_departments(
    required_departments: tuple[str] = None,
    **department_name: dict[str, float],
) -> tuple[list, float]:
    """Display the top 3 salaries in the company and the percentage of this top to all salaries.

    Args:
        required_departments (tuple[str]): tuple of department names(str)
            to be included in statistics. Default is None.
        department_name (dict[str, float]): dictionary where
            the names of the department employees are keys (str),
            and salaries are the value (float).

    Returns:
        Tuple[list, float]: statistics the top 3 salaries in the company
            and the percentage of this top to all salaries.

    Raises:
        ValueError: if list of the salary is empty.
    """
    list_salary = []

    for department, employee in department_name.items():
        if required_departments is None or department in required_departments:
            for salary in employee.values():
                list_salary.append(salary)
    list_salary.sort(reverse=True)
    if not list_salary:
        raise ValueError('List salary cannot be a empty')
    top_salaries = list_salary[:3]
    total_salaries = round(sum(top_salaries) / sum(list_salary), 2) * 100
    return top_salaries, total_salaries
