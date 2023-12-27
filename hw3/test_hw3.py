"""Tests for hw3."""

from typing import Any

import pytest

import hw3

PRICE_ONE = 623
PRICE_TWO = 324
PRICE_FREE = 99.9
PRICE_FOUR = 999
PRICE_FIVE = 12.3

CLIENT1 = hw3.Client('Danil')
CLIENT2 = hw3.Client('Polina')
DISH1 = hw3.Dish('Meat', PRICE_ONE)
DISH2 = hw3.Dish('Salad', PRICE_TWO)
DISH3 = hw3.Dish('Ice Cream', PRICE_FREE)
ORDER1 = hw3.Order(CLIENT1, [DISH1, DISH2])
ORDER2 = hw3.Order(CLIENT2, [DISH3])
RESTAURANT = hw3.Restaurant([ORDER1, ORDER2], [DISH1, DISH2, DISH3], [DISH1, DISH2])

CLASS_NAME = RESTAURANT.__class__.__name__
AVAIL_DISHES = RESTAURANT.available_dishes
DISHES = RESTAURANT.all_dishes
RESTR_STR = f'Menu {CLASS_NAME}: {DISHES}, available dishes: {AVAIL_DISHES}'
A_STR = 'a'


TEST_DATA = (
    (
        ORDER1,
        f'Order recipient: {CLIENT1} composition of the order: {ORDER1.dishes}',
        ),
    (
        RESTAURANT,
        RESTR_STR,
    ),
    (
        DISH1,
        'Dish with price: 623',
    ),
)


@pytest.mark.parametrize('given, expected', TEST_DATA)
def test_restaurant(given: Any, expected: str):
    """Test for valid Restaurant instance creation.

    Args:
        given: Any - input data.
        expected: str - awaited result.
    """
    assert str(given) == expected


@pytest.mark.xfail
def test_dish_fail_name():
    """First negative test."""
    hw3.Dish(1, PRICE_FIVE)


@pytest.mark.xfail
def test_dish_fail_price():
    """Second negative test."""
    hw3.Dish('Name', 'aaaaaa')


@pytest.mark.xfail
def test_order_fail():
    """Third negative test."""
    hw3.Order(A_STR, 'asd')


@pytest.mark.xfail
def test_restraunt_fail():
    """Fourth negative test."""
    hw3.Restaurant(
        [hw3.Order(hw3.Client('Name'), [hw3.Dish(A_STR, 8)])],
        [A_STR],
        [hw3.Dish(A_STR, PRICE_FOUR)],
    )
