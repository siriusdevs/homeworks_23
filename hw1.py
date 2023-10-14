"""Calculates the three smallest and the largest salaries."""


def company_departament(departments: [str, dict], min_salary: float | None = None) -> tuple[list]:
    """
    Extract minimum and maxsimun three salaries.

    Args:
        min_salary: float | None = None.
        departments: dict[str, dict] - dict of department names and values.

    Returns:
        tuple[list] - array for highest and lowest salaries.
    """
    salaries = []

    for department, dept_salaries in departments.items():
        if not dept_salaries:
            continue
        if min_salary:
            dept_salaries = [salary for salary in dept_salaries.values() if salary >= min_salary]
        else:
            dept_salaries = list(dept_salaries.values())
        all_salary = sum(dept_salaries)
        average_salary = all_salary / max(len(dept_salaries), 1)
        salaries.append([average_salary, department])
    salaries.sort(key=lambda salary: salary[0])
    min_max_department = [salary[1] for salary in salaries]
    return min_max_department[:3], min_max_department[-3:]
