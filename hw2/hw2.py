"""Модуль для расчёта статистики."""

import json

from static_city import get_static_sity
from static_last_login import find_was_online


def check_file(path_to_file: str) -> bool:
    """Проверка на существование файла.

    Args:
        path_to_file (str): путь к файлу

    Returns:
        bool: ложь если файл есть, истина если нету
    """
    try:
        with open(path_to_file, 'r'):
            return False
    except FileNotFoundError:
        return True


def process_data(path_to_file_data: str, path_to_file_result: str) -> None | str:
    """Запись и расчёт статистики в json-файл.

    Args:
        path_to_file_data (str): путь к json-файлу с данными о клиентах
        path_to_file_result (str): путь к json-файлу вывода

    Returns:
        none: если нету ошибок
        str: сообщение с ошибкой
    """
    statistics = {}
    cities = []
    last_logins = []

    if check_file(path_to_file_data):
        return f'Файла {path_to_file_data} не существует!'

    with open(path_to_file_data, 'r') as data_file:
        try:
            data_users = json.load(fp=data_file)
        except ValueError:
            return f'Файл {path_to_file_data} пустой!'

    for name in data_users.keys():
        last_logins.append(data_users[name].get('last_login'))
        cities.append(data_users[name].get('region'))

    statistics['statistic last login'] = find_was_online(last_logins)
    statistics['statistic city'] = get_static_sity(cities)

    if not statistics['statistic last login']:
        return 'Некорректная дата'

    if check_file(path_to_file_result):
        return f'Файла {path_to_file_result} не существует!'

    with open(path_to_file_result, 'w', encoding='utf-8') as file_result:
        json.dump(
            statistics,
            file_result,
            indent=4,
            ensure_ascii=False,
        )
