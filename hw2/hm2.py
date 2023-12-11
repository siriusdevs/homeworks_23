"""Модуль для расчёта статистики."""

import json

from static_city import get_static_sity
from static_last_login import find_was_online


def process_data(path_to_file_data: str, path_to_file_result: str):
    """Запись и расчёт статистики в json-файл.

    Args:
        path_to_file_data (str): путь к json-файлу с данными о клиентах
        path_to_file_result (str): путь к json-файлу вывода
    """
    statistics = {'statictik city': {}, 'statictik last login': {}}
    cities = []
    last_logins = []
    with open(path_to_file_data, 'r') as data_file:
        data_users = json.load(fp=data_file)
        for name in data_users.keys():
            last_logins.append(data_users[name].get('last_login'))
            cities.append(data_users[name].get('region'))

    statistics['statictik last login'] = find_was_online(last_logins)
    statistics['statictik city'] = get_static_sity(cities)

    with open(path_to_file_result, 'w', encoding='utf-8') as file_result:
        json.dump(
            statistics,
            file_result,
            indent=4,
            ensure_ascii=False,
        )
