"""Файл с ДЗ 2."""
import json
from datetime import datetime

MONTH = 30
HALF_YEAR = 180


def process_data(
    input_path: str = 'data_hw2.json', output_path: str = 'data_result.json',
):
    """
    Функция реализующая анализ существующего json и соберет из него новую статистику.

    Args:
        input_path (str): путь, где находится .json файл.
        output_path (str): путь для записи итогового .json файла.
    """
    with open(input_path, 'r') as input_file:
        json_data = json.load(input_file)

    result_data = {
        'regions': {},
        'ages': [],
        'last_login_dates': [],
        'total': len(json_data),
    }

    for _user, user_info in json_data.items():
        last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')

        if user_info['region'] not in result_data['regions']:
            result_data['regions'][user_info['region']] = 0
        result_data['regions'][user_info['region']] += 1

        result_data['ages'].append(user_info['age'])
        result_data['last_login_dates'].append(last_login)

    result_data['region_distribution'] = {
        region: (count / result_data['total']) * 100 for region, count in result_data['regions'].items()
    }

    result_data['online_times'] = [datetime.now() - date for date in result_data['last_login_dates']]
    result_data['online_days'] = [time.total_seconds() / (60 * 60 * 24) for time in result_data['online_times']]

    const = result_data['total']
    const2 = result_data['online_days']
    result_data['stats'] = {
        'region_distribution': result_data['region_distribution'],
        'average_age': sum(result_data['ages']) / result_data['total'],
        'online_times': {
            '<2 days': sum(day < 2 for day in const2) / const,
            '<1 week': sum(day < 7 for day in const2) / const,
            '<1 month': sum(day < MONTH for day in const2) / const,
            '<6 months': sum(day < HALF_YEAR for day in const2) / const,
            '>6 months': sum(day > HALF_YEAR for day in const2) / const,
        },
    }

    with open(output_path, 'w') as output_file:
        json.dump(result_data['stats'], output_file)


process_data()
