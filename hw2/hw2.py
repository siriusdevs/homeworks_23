import json
from datetime import datetime

def process_data(input_path, output_path):
    hosts_count = dict()
    online_status_count = {
        "less_than_2_days": 0,
        "less_than_a_week": 0,
        "less_than_a_month": 0,
        "less_than_six_months": 0,
        "more_than_six_months": 0
    }
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
        except KeyError:
            raise Exception(f'No last_login field for client {client}.')
    hosts_percentage = {host: (count / TOTAL_CLIENTS) * 100 for host, count in hosts_count.items()}


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
