"""Module with tests for the main module."""


import pytest

from hw3 import Computer, Monitor, Store

MSI = 'msi'
WINDOWS = 'windows'
INTEL = 'intel'
HDMI = 'hdmi'
ASUS = 'asus'
LINUX = 'linux'
ACER = 'acer'
LENOVO = 'lenovo'
SAMSUNG = 'samsung'
PRICE1 = 70000
PRICE2 = 65000
PRICE3 = 45000
PRICE4 = 12000
PRICE5 = 15000
PRICE6 = 65000
PRICE7 = 80000
SC_SIZE1 = 27
SC_SIZE2 = 23
SC_SIZE3 = 25


# test Product
def test_title_getter():
    """Getter test for title."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    assert computer.title == MSI


def test_title_setter():
    """Setter test for title."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    computer.title = 'hp'
    assert computer.title == 'hp'


@pytest.mark.xfail(raises=TypeError)
def test_title_setter_invalid_type():
    """Setter test for incorrect title data type."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    computer.title = 20


def test_price_getter():
    """Getter test for price."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    assert computer.price == PRICE1


def test_price_setter():
    """Setter test for price."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    computer.price = PRICE7
    assert computer.price == PRICE7


@pytest.mark.xfail(raises=ValueError)
def test_price_setter_negative_value():
    """Setter test for negative price value."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    computer.price = -56000


@pytest.mark.xfail(raises=TypeError)
def test_price_setter_invalid_type():
    """Setter test for incorrect price data type."""
    computer = Computer(MSI, PRICE1, WINDOWS, INTEL)
    computer.price = '70000'


# test Computer
def test_operate_system_getter():
    """Getter test for operating system."""
    computer = Computer(ASUS, PRICE6, WINDOWS, INTEL)
    assert computer.operate_system == WINDOWS


def test_operate_system_setter():
    """Setter test for operating system."""
    computer = Computer(ASUS, PRICE6, WINDOWS, INTEL)
    computer.operate_system = LINUX
    assert computer.operate_system == LINUX


@pytest.mark.xfail(raises=TypeError)
def test_operate_system_setter_invalid_type():
    """Setter test for incorrect operating system data type."""
    computer = Computer(ASUS, PRICE2, WINDOWS, INTEL)
    computer.operate_system = 7


def test_cpu_getter():
    """Getter test for processor."""
    computer = Computer(ASUS, PRICE2, WINDOWS, INTEL)
    assert computer.cpu == INTEL


def test_cpu_setter():
    """Setter test for processor."""
    computer = Computer(ASUS, PRICE2, WINDOWS, INTEL)
    computer.cpu = 'amd'
    assert computer.cpu == 'amd'


@pytest.mark.xfail(raises=TypeError)
def test_cpu_setter_invalid_type():
    """Setter test for incorrect processor data type."""
    computer = Computer(ASUS, PRICE2, WINDOWS, INTEL)
    computer.cpu = 63


# test Monitor
def test_screen_size_getter():
    """Getter for screen size."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    assert monitor.screen_size == SC_SIZE1


def test_screen_size_setter():
    """Setter for screen size."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    monitor.screen_size = SC_SIZE3
    assert monitor.screen_size == SC_SIZE3


@pytest.mark.xfail(raises=ValueError)
def test_screen_size_setter_negative_value():
    """Setter test for negative screen size value."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    monitor.screen_size = -15


@pytest.mark.xfail(raises=TypeError)
def test_screen_size_setter_invalid_type():
    """Setter test for incorrect screen size data type."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    monitor.screen_size = '27'


def test_type_connection_getter():
    """Getter test for type connection."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    assert monitor.type_connection == 'hdmi'


def test_type_connection_setter():
    """Setter test for type connection."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    monitor.type_connection = 'vga'
    assert monitor.type_connection == 'vga'


@pytest.mark.xfail(raises=TypeError)
def test_type_connection_setter_invalid_type():
    """Setter test for incorrect type connection data type."""
    monitor = Monitor(ACER, PRICE5, SC_SIZE1, HDMI)
    monitor.type_connection = 7.0


# test Store
def test_products_getter():
    """Getter test for products."""
    computer = Computer(LENOVO, PRICE3, WINDOWS, INTEL)
    monitor = Monitor(SAMSUNG, PRICE4, SC_SIZE2, HDMI)
    store = Store([computer, monitor])
    assert store.products == [LENOVO, SAMSUNG]


def test_products_setter():
    """Setter test for products."""
    computer = Computer(LENOVO, PRICE3, WINDOWS, INTEL)
    monitor = Monitor(SAMSUNG, PRICE4, SC_SIZE2, HDMI)
    store = Store([])
    store.products = [computer, monitor]
    assert store.products == [LENOVO, SAMSUNG]


@pytest.mark.xfail(raises=TypeError)
def test_products_setter_non_list():
    """Setter test for incorrect products data type."""
    store = Store()
    store.products = LENOVO


@pytest.mark.xfail(raises=TypeError)
def test_products_setter_non_object_class():
    """Setter test for product out of class."""
    store = Store([])
    store.products = [LENOVO]


def test_add_products():
    """Test add products."""
    computer = Computer(LENOVO, PRICE3, WINDOWS, INTEL)
    monitor = Monitor(SAMSUNG, PRICE4, SC_SIZE2, HDMI)
    computer2 = Computer(ASUS, PRICE3, LINUX, 'amd')
    store = Store([computer, monitor])
    store.add_product(computer2)
    assert store.products == [LENOVO, SAMSUNG, ASUS]


def test_remove_products():
    """Test remove products."""
    computer = Computer(LENOVO, PRICE3, WINDOWS, INTEL)
    monitor = Monitor(SAMSUNG, PRICE4, SC_SIZE2, HDMI)
    store = Store([computer, monitor])
    store.remove_product(monitor)
    assert store.products == [LENOVO]


def test_receive_products():
    """Test receive products."""
    computer = Computer(LENOVO, PRICE3, WINDOWS, INTEL)
    monitor = Monitor(SAMSUNG, PRICE4, SC_SIZE2, HDMI)
    store = Store([computer, monitor])
    store.receive_products()
    assert store.products == [LENOVO, SAMSUNG]


@pytest.mark.xfail(raises=TypeError)
def test_add_products_non_object_class():
    """Test add products out of class."""
    store = Store()
    store.add_product(ASUS)


@pytest.mark.xfail(raises=TypeError)
def test_remove_products_non_object_class():
    """Test remove products out of class."""
    store = Store()
    store.remove_product('hp')


@pytest.mark.xfail(raises=ValueError)
def test_remove_products_absent_store():
    """Test remove products out of Store."""
    monitor = Monitor('dexp', PRICE5, SC_SIZE2, HDMI)
    store = Store([])
    store.remove_product(monitor)
