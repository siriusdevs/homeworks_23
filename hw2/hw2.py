import json
from datetime import datetime


online_status_count = {
    "less_than_2_days": 0,
    "less_than_a_week": 0,
    "less_than_a_month": 0,
    "less_than_six_months": 0,
    "more_than_six_months": 0
}


def process_data(input_path, output_path):
    hosts_count = dict()
    hosts_percentage = dict()
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)
    TOTAL_CLIENTS = len(data)
    for client, info in data.items():
        try:
            host = info['email'].split('@')[1]
            if not host:
                raise Exception(f'email field is empty for client {client}')
            hosts_count[host] = hosts_count.get(host, 0) + 1
        except KeyError:
            raise Exception(f'No email field for client {client}.')
        try:
            last_login = info['last_login']
            if not last_login:
                raise Exception(f'last_login field is empty for client {client}')
            date = datetime.strptime(last_login, '%Y-%m-%d')
            last_login_ago = (datetime.now() - date).days
            fill_online_status_count(last_login_ago)
        except KeyError:
            raise Exception(f'No last_login field for client {client}.')
    for host, count in hosts_count.items():
        hosts_percentage[host] = round((count / TOTAL_CLIENTS) * 100, 2)


def fill_online_status_count(last_login_ago: int) -> None:
    if last_login_ago < 2:
        online_status_count['less_than_2_days'] += 1
    elif last_login_ago < 7:
        online_status_count['less_than_a_week'] += 1
    elif last_login_ago < 30:
        online_status_count['less_than_a_month'] += 1
    elif last_login_ago < (30 * 6):
        online_status_count['less_than_six_months'] += 1
    else:
        online_status_count['more_than_six_months'] += 1


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
