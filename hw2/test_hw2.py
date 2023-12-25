"""Класс тестирования для функции process_data."""
import json
import os
import unittest

from hw2 import process_data


class TestProcessData(unittest.TestCase):
    """Класс содержащий в себе функции тестирования."""

    def test_process_data(self):
        """Метод тестирования возвращаемого json файла."""
        input_path = os.path.join('data_hw2.json')
        output_path = os.path.join('data_result.json')

        process_data(input_path, output_path)

        with open(output_path, 'r') as output_file:
            stats = json.load(output_file)

        self.assertIsInstance(stats, dict)
        self.assertIn('region_distribution', stats)
        self.assertIn('registration_years_distribution', stats)

    def test_file_paths(self):
        """Метод тестирования существующих файлов."""
        input_path = 'data_hw2.json'
        output_path = 'data_result.json'

        self.assertTrue(
            os.path.exists(input_path),
            msg='Файл {0} не найден'.format(input_path),
        )
        self.assertTrue(
            os.path.exists(output_path),
            msg='Файл {0} не найден'.format(output_path),
        )


if __name__ == '__main__':
    unittest.main()
