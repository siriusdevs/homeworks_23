"""Clients statistics module."""
import datetime
import json
import os
from pathlib import Path

thirty_days = 30
half_year = 182

TWO_DAYS = datetime.timedelta(days=2)
ONE_WEEK = datetime.timedelta(weeks=1)
ONE_MONTH = datetime.timedelta(days=thirty_days)
HALF_YEAR = datetime.timedelta(days=half_year)

LAST_LOGIN_KEY = 'last_login'


def get_json_data(
    input_path: str,
):
    """Read the data from the json file.

    Args:
        input_path (str): path to input json file.

    Returns:
        dict: data from the json file.

    Raises:
        ValueError: If there is an unsuitable file in the input data.
    """
    try:
        with open(input_path) as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        raise ValueError(f'Файл {input_path} не существует')
    except json.decoder.JSONDecodeError:
        raise ValueError(f'Передан пустой файл {input_path}')

    if not json_data:
        raise ValueError(f'Файл {input_path} не содержит полезной информации')
    return json_data


def write_json_data(
    output_path: str,
    geography_statistics: dict,
    online_statistics: dict,
    users: int,
):
    """Write the statistics to a json file.

    Args:
        output_path (str): path to output json file.
        geography_statistics (dict): geography statistics.
        online_statistics (dict): online statistics.
        users (int): number of site's users
    """
    path = Path(output_path)
    if not path.parent.exists():
        os.makedirs(path.parent)
    with open(output_path, 'w') as json_statistics:
        json.dump(
            {
                'Geography stats':
                    {
                        region:
                            100*round(
                                amount/users,
                                2,
                            ) for region, amount in geography_statistics.items()
                    },
            }
            | {
                'Last login stats':
                    {
                        date:
                            100*round(
                                amount/users,
                                2,
                            ) for date, amount in online_statistics.items()
                    },
            },
            fp=json_statistics,
        )


def ghostbuster(
    last_login: datetime,
    user_name: str,
    date: str,
) -> None:
    """Catch time traveler.

    Args:
        last_login (datetime): last online time
        user_name (str): time traveler's name
        date (str): time traveler's time

    Raises:
        ValueError: If a time traveler is detected.
    """
    if datetime.datetime.now() < last_login:
        raise ValueError(
            f'Найден человек из будущего. {user_name} из {date}!',
        )


def process_data(
    input_path: str,
    output_path: str = 'output/output.json',
) -> None:
    """Calculate statistics for site clients from a json file.

    Args:
        input_path (str): path to input json file.
        output_path (str): path to output json file.
    """
    json_data = get_json_data(input_path)
    geography_statistics = {}
    online_statistics = {
        '< 2days': 0,
        '< 1week': 0,
        '< 1month': 0,
        '< 1 half year': 0,
        '> half year': 0,
    }

    for user_name, user in json_data.items():

        if 'region' not in user or LAST_LOGIN_KEY not in user:
            continue

        region = user['region']
        if user['region'] not in geography_statistics:
            geography_statistics[region] = 0
        geography_statistics[region] += 1

        last_login = datetime.datetime.strptime(
            user[LAST_LOGIN_KEY].replace('-', ''),
            '%Y%m%d',
        )

        ghostbuster(last_login, user_name, user[LAST_LOGIN_KEY])

        last_online = datetime.datetime.now() - last_login
        match last_online:
            case last_online if last_online < TWO_DAYS:
                online_statistics['< 2days'] += 1
            case last_online if last_online < ONE_WEEK:
                online_statistics['< 1week'] += 1
            case last_online if last_online < ONE_MONTH:
                online_statistics['< 1month'] += 1
            case last_online if last_online < HALF_YEAR:
                online_statistics['< 1 half year'] += 1
            case last_online if last_online > HALF_YEAR:
                online_statistics['> half year'] += 1
    write_json_data(
        output_path,
        geography_statistics,
        online_statistics,
        len(json_data),
    )
