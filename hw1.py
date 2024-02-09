"""The typing module provides support for defining and using type hints."""
from typing import Optional, Union


def check_salary(
    departments: tuple[str, dict],
    maxs: Optional[int],
) -> tuple[list[float], Union[int, float]]:
    """_summary_.

    Args:
        departments (tuple[str, dict]): motorcade with the department and its salaries
        maxs (Optional[int]): salary limit

    Raises:
        ValueError: if the given argument is not in the dictionary
        TypeError: _description_

    Returns:
        tuple[list[float], Union[int, float]]: if department is not a string
    """
    main_list = []
    for department, employees in departments:
        if not isinstance(employees, dict):
            raise ValueError('the salary is not assigned to the employee')

        if not isinstance(department, str):
            raise TypeError('incorrectly named department')

        employee = employees

    for salary_depa in employee.values():
        main_list.append(salary_depa)
    if maxs == float('inf'):
        maxs = max(main_list)

# создадим отдельный список, с учетом максимального числа зарплаты
    side_list = [round(num, 2) for num in main_list if maxs is None or num <= maxs]
    side_list.sort()
    return side_list, main_list


def salary(*departments: tuple, maxs: Optional[int] = None) -> tuple[list, Union[int, float]]:
    """.

    A function that displays the top 3 salaries, the ratio of the top salaries to the
    total company salaries (as a percentage)

    Args:
        departments: tuple -  a tuple containing tuples of department names and salary information.
        maxs: (int or None) - maximum salary limit.

    returns:
        tuple - top 3 maximum salary and attitude

    Raises:
        ValueError: if the salary is zero.
    """
    side_list, main_list = check_salary(departments, maxs)
    maximum_salary = side_list[:-4:-1]

    try:
        # найдем отношение топа ко всей зарплате
        salary_ratio = round(((sum(maximum_salary) / sum(main_list)) * 100), 2)
    except ZeroDivisionError:
        raise ValueError('the salary of all departments is zero')

    return maximum_salary, salary_ratio
