import json


def process_data(input_path, output_path):
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)
    print(data)
    total_clients = len(data)
    hosts_count = dict()
    print(total_clients)
    for client, info in data.items():
        print(client)
        host = info.get('email').split('@')[1]
        if host:
            hosts_count[host] = hosts_count.get(host, 0) + 1
        print(host)
        print(info)


    hosts_pecentage = {host: (count / total_clients) * 100 for host, count in hosts_count.items()}


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
