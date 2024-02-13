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


def process_data(
    output_path: str = 'data_result.json',
):
    """
    Функция реализующая анализ существующего json и соберет из него новую статистику.

    Args:
        output_path (str): путь для записи итогового .json файла.

    Returns:
        str: предупреждение о делении на 0.
    """
    json_data = load_json_data()
    result_data = {
        'regions': {},
        'ages': [],
        'last_login_dates': [],
        f'{Constants.total_list[0]}': len(json_data),
    }

    for _user, user_info in json_data.items():
        last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')

        if user_info['region'] not in result_data[Constants.regions_list[0]]:
            result_data[Constants.regions_list[0]][user_info['region']] = 0
        result_data[Constants.regions_list[0]][user_info['region']] += 1

        result_data['ages'].append(user_info['age'])
        result_data['last_login_dates'].append(last_login)

    if Constants.total_list[0] == 0:
        return 'На ноль делить нельзя!'
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
    if (
        (result_data[Constants.total_list[0]] != 0) and \
        (result_data[Constants.total_list_two[0]] != 0) and \
        (result_data['total'] != 0)
    ):
        try:
            result_data['stats'] = {
                'region_distribution': result_data['region_distribution'],
                'average_age': sum(result_data['ages'])
                / result_data[Constants.total_key[0]],
                'online_times': {
                    '<2 days': sum(
                        day < 2 for day in result_data[Constants.online_days[0]]
                    )
                    / result_data[Constants.total_key[0]],
                    '<1 week': sum(
                        day < 7 for day in result_data[Constants.online_days[0]]
                    )
                    / result_data[Constants.total_list_two[0]],
                    '<1 month': sum(
                        day < Constants.month
                        for day in result_data[Constants.online_days[0]]
                    )
                    / result_data[Constants.total_list_two[0]],
                    '>6 months': sum(
                        day > Constants.half_year
                        for day in result_data[Constants.online_days[0]]
                    )
                    / result_data['total'],
                },
            }
        except ZeroDivisionError as error:
            return f'На ноль делить нельзя!\n{error}'
    else:
        return 'На ноль делить нельзя!'

    with open(output_path, 'w') as output_file:
        json.dump(result_data['stats'], output_file)


process_data()
