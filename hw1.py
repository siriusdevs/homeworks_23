"""This module contains a function that counts average,
maximal and median salary of a company"""


def salary(*opt, **departments: dict[dict[str, int | float]]):
    """The function can count different types of salaries
    Args: positional argument opt,
          some keyword arguments: dict[dict[str, int|float]]
    Returns: a tuple of numbers: int|float
    """
    list_departments = list(departments.values())
    dep = {}
    for department in list_departments:
        dep.update(department)
        salaries = list(dep.values())
    if not opt:
        opt = None
    if opt is not None:
        for sal in salaries.copy():
            if sal > list(opt)[0]:
                salaries.remove(sal)
    sum_salaries = sum(salaries)
    average_salary = sum_salaries / len(salaries)
    max_salary = max(salaries)
    index_middle_salary = len(salaries)//2
    median_salary = salaries[index_middle_salary]
    return round(average_salary, 2), round(max_salary, 2), round(median_salary,2)
print(salary(100000,
             department1={'Ульяна': 80000, 'Игорь': 85000, 'Виктория': 70000},
             department2={'Алина': 100000, 'Катя': 150000, 'Виктор': 150000}))
