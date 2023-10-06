"""Calculates the three smallest and the largest salaries."""


def company_departament(employees: dict, min_salary: float | None = None) -> tuple[list]:
    """
    Extract minimum and maxsimun three salaries.

    Args:
        min_salary: float | None = None.
        employees: dict[str, int] - dict of department names and values.

    Returns:
        list[str] - array for highest and lowest salaries.
    """
    salaries = []
    for employee in employees.keys():
        average_salary = sum(employees[employee].values()) / len(employee)
        if min_salary is None or min_salary <= average_salary:
            salaries.append([average_salary, employee])
    salaries.sort(key=lambda salary: salary[0])
    min_max_department = [salary[1] for salary in salaries]
    return min_max_department[:3], min_max_department[-3:]
