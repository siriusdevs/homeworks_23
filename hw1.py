"""Module for calculating top-3 high and low paid departments."""


def average_salary(new: dict, salary: float | int, depts: str) -> None:
    """
    Write the average salary of departments to the dictionary .

    Args:
        new: dict - dictionary with departments and average salary.
        salary: float | int - salary in the department.
        depts: str - name of department.

    Raises:
        ZeroDivisionError:  if len(salary) == 0.
    """
    if not salary:
        raise ZeroDivisionError('На ноль делить нельзя!')
    new[depts] = round(sum(salary) / len(salary), 2)


def top_departments(department: dict[str, dict], limit: float = None) -> tuple:
    """
    Calculate the average salary of departments.

    Args:
        department: dict - data with departments, its employees and their salaries.
        limit: float - optional arg(default=None), above which salaries are not taken into account.

    Returns:
        tuple:  first - 3 highly paid, second - 3 low-paid departments.
    """
    new = {}
    for depts, employee in department.items():
        if limit:
            filt = {employee: salary for employee, salary in employee.items() if salary < limit}
            if not filt:
                continue
            salary = filt.values()
        else:
            salary = employee.values()
        average_salary(new, salary, depts)
    high_paid_res = (sorted(new, key=new.get, reverse=True))[:3]
    low_paid_res = (sorted(new, key=new.get))[:3]
    return high_paid_res, low_paid_res

