"""hw3 test module."""


import pytest

from hw3 import Product, Computer, Monitor, Shop

PRODUCT_DATA = (
    (
        'cheese',
        230,
    ),
)
COMPUTER_INCORRECT_TYPES_DATA = (
    (
        123, 123, 'windows', 'intel'
    ),
    (
        'bell', 'three hundred', 'windows', 'intel'
    ),
    (
        'bell', 300, 13, 'intel'
    ),
    (
        'bell', 300, 'windows', 3
    ),
)
MONITOR_INCORRECT_TYPES_DATA = (
    (
        'atas', 100, '4d', 'hdmi'
    ),
    (
        'atas', 100, 23.6, 4
    ),
)
SHOP_INCORRECT_PRODUCT_DATA = (Monitor('asus', 4, 21, 'usb'), 5)
WRONG_OS_NAME_DATA = 'winds'
WRONG_PROC_NAME_DATA = 'amf1100000'
WRONG_CON_NAME_DATA = 'ussr'



@pytest.mark.xfail(reason=ValueError)
def test_os_wrong_name():
    assert Computer('gigachad', 300, WRONG_OS_NAME_DATA, 'intel i7')


@pytest.mark.xfail(reason=ValueError)
def test_proc_wrong_name():
    assert Computer('gigachad', 300, 'Windows', WRONG_PROC_NAME_DATA)


@pytest.mark.xfail(reason=ValueError)
def test_con_wrong_name():
    assert Monitor('samsam', 100, 25, WRONG_CON_NAME_DATA)


@pytest.mark.xfail(reason=TypeError)
def test_shop_wrong_size():
    assert Shop(SHOP_INCORRECT_PRODUCT_DATA)


@pytest.mark.xfail(reason=TypeError)
def test_monitor_wrong_size():
    assert Monitor(*MONITOR_INCORRECT_TYPES_DATA[0])


@pytest.mark.xfail(reason=TypeError)
def test_monitor_wrong_con():
    assert Monitor(*MONITOR_INCORRECT_TYPES_DATA[1])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_name():
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[0])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_price():
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[1])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_os():
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[2])


@pytest.mark.xfail(reason=TypeError)
def test_computer_wrong_processor():
    assert Computer(*COMPUTER_INCORRECT_TYPES_DATA[3])


@pytest.mark.xfail(reason=TypeError)
def test_create_abstract_product(name: str, price: int):
    assert Product(*PRODUCT_DATA[0])