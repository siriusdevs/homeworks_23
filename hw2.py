"""This module include function process_data,which writes statistics to a file."""


import json
import os

mail = 'email'
registr = 'registered'


def is_file(in_path: str, out_path: str) -> None:
    """Check if the arguments are files.

    Args:
        in_path: path to json file with data on site clients
        out_path: path to json output file

    Raises:
        FileNotFoundError: If in_path or out_path is not file
    """
    if not os.path.isfile(in_path) or not os.path.isfile(out_path):
        raise FileNotFoundError('Is not a file path')


def dict_path(count_dct: dict) -> dict:
    """Take a set and two lists and returns a dictionary with statistics.

    Args:
        count_dct:dict with counts

    Returns:
        A dictionary with statistics.
    """
    res_dict = {mail: {}, registr: {}}
    regist_len = len(count_dct[registr])
    email_len = len(count_dct['email'])

    for register, email in zip(count_dct[registr], count_dct[mail]):
        res_dict[registr][register] = round((
            count_dct[registr][register]/regist_len
        )*100, 2,
        )
        res_dict[mail][email] = round((count_dct[mail][email]/email_len)*100, 2)
    return res_dict


def process_data(input_filepath: str, output_filepath: str) -> None:
    """Take json file and returns emailing and registration statiatic.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file

    """
    is_file(input_filepath, output_filepath)
    with open(input_filepath, 'r') as input_file:
        res_dict = {mail: {}, registr: {}}

        for user in json.load(input_file).values():
            for key in user.keys():
                if key == registr:
                    res_dict[registr][user[key]] = res_dict.get(user[key], 0)+1
                elif key == mail:
                    mail_host = user[key][user[key].find('@')+1:]
                    res_dict[mail][mail_host] = res_dict.get(mail_host, 0)+1
        res_dict = dict_path(res_dict)
    with open(output_filepath, 'w') as output_file:
        json.dump(res_dict, output_file)
