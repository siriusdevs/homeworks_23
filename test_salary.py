from salary import salary
import pytest
import random
def test_with_optional_argument():
    assert salary(100000, department1={'Ульяна': 80000, 'Игорь': 85000, 'Виктория': 70000}, 
                  department2={'Алина': 100000, 'Катя': 150000, 'Виктор': 150000}) == (83750.0, 100000, 70000)
def test_without_optional_argument():
    assert salary(department1={'Ульяна': 80000, 'Игорь': 85000, 'Виктория': 70000},
             department2={'Алина': 100000, 'Катя': 150000, 'Виктор': 150000}) == (105833.33, 150000, 100000)
def test_with_other_arguments():
    assert salary(department1 ={'Полина': 293660}, department2 = {'Марина': 293660, 'Виктор': 386929}, 
                  department3= {'Виктория': 293660}, department4 ={'Дмитрий': 293660, 'Екатерина': 386929, 'Сергей': 405264}) == (336251.71, 405264, 293660)
def test_with_other_arguments2():
    assert salary(department1={'Екатерина': 276834, 'Сергей': 442868, 'Виктория': 208196}, department2={'Полина': 276834},
                   department3 = {'Александра': 276834}, department4={'Дмитрий': 276834, 'Евгений': 442868, 'Марина': 208196})== (301183.0, 442868, 276834)