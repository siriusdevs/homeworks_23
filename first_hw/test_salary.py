"""Тесты для ДЗ1."""
import unittest

from main import salary_stats

CONST1 = 5125.0
CONST2 = 6000.0
CONST3 = 5250.0
CONST4 = 5500.0
CONST5 = 6000.0
CONST6 = 5500.0


class TestSalaryStatistics(unittest.TestCase):
    """Класс для тестирования функций задания."""

    def test_salary_stats(self):
        """Метод тестирования функции без лимита зарплаты."""
        departments = {
            'Sales': {'John': 5000.0, 'Jane': 6000.0},
            'HR': {'Bob': 4000.0, 'Alice': 5500.0},
        }
        stats = salary_stats(departments)
        self.assertEqual(stats['average'], CONST1)
        self.assertEqual(stats['maximum'], CONST2)
        self.assertEqual(stats['median'], CONST3)

    def test_salary_stats_with_limits(self):
        """Метод тестирования функции с лимитом зарплаты."""
        departments = {
            'Sales': {'John': 5000.0, 'Jane': 6000.0},
            'HR': {'Bob': 4000.0, 'Alice': 5500.0},
        }
        limit = 4100.0

        stats = salary_stats(departments, limit)
        self.assertEqual(stats['average'], CONST4)
        self.assertEqual(stats['maximum'], CONST5)
        self.assertEqual(stats['median'], CONST6)


if __name__ == '__main__':
    unittest.main()
