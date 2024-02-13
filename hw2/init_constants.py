"""Константы для файла hw2."""
import json


class Constants:
    """Класс инициализации глобальных переменных."""

    regions_list = ['regions']
    total_list = ['total']
    total_key = ['total']
    online_days = ['online_days']
    total_list_two = ['total']
    month = 30
    half_year = 180
    json_data = None

    def load_json_data(self, input_path='data_hw2.json'):
        """
        Метод для загрузки json данных.

        Args:
            input_path (str): Путь к файлу json.

        Returns:
            dict: Загруженный json.
        """
        with open(input_path, 'r') as input_file:
            self.json_data = json.load(input_file)
