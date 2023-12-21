import pytest
import json
from hw2 import process_data

def test_process_data():
    # Создаем тестовые данные
    test_data = {
        "client1": {"age": 20, "last_login": "2022-01-01"},
        "client2": {"age": 30, "last_login": "2022-02-01"},
        "client3": {"age": 40, "last_login": "2022-03-01"},
    }

    with open("test_data.json", "w") as f:
        json.dump(test_data, f)

    # Вызываем функцию с тестовыми данными
    process_data("test_data.json", "test_result.json")

    # Загружаем результаты
    with open("test_result.json", "r") as f:
        result = json.load(f)

    # Проверяем результаты
    assert result["age_percentages"] == [0.0, 33.33, 33.33, 33.33, 0.0]
    assert result["last_online_percentages"] == [100.0, 0.0, 0.0, 0.0, 0.0]

    # Удаляем тестовые файлы
    os.remove("test_data.json")
    os.remove("test_result.json")