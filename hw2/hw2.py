import json


def process_data(input_path, output_path):
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)
    print(data)
    total_clients = len(data)
    email_hosts_count = dict()
    print(total_clients)
    for client, info in data.items():
        print(client)
        email_host = info.get('email').split('@')[1]
        if email_host:
            email_hosts_count[email_host] = email_hosts_count.get(email_host, 0) + 1
        print(email_host)
        print(info)


    email_host_pecentage = {host: (count/total_clients) * 100 for host, count in email_hosts_count.items()}


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
