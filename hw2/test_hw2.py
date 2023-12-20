import pytest
import json
import os
from testcases import positive_test_data, negative_test_data
from test_answers import test_answers
from hw2 import analyze_json

def create_file(subfolder: str, filename: str) -> str:
    file_path = os.path.join(subfolder, filename)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    with open(file_path, 'w') as new_file:
        new_file.write('')
    
    return file_path

def prepare_data(test_id: int, positive: bool = True) -> tuple[str, str]:
        if positive:
            test_data = positive_test_data[test_id]
        else:
            test_data = negative_test_data[test_id]

        to_json = test_data
        path_to_json = create_file('./hw2/tests/', f'test_{test_id}.json')
        with open(path_to_json, 'w') as json_to_write:
            json_to_write.write(json.dumps(to_json))
        path_to_result = create_file('./hw2/tests/res/', f'res_{test_id}.json')
        return path_to_json, path_to_result

def get_result(path_to_result) -> str:
        result_json = open(path_to_result)
        result_line = result_json.read()
        return result_line

def positive_tests(test_id: int) -> bool:
    path_to_json, path_to_result = prepare_data(test_id)
    analyze_json(path_to_json, path_to_result)
    is_correct = get_result(path_to_result) == test_answers[test_id]

    return is_correct

def negative_tests(test_id: int) -> bool:
    path_to_json, path_to_result = prepare_data(test_id, positive=False)
    analyze_json(path_to_json, path_to_result)
    is_correct = (get_result(path_to_result) == test_answers[test_id])
    
    return is_correct

print(negative_tests(5))    