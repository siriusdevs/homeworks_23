"""Module that tests the main file."""

from hw1 import company_salary_stats

stats_eq_zero = {'average': 0, 'max': 0, 'median': 0}


def test_company_salary_stats():
    """
    Test function for the company_salary_stats function.

    This test case checks if the function returns the correct statistics when the "IT"
    department is excluded, and the salaries for "HR" and "IT" are provided.
    """
    test_result = company_salary_stats(
        ('IT',), HR={'Johin': 500, 'Emma': 550}, IT={'Mike': 8999999, 'Sara': 10000},
        )
    assert test_result == {'average': 525, 'max': 550, 'median': 525}


def test_no_salaries():
    """
    This test verifies the behavior of company_salary_stats when no salaries are provided.

    It checks if the function returns the expected dictionary with average, maximum,
    and median salaries all being 0.
    """
    stats = company_salary_stats()
    assert stats == stats_eq_zero


def test_empty_department():
    """
    This test checks companysalarystats with no employees in any department.

    It checks if the function returns the expected dictionary with average,
    maximum, and median salaries all being 0.
    """
    stats = company_salary_stats(sales={}, marketing={}, finance={})
    assert stats == stats_eq_zero


def test_no_employees():
    """
    This test checks company_salary_stats when no employees are present in any department.

    It checks if the function returns the expected dictionary with average,
    maximum, and median salaries all being 0.
    """
    stats = company_salary_stats(sales={}, marketing={}, finance={})
    assert stats == stats_eq_zero


def test_single_department():
    """
    This test checks companysalarystats with only one department of employees and salaries.

    It checks if the function returns the expected statistics for the single
    department provided.
    """
    stats = company_salary_stats(sales={'Johni': 3000, 'Riko': 3500, 'Ann': 3200})
    assert stats == {'average': 3233.33, 'max': 3500, 'median': 3200}


def test_exclude_all_departments():
    """
    This test verifies the behavior of company_salary_stats when all departments are excluded.

    It checks if the function returns the expected dictionary with average, maximum, and median
    salaries all being 0.
    """
    stats = company_salary_stats(
        exclude_departments=('sales', 'marketing', 'finance'),
        sales={'John': 3000, 'Alice': 3500, 'Eve': 3200},
        marketing={'Bob': 2800, 'Carol': 3100}, finance={'Dave': 4000, 'Frank': 4200},
        )
    assert stats == stats_eq_zero


def test_zero_salaries():
    """
    This test verifies the behavior of company_salary_stats when all employees have zero salaries.

    It checks if the function returns the expected dictionary with average, maximum,
    and median salaries all being 0.
    """
    stats = company_salary_stats(
        sales={'Lara': 0, 'Adel': 0, 'Mishel': 0},
        marketing={'Boby': 0, 'Carolina': 0}, finance={'Dave': 0, 'Frank': 0},
        )
    assert stats == stats_eq_zero
