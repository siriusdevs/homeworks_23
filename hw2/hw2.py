"""Docstring."""

import json
from datetime import datetime

online_status_count = {
    'less_than_2_days': 0,
    'less_than_a_week': 0,
    'less_than_a_month': 0,
    'less_than_six_months': 0,
    'more_than_six_months': 0,
}


def process_data(input_path, output_path) -> None:
    hosts_count = {}
    hosts_percentage = {}
    with open(input_path, 'r') as input_file:
        json_data = json.load(input_file)
    total_clients = len(json_data)
    for client, client_info in json_data.items():
        try:
            host = client_info['email'].split('@')[1]
        except KeyError:
            raise Exception(f'No email field for client {client}.')
        if not host:
            raise Exception(f'email field is empty for client {client}')
        hosts_count[host] = hosts_count.get(host, 0) + 1
        last_login = get_last_login()
        date = datetime.strptime(last_login, '%Y-%m-%d')
        last_login_ago = (datetime.now() - date).days
        fill_online_status_count(last_login_ago)
    for host_name, count in hosts_count.items():
        hosts_percentage[host_name] = round((count / total_clients) * 100, 2)


def get_last_login(client_info: dict) -> None:
    try:
        last_login = client_info['last_login']
    except KeyError:
        raise Exception(f'No last_login field for client {client}.')
    if not last_login:
        raise Exception(f'last_login field is empty for client {client}')
    return last_login


def fill_online_status_count(last_login_ago: int) -> None:
    two_days = 2
    week = 7
    month = 30
    six_months = month * 6
    if last_login_ago < two_days:
        online_status_count['less_than_2_days'] += 1
    elif last_login_ago < week:
        online_status_count['less_than_a_week'] += 1
    elif last_login_ago < month:
        online_status_count['less_than_a_month'] += 1
    elif last_login_ago < (six_months):
        online_status_count['less_than_six_months'] += 1
    else:
        online_status_count['more_than_six_months'] += 1


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
