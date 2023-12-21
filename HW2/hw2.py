import json
from datetime import datetime, timedelta

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    age_categories = [0, 18, 25, 45, 60, float('inf')]
    age_counts = [0] * len(age_categories)
    last_online_categories = [2, 7, 30, 180, float('inf')]
    last_online_counts = [0] * len(last_online_categories)

    for client in data.keys():
        age = data[client]['age']
        for i in range(1, len(age_categories)):
            if age_categories[i-1] <= age < age_categories[i]:
                age_counts[i-1] += 1
                break

        last_online = (datetime.now() - datetime.fromisoformat(data[client]['last_login'])).days
        for i in range(1, len(last_online_categories)):
            if last_online_categories[i-1] <= last_online < last_online_categories[i]:
                last_online_counts[i-1] += 1
                break

    total_clients = len(data)
    age_percentages = [round(count / total_clients * 100, 2) for count in age_counts]
    last_online_percentages = [round(count / total_clients * 100, 2) for count in last_online_counts]

    result = {
        'age_percentages': age_percentages,
        'last_online_percentages': last_online_percentages
    }

    with open(output_file, 'w') as f:
        json.dump(result, f)

if __name__ == '__main__':
    process_data("data_hw2.json", 'result.json')
