"""Function that calculates website usage statistics."""
import json
import os
from datetime import datetime

MONTH = 30
HALF_YEAR = 180
mail_host = {}
time_stats = {
    'less_then_2_days': [],
    'less_then_1_week': [],
    'less_then_1_month': [],
    'less_then_6_months': [],
    'more_then_6_months': [],
}


def check_is_file(file_name: str) -> bool:
    """Chekcs that file is a file.

    Args:
        file_name: name of the input data file.

    Raises:
        FileNotFoundError: if file is not a file or is not exist.

    """
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f'<{file_name}> is not a file or is not exist.')


def check_by_time(user_info: dict) -> None:
    """Dictributes age over time.

    Args:
        user_info: dict - information of user.

    """
    age = user_info.get('age')
    online = datetime.now() - datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')

    if online.days <= 2:
        time_stats['less_than_2_days'].append(age)
    elif online.days <= 7:
        time_stats['less_than_1_week'].append(age)
    elif online.days <= MONTH:
        time_stats['less_then_1_month'].append(age)
    elif online.days <= HALF_YEAR:
        time_stats['less_then_6_months'].append(age)
    else:
        time_stats['more_then_6_months'].append(age)


def process_data(input_data, output_data):
    """Calculate websites usage statistics.

    Args:
        input_data: name of the input data file.
        output_data: name of the output data file.

    """
    check_is_file(input_data)
    with open(input_data) as input_file:
        information: dict[str, dict] = json.load(input_file)

    for user_info in information.values():
        email: str = user_info.get('email')
        if email:
            email_parts = email.split('@')
            if email_parts[1] not in mail_host.keys():
                mail_host[email_parts[1]] = 0
            if len(email_parts) == 2:
                mail_host[email_parts[1]] += 1

        check_by_time(user_info)

    for user_quantity in time_stats.values():
        user_quantity = sum(user_quantity) / len(user_quantity) if user_quantity else 0

    stats: dict[str, dict[str, list]] = {
        'email_usage': mail_host,
        'time_stats': time_stats,
        }

    with open(output_data, 'w') as output_file:
        json.dump(stats, output_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    process_data('data_hw2.json', 'stats_data.json')
