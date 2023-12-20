# import pytest
import json
import os
from testcases import positive_test_data
from hw2 import analyze_json

def create_file(subfolder: str, filename: str) -> str:
    file_path = os.path.join(subfolder, filename)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    with open(file_path, 'w') as new_file:
        new_file.write('')
    
    return file_path

def prepare_data(test_id: int) -> tuple[str, str]:
        to_json = positive_test_data[test_id]
        path_to_json = create_file('./hw2/tests/', f'test_{test_id}.json')
        with open(path_to_json, 'w') as json_to_write:
            json_to_write.write(json.dumps(to_json))
        path_to_result = create_file('./hw2/tests/res/', f'res_{test_id}.json')
        return path_to_json, path_to_result



def positive_tests(test_id) -> bool:
        analyze_json(*prepare_data(test_id))