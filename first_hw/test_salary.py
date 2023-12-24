import unittest
from main import salary_stats


class TestSalaryStatistics(unittest.TestCase):
    def test_salary_stats(self):
        departments = {
            'Sales': {'John': 5000.0, 'Jane': 6000.0},
            'HR': {'Bob': 4000.0, 'Alice': 5500.0},
        }
        stats = salary_stats(departments)
        self.assertEqual(stats['average'], 5125.0)
        self.assertEqual(stats['maximum'], 6000.0)
        self.assertEqual(stats['median'], 5250.0)

    def test_salary_stats_with_limits(self):
        departments = {
            'Sales': {'John': 5000.0, 'Jane': 6000.0},
            'HR': {'Bob': 4000.0, 'Alice': 5500.0},
        }
        limit = 4100.0

        stats = salary_stats(departments, limit)
        self.assertEqual(stats['average'], 5500.0)
        self.assertEqual(stats['maximum'], 6000.0)
        self.assertEqual(stats['median'], 5500.0)


if __name__ == '__main__':
    unittest.main()
