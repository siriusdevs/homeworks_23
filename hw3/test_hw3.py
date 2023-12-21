"""hw3 test module."""

import pytest

from hw3 import Computer, Monitor, Product, Shop

NEGATIVE_PRICE = -1

# Default values: name, price, os, processor, size, connector_type
DEFAULT = ('cheese', 300, 'ubuntu', 'intel', 25, 'usb')

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

MONITOR_INCORRECT_TYPES_DATA = (
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
SHOP_INCORRECT_PRODUCT_DATA = (Monitor('asus', 4, 2, 'usb'), 5)

# Всякое разное - и капс, и int | float и все возможные процессоры и ОС
COMPUTER_TEST_DATA = (
    (
        'gigachad', 300, 'WiNdOwS', 'INTELi7',
    ),
    (
        'fulmultigamergbmega', 299.99, 'macos', 'intel',
    ),
    (
        'yyyaaaaa', 0, 'UBUNTu', 'amd ryzen 9',
    ),
)

# Всякое разное - и капс, и int | float и все возможные разъемы для подключения
MONITOR_TEST_DATA = (
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
        MONITOR_TEST_DATA[0], MONITOR_TEST_DATA[1],
        COMPUTER_TEST_DATA[2], COMPUTER_TEST_DATA[0],
        'Products are: samsam, atas, gigachad',
    ),
)


@pytest.mark.parametrize(
    'monitor1, monitor2, computer1, computer2, expected',
    TEST_ADD_REMOVE_GET_PRODUCTS,
)
def test_add_remove_get_shop(
    monitor1: tuple,
    monitor2: tuple,
    computer1: tuple,
    computer2: tuple,
    expected: str,
        ):
    """Test add, remove product and return all products.

    Args:
        monitor1: tuple - first product.
        monitor2: tuple - second product.
        computer1: tuple - third product, for removing.
        computer2: tuple - fourth product, for adding.
        expected: str - result.
    """
    mon1 = Monitor(*monitor1)
    mon2 = Monitor(*monitor2)
    pc1 = Computer(*computer1)
    pc2 = Computer(*computer2)
    prod_list = (mon1, mon2, pc1)
    shop = Shop(prod_list)
    shop.add_product(pc2)
    shop.remove_product(pc1)
    assert expected == shop.get_all_products()


@pytest.mark.parametrize('name, price, size, con_type', MONITOR_TEST_DATA)
def test_monitor(name: str, price: int | float, size: int | float, con_type: str):
    """Test creating monitor with various data.

    Args:
        name: str - monitor name.
        price: int | float - monitor price.
        size: int | float - monitor diagonal size.
        con_type: str - connection type.
    """
    assert Monitor(name, price, size, con_type)


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
def test_shop_wrong_product():
    """Try create shop with wrong product in tuple."""
    assert Shop(SHOP_INCORRECT_PRODUCT_DATA)


@pytest.mark.xfail(reason=TypeError)
def test_monitor_wrong_size():
    """Try create monitor with incorrect type of size field."""
    assert Monitor(*MONITOR_INCORRECT_TYPES_DATA[0])


@pytest.mark.xfail(reason=TypeError)
def test_monitor_wrong_con():
    """Try create monitor with wrong connector type."""
    assert Monitor(*MONITOR_INCORRECT_TYPES_DATA[1])


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
