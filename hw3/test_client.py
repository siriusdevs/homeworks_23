"""Module include tests on Client and Dish classes."""
import pytest

from client import Client

names_of_clients = ('Albert', 'Artem')


@pytest.mark.parametrize('name', names_of_clients)
def test_clients_ptrs(name: str) -> None:
    """Check parameters.

    Args:
        name (str): name of client
    """
    assert Client(name).name == name


@pytest.mark.xfail(raises=TypeError)
def test_client_invalid():
    """Check setter work."""
    with pytest.raises(TypeError):
        Client(9)
