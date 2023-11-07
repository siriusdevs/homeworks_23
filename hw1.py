"""The typing module provides support for defining and using type hints in Python."""
from typing import Optional


def salary(*departments: tuple, maxs: Optional[int] = None) -> tuple:
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
    main_list = []

    for department in departments:
        if isinstance(department[1], dict):
            for salary_depa in department[1].values():
                main_list.append(salary_depa)
        if sum(main_list) == 0:
            raise ValueError('all salaries are zero')

    # создадим отдельный список, с учетом максимального числа зарплаты
    if maxs is None:
        maxs = max(main_list)

    side_list = [round(num, 2) for num in main_list if num <= maxs]
    side_list.sort()
    maximum_salary = side_list[:-4:-1]

    # найдем отношение топа ко всей зарплате
    salary_ratio = round(((sum(maximum_salary) / sum(main_list)) * 100), 2)

    return maximum_salary, salary_ratio
