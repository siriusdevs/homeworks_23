from typing import Optional


def salary(*departments: tuple, maxs: Optional[int] = None) -> tuple:
    """
    A function that displays the top 3 salaries, the ratio of the top salaries to the
    total company salaries (as a percentage)

    Args:
        departments: tuple -  a tuple containing tuples of department names and salary information.
        maxs: (int or None) - maximum salary limit.

    Returns:
        salaty_ratio: int -  the ratio of the top to the entire salary.
        maximum_salary: List - top maximum salaries
    """
    main_list = []

    for department in departments:
        if isinstance(department[1], dict):
            for salary in department[1].values():
                main_list.append(salary)

    # создадим отдельный список, с учетом максимального числа зарплаты
    if maxs is None:
        maxs = max(main_list)

    side_list = [round(x, 2) for x in main_list if x <= maxs]
    side_list.sort()
    maximum_salary = side_list[:-4:-1]

    # найдем отношение топа ко всей зарплате
    salary_ratio = round(((sum(maximum_salary) / sum(main_list)) * 100), 2)

    return maximum_salary, salary_ratio


print(salary(
    (
        'testing department',
        {
                'Ivanov': 10000,
                'Trofimov': 20000,
                'Tenigin': 30000
            }
    ),

    (
        'security department',
        {
            'Tereshin': 40000,
            'Rindin': 50000,
            'Zorina': 60000
        }
    ),

    (
        'sales department',
        {
            'Simonova': 70000,
            'Zaizev': 80000,
            'Ivanova': 90000
        }
    ),
    maxs=90000
)
)
