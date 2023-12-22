"""Module that tests the main file."""
import hw3
import pytest

ERORR_DATA_COMPUTER = (
    ('bell', 9112, 98, 'qpps22'),
    ('bell', 12, 'weroff', 2),
)


ERORR_DATA_SCREEN = (
    (
        'pok', 20, '2d', 'ddfg',
    ),
    (
        'pok', 20, 15, 9, 4,
    ),
)

COMPUTER_TEST_DATA = (
    (
        'mypc', 55000, 'liNUX', 'INTELi3',
    ),
    (
        'EVM-1', 29999.01, 'mac', 'intel',
    ),
    (
        'siriuspc', 10, 'winDows', 'amd',
    ),
)

SCREEN_TEST_DATA = (
    (
        'dexp', 20, 13456, 'vgA',
    ),
    (
        'logiteh', 1, 0.1, 'uSB',
    ),
    (
        'uiopikj', 0, 34987, 'vGa',
    ),
    (
        'ytr', 999999.9999, 0, 'usb',
    ),
    (
        'werty', 8766.9, 33, 'DISPLAY PORT',
    ),
    (
        '12345', 33, 34, 'dvi',
    ),
)

ITEM_CONTROL_TEST = (
    (
        SCREEN_TEST_DATA[0], SCREEN_TEST_DATA[1],
        COMPUTER_TEST_DATA[2], COMPUTER_TEST_DATA[0],
        'Products are: dexp, logiteh, mypc',
    ),
)

WRONG_PRICE = -20

STANDARD_SPEC = ('cheese', 7800, 'linux', 'intel', 16, 'usb')
# Standard values: name, price, os, processor, diag, connection_method


@pytest.mark.xfail(reason=ValueError)
def test_wrong_price():
    """Attempt to create a product with a negative price."""
    assert hw3.Computer(STANDARD_SPEC[0], WRONG_PRICE, STANDARD_SPEC[2], STANDARD_SPEC[3])


@pytest.mark.xfail(reason=TypeError)
def test_screen_incorrect_diagonal():
    """Attempt to create a screen with an incorrect type of diagonal field."""
    assert hw3.Screen(*ERORR_DATA_SCREEN[0])


@pytest.mark.xfail(reason=TypeError)
def test_screen_incorrect_connection():
    """Attempt to create screen with incorrect connector type."""
    assert hw3.Screen(*ERORR_DATA_SCREEN[1])


@pytest.mark.xfail(reason=TypeError)
def test_computer_incorrect_os():
    """Attempt to create computer with incorrect os type."""
    assert hw3.Computer(*ERORR_DATA_COMPUTER[0])


@pytest.mark.xfail(reason=TypeError)
def test_computer_incorrect_processor():
    """Attempt to create computer with incorrect processor type."""
    assert hw3.Computer(*ERORR_DATA_COMPUTER[1])


@pytest.mark.xfail(reason=TypeError)
def test_create_abstract_class():
    """Attempt to create object from abstract class."""
    assert hw3.Product(STANDARD_SPEC[0], STANDARD_SPEC[1])


@pytest.mark.parametrize(
    'screen1, screen2, computer1, computer2, expected',
    ITEM_CONTROL_TEST,
)
def test_crud_store(
    screen1: tuple,
    screen2: tuple,
    computer1: tuple,
    computer2: tuple,
    expected: str,
        ):
    """Test add, remove and return all products.

    Args:
        screen1: tuple - 1 product.
        screen2: tuple - 2 product.
        computer1: tuple - 3 product, for remove.
        computer2: tuple - 4 product, for add.
        expected: str - result.
    """
    mon1 = hw3.Screen(*screen1)
    mon2 = hw3.Screen(*screen2)
    pc1 = hw3.Computer(*computer1)
    pc2 = hw3.Computer(*computer2)
    prod_list = (mon1, mon2, pc1)
    store = hw3.Store(prod_list)
    store.add_product(pc2)
    store.remove_product(pc1)
    assert expected == store.get_all_products()


@pytest.mark.parametrize('name, price, os, processor', COMPUTER_TEST_DATA)
def test_computer(name: str, price: int | float, os: str, processor: str):
    """Test creating computer with various data.

    Args:
        name: str - computer name.
        price: int | float - computer price.
        os: str - operating system installed on computer.
        processor: str - processor in a computer.
    """
    assert hw3.Computer(name, price, os, processor)
