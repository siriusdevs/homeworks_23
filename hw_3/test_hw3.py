"""Module that tests the main file."""

import pytest

from hw3 import Computer, Screen, Product, Store

NEGATIVE_PRICE = -1

# Default values: name, price, os, processor, diagonal, connector_type
DEFAULT = ('cheese', 300, 'linux', 'intel', 25, 'usb')

COMPUTER_INCORRECT_TYPES_DATA = (
    # Некорректное имя ОС
    (
        'bell', 300, 13, 'intel33',
    ),
    # Некорректное имя процессора
    (
        'bell', 300, 'windows', 3,
    ),
)

SCREEN_INCORRECT_TYPES_DATA = (
    # Некорректно заданый размер
    (
        'atas', 100, '4d', 'hdmi',
    ),
    # Некорректно задано название разъема для подключения
    (
        'atas', 100, 23.6, 4,
    ),
)

# Второй объект в кортеже не Product
STORE_INCORRECT_PRODUCT_DATA = (Screen('asus', 4, 2, 'usb'), 5)

# Всякое разное - и капс, и int | float и все возможные процессоры и ОС
COMPUTER_TEST_DATA = (
    (
        'gigachad', 300, 'WiNdOwS', 'INTELi7',
    ),
    (
        'fulmultigamergbmega', 299.99, 'mac', 'intel',
    ),
    (
        'yyyaaaaa', 0, 'linux', 'amd ryzen 9',
    ),
)

# Всякое разное - и капс, и int | float и все возможные разъемы для подключения
SCREEN_TEST_DATA = (
    (
        'samsam', 300, 25, 'UsB',
    ),
    (
        'atas', 299.99, 24.99, 'hdmi',
    ),
    (
        'next', 1, 1, 'vGa',
    ),
    (
        'nex', 1, 1, 'tHunDerBolt',
    ),
    (
        'ne', 1, 1, 'DISPLAY PORT',
    ),
    (
        'n', 1, 1, 'dvi',
    ),
)

# Набор товаров для дальнейшей работы
TEST_ADD_REMOVE_GET_PRODUCTS = (
    (
        SCREEN_TEST_DATA[0], SCREEN_TEST_DATA[1],
        COMPUTER_TEST_DATA[2], COMPUTER_TEST_DATA[0],
        'Products are: samsam, atas, gigachad',
    ),
)


@pytest.mark.parametrize(
    'screen1, screen2, computer1, computer2, expected',
    TEST_ADD_REMOVE_GET_PRODUCTS,
)
def test_add_remove_get_store(
    screen1: tuple,
    screen2: tuple,
    computer1: tuple,
    computer2: tuple,
    expected: str,
        ):
    """Test add, remove product and return all products.

    Args:
        screen1: tuple - first product.
        screen2: tuple - second product.
        computer1: tuple - third product, for removing.
        computer2: tuple - fourth product, for adding.
        expected: str - result.
    """
    mon1 = Screen(*screen1)
    mon2 = Screen(*screen2)
    pc1 = Computer(*computer1)
    pc2 = Computer(*computer2)
    prod_list = (mon1, mon2, pc1)
    store = Store(prod_list)
    store.add_product(pc2)
    store.remove_product(pc1)
    assert expected == store.get_all_products()


@pytest.mark.parametrize('name, price, diagonal, con_method', SCREEN_TEST_DATA)
def test_screen(name: str, price: int | float, diagonal: int | float, con_method: str):
    """Test creating screen with various data.

    Args:
        name: str - screen name.
        price: int | float - screen price.
        diagonal: int | float - screen diagonal.
        con_method: str - connection type.
    """
    assert Screen(name, price, diagonal, con_method)


@pytest.mark.parametrize('name, price, os, processor', COMPUTER_TEST_DATA)
def test_computer(name: str, price: int | float, os: str, processor: str):
    """Test creating computer with various data.

    Args:
        name: str - computer name.
        price: int | float - computer price.
        os: str - operating system installed on computer.
        processor: str - processor in a computer.
    """
    assert Computer(name, price, os, processor)


@pytest.mark.xfail(reason=ValueError)
def test_negative_price():
    """Try create product with negative price."""
    assert Computer(DEFAULT[0], NEGATIVE_PRICE, DEFAULT[2], DEFAULT[3])


@pytest.mark.xfail(reason=TypeError)
def test_store_wrong_product():
    """Try create store with wrong product in tuple."""
    assert Store(STORE_INCORRECT_PRODUCT_DATA)


@pytest.mark.xfail(reason=TypeError)
def test_screen_wrong_diagonal():
    """Try create screen with incorrect type of diagonal field."""
    assert Screen(*SCREEN_INCORRECT_TYPES_DATA[0])


@pytest.mark.xfail(reason=TypeError)
def test_screen_wrong_con():
    """Try create screen with wrong connector type."""
    assert Screen(*SCREEN_INCORRECT_TYPES_DATA[1])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_os():
    """Try create computer with wrong os type."""
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[0])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_processor():
    """Try create computer with wring processor type."""
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[1])


@pytest.mark.xfail(reason=TypeError)
def test_create_abstract_product():
    """Try create abstract Product."""
    assert Product(DEFAULT[0], DEFAULT[1])