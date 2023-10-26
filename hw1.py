"""Module for calculating top-3 high and low paid departments."""


def top_departments(department: dict[str, dict], limit: float = None) -> dict:
    """
    Calculate the average salary of departments.

    Args:
        department: dict - data with departments, its employees and their salaries.
        limit: float - optional arg(default=None), above which salaries are not taken into account.

    Returns:
        dict: the first - 3 highly paid, the second - 3 low-paid departments.

    Raises:
        Exception: if not salaries are found below the entered limit.
    """
    new = {}
    for depts, employee in department.items():
        if limit:
            filt = {employee: salary for employee, salary in employee.items() if salary < limit}
            if not filt:
                raise Exception('Нет данных по введенному лимиту!')
            department[depts] = filt
            salary = filt.values()
        else:
            salary = employee.values()
        new[depts] = round(sum(salary) / len(salary), 2)
    high_paid_res = (sorted(new, key=new.get, reverse=True))[:3]
    low_paid_res = (sorted(new, key=new.get))[:3]
    return f'Топ высокооплачиваемых отделов: {high_paid_res}', \
        f'Топ низкооплачиваемых отделов: {low_paid_res}'
