"""This module include function process_data."""


import json
import os


def is_file(in_path: str, out_path: str) -> bool:
    """Check if the arguments are files.

    Args:
        in_path: path to json file with data on site clients
        out_path: path to json output file

    Raises:
        FileNotFoundError: If in_path or out_path is not file
    """
    if not os.path.isfile(in_path) or not os.path.isfile(out_path):
        raise FileNotFoundError('Is not a file path')


def dict_path(set_names: set, registr: list, mail: list) -> dict:
    """Take a set and two lists and returns a dictionary with statistics.

    Args:
        set_names:set of mail and registrar list joins
        registr: list with data of registration
        mail: list with mails host

    Returns:
        Returns a dictionary with statistics.
    """
    res_dict = {}
    for name in set_names:
        if name in registr:
            res_dict[name] = round((registr.count(name)/len(registr))*100, 2)
        else:
            res_dict[name] = round((mail.count(name)/len(mail))*100, 2)
    return res_dict


def process_data(input_filepath: str, output_filepath: str) -> None | str:
    """Take json file and returns emailing and registration statiatic.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file

    """
    is_file(input_filepath, output_filepath)
    with open(input_filepath, 'r') as file1:
        registrated = []
        email = []
        for user in json.load(file1).values():
            for key in user.keys():
                if key == 'registered':
                    registrated.append(user[key])
                elif key == 'email':
                    email.append(user[key].split('@')[1])
    res_dict = dict_path(sorted((set(registrated+email))), registrated, email)
    with open(output_filepath, 'w') as file2:
        json.dump(res_dict, file2)
