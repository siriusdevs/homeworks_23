import pytest
from hw1 import company_statistics
# Test case 1: Test with included_departments=None
def test_company_statistics_included_departments_none():
    department1 = ('Отдел1', {'John': 5000, 'Alice': 6000, 'Bob': 4500})
    department2 = ('Отдел2', {'Emma': 5500, 'David': 4800, 'Olivia': 5200})
    result = company_statistics(department1, department2, included_departments=None)
    sorted_salaries, percentage = result
    assert sorted_salaries == [6000, 5500, 5200]
    assert percentage == 53.87

# Test case 2: Test with included_departments=['HR']
def test_company_statistics_included_departments_hr():
    department1 = ('Отдел1', {'John': 5000, 'Alice': 6000, 'Bob': 4500})
    department2 = ('Отдел2', {'Emma': 5500, 'David': 4800, 'Olivia': 5200})
    result = company_statistics(department1, department2, included_departments=['IT'])
    sorted_salaries, percentage = result
    assert sorted_salaries == []
    assert percentage == 0

# Test case 3: Test with included_departments=['IT']
def test_company_statistics_included_departments_it():
    department1 = ('IT_1', {'John': 5000, 'Alice': 6000, 'Bob': 4500})
    department2 = ('IT_2', {'Emma': 5500, 'David': 4800, 'Olivia': 5200})
    result = company_statistics(department1, department2, included_departments=['IT_1', 'IT_2'])
    sorted_salaries, percentage = result
    assert sorted_salaries == [6000, 5500, 5200]
    assert percentage == 53.87

# Test case 4: Test with empty departments
def test_company_statistics_empty_departments():
    result = company_statistics()
    sorted_salaries, percentage = result
    assert sorted_salaries == []
    assert percentage == 0

# Test case 5: Test with single department
def test_company_statistics_single_department():
    department = ('Отдел1', {'John': 5000, 'Alice': 6000, 'Bob': 4500})
    result = company_statistics((department), included_departments=None)
    sorted_salaries, percentage = result
    assert sorted_salaries == [6000, 5000, 4500]
    assert percentage == 100.0
