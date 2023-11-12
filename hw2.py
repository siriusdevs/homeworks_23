import json
from datetime import datetime, timedelta


def update_online_stats(
    online_stats: dict,
    time_online: timedelta,
    month: int, six_months: int,
):
    if time_online < timedelta(days=2):
        online_stats['less than 2 days'] += 1
    elif time_online < timedelta(days=7):
        online_stats['less than week'] += 1
    elif time_online < timedelta(days=month):
        online_stats['less than month'] += 1
    elif time_online < timedelta(days=six_months):
        online_stats['less than 6 months'] += 1
    else:
        online_stats['great than 6 months'] += 1


def online(usr_data: dict) -> dict:
    month = 31
    six_months = 186
    online_stats = {
        'less than 2 days': 0,
        'less than week': 0,
        'less than month': 0,
        'less than 6 months': 0,
        'great than 6 months': 0,
        }
    for user_info in usr_data.values():
        registr = datetime.strptime(user_info.get('registered'), '%Y-%m-%d')
        last_log = datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')
        time_online = (last_log - registr)
        update_online_stats(online_stats, time_online, month, six_months)
    return online_stats


def geo(usr_data: dict) -> dict:
    city_stats = {}
    for user_info in usr_data.values():
        region = user_info.get('region')
        if region not in city_stats:
            city_stats[region] = 0
        city_stats[region] += 1
    return city_stats


def process_data(data_file, output_file):
    with open(data_file, 'rt') as inp_f:
        usr_data = json.load(inp_f)
        geo_distribution = {city: num / len(usr_data) for city, num in geo(usr_data).items()}
        online_stats = {period: num / len(usr_data) for period, num in online(usr_data).items()}
        with open(output_file, 'w') as out_f:
            json.dump(
                {
                    'geo_distribution': geo_distribution, 'online_stats': online_stats,
                },
                out_f, indent=4,
            )


process_data('data_hw2.json', 'output.json')
