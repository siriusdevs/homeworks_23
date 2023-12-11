"""Модуль для получения статистики по городам."""


def get_static_sity(cities: list):
    """Получить статистику по городам.

    Args:
        cities (list): города

    Returns:
        dict: словарь со статистикой по городам
    """
    static = {}
    for city in cities:
        if city in static.keys():
            static[city] += 1
        else:
            static[city] = 1

    for key in static.keys():
        percent = round(static[key] / len(cities) * 100)
        static[key] = f'{percent}%'

    return static
