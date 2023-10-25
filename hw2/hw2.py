import json


def process_data(input_path, output_path):
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)
    print(data)
    total_clients = len(data)
    print(total_clients)
    for client, info in data.items():
        print(client)
        print(info)


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu')
