"""This module include function process_data, which writes statistics to a file."""

import json
import logging
import os
from datetime import date, datetime
from typing import Any

MAIL = 'email'
REGISTER = 'registered'
logging.basicConfig(level=logging.INFO)


def load_input_file(input_filepath: str, output_filepath: str) -> Any:
    """Read content file.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file

    Returns:
        Content file or None.
    """
    try:
        with open(input_filepath, 'r') as input_file:
            return json.load(input_file)
    except json.decoder.JSONDecodeError as err:
        logging.error('Input file is empty')
        dump_to_invalid_file(output_filepath, type(err).__name__, 'Input file is empty')
    except PermissionError as err:
        msg = f'({output_filepath})access denied'
        logging.error(msg)
        dump_to_invalid_file(output_filepath, type(err).__name__, msg)
        return None


def dump_to_invalid_file(output_filepath: str, err: str, msg: str) -> None:
    """Write in file type and message about error.

    Args:
        output_filepath: path to json output file
        err: type of error
        msg: message about error
    """
    with open(output_filepath, 'w') as output_file:
        json.dump(obj={
            'status': err, 'message': msg,
        },
            fp=output_file,
        )


def to_datetime(output_filepath: str, regisrated: str, last_login: str) -> datetime | None:
    """Check if the date is in the format and lower then today date and last login date.

    Args:
        output_filepath: path to json output file
        regisrated: string with user regisrated date
        last_login: string with user last login

    Returns:
        Object datetime type.
    """
    try:
        regisrated, last_login = date.fromisoformat(regisrated), date.fromisoformat(last_login)
    except ValueError as err:
        msg = f'{regisrated} in uncorrect format YYYY-MM-DD or time'
        logging.error(msg)
        dump_to_invalid_file(output_filepath, type(err).__name__, msg)
        return None

    if regisrated <= datetime.now().date() and regisrated <= last_login:
        return regisrated

    msg = f'{regisrated} in uncorrect time'
    logging.error(msg)
    dump_to_invalid_file(output_filepath, 'TimeDateError', msg)


def file_found(in_path: str, out_path: str) -> bool:
    """Check if the arguments are files.

    Args:
        in_path: path to json file with data on site clients
        out_path: path to json output file

    Returns:
        False if File not found or None.
    """
    if not os.path.isfile(out_path):
        logging.info('Output file not found, create')
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)

    if not os.path.isfile(in_path):
        msg = 'Is not a file path'
        logging.error(msg)
        dump_to_invalid_file(out_path, 'FileNotFoundError', msg)
        return False
    return True


def dict_path(count_dct: dict[datetime, dict]) -> dict[str, dict]:
    """Take a set and two lists and returns a dictionary with statistics.

    Args:
        count_dct:dict with counts

    Returns:
        A dictionary with statistics.
    """
    res_dict = {MAIL: {}, REGISTER: {}}
    regist_len = len(count_dct[REGISTER]) if count_dct[REGISTER] else 1
    email_len = len(count_dct[MAIL]) if count_dct[MAIL] else 1

    for register, mail_host in zip(sorted(count_dct[REGISTER]), count_dct[MAIL]):
        new_register = register.strftime('%Y-%m-%d')
        res_dict[REGISTER][new_register] = round((
            count_dct[REGISTER][register]/regist_len
        )*100, 2,
        )
        res_dict[MAIL][mail_host] = round((count_dct[MAIL][mail_host]/email_len)*100, 2)
    return res_dict


def process_data(input_filepath: str, output_filepath: str) -> None:
    """Take json file and returns emailing and registration statiatic.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file
    """
    if not file_found(input_filepath, output_filepath):
        return

    res_dict = {MAIL: {}, REGISTER: {}}
    data_files = load_input_file(input_filepath, output_filepath)

    if data_files is None:
        return

    if not isinstance(data_files, dict):
        msg = 'Content in file must be dict'
        logging.error(msg)
        dump_to_invalid_file(output_filepath, 'InvalidContentFile', msg)
        return

    for user in data_files.values():
        if user.get(REGISTER):
            reg_date = to_datetime(output_filepath, user.get(REGISTER), user.get(
                'last_login', datetime.now().strftime('%Y-%m-%d'),
            ))
            if not reg_date:
                return
            res_dict[REGISTER][reg_date] = res_dict.get(reg_date, 0)+1
        if user.get(MAIL):
            user_mail = user.get(MAIL)
            mail_host = user_mail[user_mail.find('@')+1:]
            res_dict[MAIL][mail_host] = res_dict.get(mail_host, 0)+1

    res_dict = dict_path(res_dict)

    with open(output_filepath, 'w') as output_file:
        json.dump(res_dict, output_file, indent=3)
    logging.info(f'Statistic was dumps in file ({output_filepath})')
