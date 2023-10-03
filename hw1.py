"""Функция для генерации отчетов о самых высокооплачиваемых и самых низкооплачиваемых отделах."""
import statistics


def generete_report(*departments: tuple, exceptions: tuple = None) -> tuple:
    """Анализирует аргументы и возвращает топ 3 высокооплачиваемых и самых низкооплачиваемых отдела.

    Args:
        departments: tuple - Название отдела и список зарплат сотрудников
        exceptions: tuple - Кортеж с названиями отделов, которые нужно исключить из отчета

    Returns:
        tuple - кортеж из 2 списков: Топ 3 высокооплачиваемых отдела и топ 3 низкооплачиваемых
    """
    def sort_data(department: tuple, reverse: bool) -> list:
        updated_data = sorted(department, key=lambda dpt: statistics.mean(dpt[1]), reverse=reverse)
        return [dpt[0] for dpt in updated_data if dpt[0] not in exceptions]

    if not exceptions:
        exceptions = ()

    higest = sort_data(departments, reverse=True)
    lowest = sort_data(departments, reverse=False)

    return lowest[:3], higest[:3]
