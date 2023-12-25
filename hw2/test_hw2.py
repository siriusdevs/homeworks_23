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
        self.assertIn('average_age', stats)
        self.assertIn('online_times', stats)


if __name__ == '__main__':
    unittest.main()

