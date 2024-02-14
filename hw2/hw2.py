"""Файл с ДЗ 2."""
import json
from datetime import datetime

from init_constants import Constants


def load_json_data(input_path: str = 'data_hw2.json'):
    """
    Функция подгрузки json информации.

    Args:
        input_path (str): путь к файлу json.

    Returns:
        dict: загруженный json.
    """
    with open(input_path, 'r') as input_file:
        return json.load(input_file)


def calculate_statistics(result_data, key):
    """
    Функция подсчета среднего возраста.

    Args:
        result_data: dict, содержащий в себе данные.
        key: dict, ключ поиска по словарю.

    Returns:
        Union[int: средний возраст, dict: ошибка о делении на 0]
    """
    try:
        return sum(result_data['ages']) / result_data[key]
    except ZeroDivisionError:
        return {'ошибка': 'Деление на  0 запрещено.'}


def calculate_online_times_statistics(result_data, online_days_key, total_key):
    """
    Вычисляет статистику онлайн-времени пользователей.

    Args:
        result_data: dict, словарь с данными.
        online_days_key: str, ключ для словаря result_data.
        total_key: str, ключ для словаря result_data.

    Returns:
        dict: Словарь с данными после анализа/Ошибка о делении на 0.
    """
    try:
        return {
            '<2 days': sum(day < 2 for day in result_data[online_days_key])
            / result_data[total_key],
            '<1 week': sum(day < 7 for day in result_data[online_days_key])
            / result_data[total_key],
            '<1 month': sum(
                day < Constants.month for day in result_data[online_days_key]
            )
            / result_data[total_key],
            '>6 months': sum(
                day > Constants.half_year for day in result_data[online_days_key]
            )
            / result_data[total_key],
        }
    except ZeroDivisionError:
        return {'ошибка': 'Деление на  0 запрещено.'}


def gather_regional_data(result_data, user_info):
    """
    Анализ собранных данных.

    Args:
        result_data (dict): Словарь для хранения региональных данных.
        user_info (dict): Информация о пользователе, включая регион.
    """
    if user_info['region'] not in result_data[Constants.regions_list[0]]:
        result_data[Constants.regions_list[0]][user_info['region']] = 0
    result_data[Constants.regions_list[0]][user_info['region']] += 1


def gather_age_and_last_login_dates(result_data, user_info):
    """
    Анализ и обновление существующих данных.

    Args:
        result_data (dict): Словарь для хранения возраста и дат последнего входа в систему.
        user_info (dict): Информация о пользователе, включая возраст и последний вход в систему.
    """
    result_data['ages'].append(user_info['age'])
    last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')
    result_data['last_login_dates'].append(last_login)


def process_data(output_path: str = 'data_result.json'):
    """
    Функция реализующая анализ существующего json и соберет из него новую статистику.

    Args:
        output_path (str): путь для записи итогового .json файла.

    Returns:
        str: dict, предупреждение о делении на 0.
    """
    result_data = {
        'regions': {},
        'ages': [],
        'last_login_dates': [],
        f'{Constants.total_list[0]}': len(load_json_data()),
    }

    for _user, user_info in (load_json_data()).items():
        gather_regional_data(result_data, user_info)
        gather_age_and_last_login_dates(result_data, user_info)

    if Constants.total_list[0] == 0:
        return {'ошибка': 'Деление на  0 запрещено.'}
    else:
        result_data['region_distribution'] = {
            region: (count / result_data[Constants.total_list[0]]) * 100
            for region, count in result_data[Constants.regions_list[0]].items()
        }

    result_data['online_times'] = [
        datetime.now() - date for date in result_data['last_login_dates']
    ]
    result_data['online_days'] = [
        time.total_seconds() / (60 * 60 * 24) for time in result_data['online_times']
    ]

    condition = result_data[Constants.total_list[0]] != 0 and \
        result_data[Constants.total_list_two[0]] != 0 and \
        result_data['total'] != 0

    if condition:
        online_times = calculate_online_times_statistics(
            result_data,
            Constants.online_days[0],
            Constants.total_key[0],
        )

        if calculate_statistics(result_data, Constants.total_key[0]) is None:
            return {'Ошибка': 'Деление на 0 запрещено.'}

        result_data['stats'] = {
            'region_distribution': result_data['region_distribution'],
            'average_age': calculate_statistics(result_data, Constants.total_key[0]),
            'online_times': online_times,
        }
    else:
        return {'Ошибка': 'Деление на   0 запрещено.'}

    with open(output_path, 'w') as output_file:
        json.dump(result_data['stats'], output_file)


process_data()
