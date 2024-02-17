"""Класс тестирования для функции process_data."""
import json
import os
import unittest

from hw2 import process_data


class TestProcessData(unittest.TestCase):
    """Класс содержащий в себе функции тестирования."""

    def test_process_data(self):
        """Метод тестирования возвращаемого json файла."""
        output_path = os.path.join('data_result.json')

        process_data(output_path)

        with open(output_path, 'r') as input_file:
            stats = json.load(input_file)

        self.assertIsInstance(stats, dict)

        if 'region_distribution' not in stats:
            self.fail("Ключ 'region_distribution' не найден в итоговом JSON.")
        else:
            self.assertIsInstance(stats['region_distribution'], dict)

        if 'average_age' not in stats:
            self.fail("Ключ 'average_age' не найден в итоговом JSON.")
        else:
            self.assertIsInstance(stats['average_age'], (int, float))

        if 'online_times' not in stats:
            self.fail("Ключ 'online_times' не найден в итоговом JSON.")
        else:
            self.assertIsInstance(stats['online_times'], dict)


if __name__ == 'main':
    unittest.main()
