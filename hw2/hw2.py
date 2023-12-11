import json, os
from typing import Any

class PathError(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f'File with path: "{path}" is not exist')

class ExtentionError(Exception):
    def __init__(self, extention: str, expected: str) -> None:
        super().__init__(f'File must be {expected}, but got {extention}')



def open_json(path_to_file: str) -> dict[str:list[Any]]:
    if not os.path.isfile(path_to_file):
        raise PathError(path_to_file)
    
    extention = os.path.splitext(path_to_file)[1]
    if not extention == '.json':
        raise ExtentionError(extention, '.json')
    
    with open(path_to_file) as file:
        data = json.load(file)

    return data