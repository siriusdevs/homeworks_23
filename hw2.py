"""Function that calculates website usage statistics."""
import json
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


def process_data(input_data, output_data):
    """Calculate websites usage statistics.

    Args:
        input_data: name of the input data file.
        output_data: name of the output data file.

    """
    with open(input_data) as in_fl:
        information: dict[str, dict] = json.load(in_fl)

    for user_info in information.values():
        email: str = user_info.get('email')
        if email:
            email_parts = email.split('@')
            if email_parts[1] not in mail_host.keys():
                mail_host[email_parts[1]] = 0
            if len(email_parts) == 2:
                mail_host[email_parts[1]] += 1

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

    for online_time, user_quantity in time_stats.values():
        if user_quantity:
            time_stats[online_time] = sum(user_quantity) / len(user_quantity)
        else:
            time_stats[online_time] = 0

    stats: dict[str, dict[str, list]] = {
        'email_usage': mail_host,
        'time_stats': time_stats,
        }

    with open(output_data, 'w') as out_fl:
        json.dump(stats, out_fl, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    process_data('data_hw2.json', 'stats_data.json')
