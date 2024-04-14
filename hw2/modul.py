import json
from collections import Counter
from datetime import datetime, timedelta

def calculate_age_category(age):
    if age <= 18:
        return '0-18'
    elif age <= 25:
        return '19-25'
    elif age <= 45:
        return '26-45'
    elif age <= 60:
        return '46-60'
    else:
        return '60+'

def calculate_online_intervals(login_dates):
    intervals = {
        '<2 days': 0,
        '<1 week': 0,
        '<1 month': 0,
        '<6 months': 0,
        '>6 months': 0
    }
    today = datetime.now()
    for date_str in login_dates:
        login_date = datetime.strptime(date_str, '%Y-%m-%d')
        delta = today - login_date
        if delta < timedelta(days=2):
            intervals['<2 days'] += 1
        elif delta < timedelta(weeks=1):
            intervals['<1 week'] += 1
        elif delta < timedelta(weeks=4):
            intervals['<1 month'] += 1
        elif delta < timedelta(weeks=24):
            intervals['<6 months'] += 1
        else:
            intervals['>6 months'] += 1
    total_logins = len(login_dates)
    return {key: (value / total_logins) * 100 for key, value in intervals.items()}

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    ages = [user.get('age', 0) for user in data.values() if isinstance(user.get('age'), int)]
    age_counter = Counter(calculate_age_category(age) for age in ages)

    login_dates = [user.get('last_login', '') for user in data.values() if isinstance(user.get('last_login'), str)]
    online_intervals = calculate_online_intervals(login_dates)

    total_users = len(data)

    age_percentage = {category: (count / total_users) * 100 for category, count in age_counter.items()}

    result = {
        'age_distribution': age_percentage,
        'online_intervals': online_intervals
    }

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

# Пример использования:
process_data('hw2/tests_folder/test2.json', 'hw2/expected_folder/2.json')
