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

    data = {
        'regions': {},
        'ages': [],
        'last_login_dates': [],
        'total': len(json_data),
    }

    for _user, user_info in json_data.items():
        last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')

        if user_info['region'] not in data['regions']:
            data['regions'][user_info['region']] = 0
        data['regions'][user_info['region']] += 1

        data['ages'].append(user_info['age'])
        data['last_login_dates'].append(last_login)

    data['region_distribution'] = {
        region: (count / data['total']) * 100 for region, count in data['regions'].items()
    }

    data['online_times'] = [datetime.now() - date for date in data['last_login_dates']]
    data['online_days'] = [time.total_seconds() / (60 * 60 * 24) for time in data['online_times']]

    data['stats'] = {
        'region_distribution': data['region_distribution'],
        'average_age': sum(data['ages']) / data['total'],
        'online_times': {
            '<2 days': sum(day < 2 for day in data['online_days']) / data['total'],
            '<1 week': sum(day < 7 for day in data['online_days']) / data['total'],
            '<1 month': sum(day < MONTH for day in data['online_days']) / data['total'],
            '<6 months': sum(day < HALF_YEAR for day in data['online_days']) / data['total'],
            '>6 months': sum(day > HALF_YEAR for day in data['online_days']) / data['total'],
        },
    }

    with open(output_path, 'w') as output_file:
        json.dump(data['stats'], output_file)


process_data()
