def company_statistics(*args, included_departments=None):
    """
    Вычисляет статистику по зарплатам сотрудников в компании.

    Args:
    *args: произвольное количество кортежей формата
    (название отдела, словарь сотрудников и их зарплат)
    included_departments (optional): кортеж названий отделов, которые нужно включить в статистику

    Returns:
    Кортеж, содержащий:
    - список трех самых высоких зарплат из всех отделов,
    - процент суммы этих зарплат от общих затрат на зарплаты всех отделов.

    Example:
    department1 = ('Отдел1', {'John': 5000, 'Alice': 6000, 'Bob': 4500})
    department2 = ('Отдел2', {'Emma': 5500, 'David': 4800, 'Olivia': 5200})
    result = company_statistics(department1, department2, included_departments=None)
    sorted_salaries, percentage = result
    print(sorted_salaries, percentage)  # Выводит три самые высокие зарплаты из всех отделов
    """

    all_salaries = []
    for department in args:
        department_name, employees = department
        if included_departments is None or department_name in included_departments:
            all_salaries.extend(employees.values())

    sorted_salaries = sorted(all_salaries, reverse=True)[:3]
    total_payments = sum(all_salaries)

    if total_payments == 0:
        percentage = 0
    else:
        sum_top_salaries = sum(sorted_salaries)
        percentage = round((sum_top_salaries / total_payments) * 100, 2)

    return sorted_salaries, percentage
