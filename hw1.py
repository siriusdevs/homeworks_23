"""The typing module provides support for defining and using type hints."""
from typing import Optional, Tuple, Union


def check_salary(
    departments: Tuple[str, dict],
    maxs: Optional[int],
) -> Tuple[list[float], Union[int, float]]:
    """_summary_.

    Args:
        departments (Tuple[str, dict]): _description_
        maxs (Optional[int]): _description_

    Raises:
        ValueError: _description_
        TypeError: _description_

    Returns:
        Tuple[list[float], Union[int, float]]: _description_
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


def salary(*departments: tuple, maxs: Optional[int] = None) -> Tuple[list, Union[int, float]]:
    """.

    A function that displays the top 3 salaries, the ratio of the top salaries to the
    total company salaries (as a percentage)

    Args:
        departments: tuple -  a tuple containing tuples of department names and salary information.
        maxs: (int or None) - maximum salary limit.

    returns:
        typle - top 3 maximum salary and attitude

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
