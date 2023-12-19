"""Tests for my hw3."""
import pytest

from hw3 import Client, CurrentAccount, SavingsAccount


def test_deposit_money():
    """Test for the deposit."""
    client = Client('John Cena', [CurrentAccount(123, 1000, 500)])
    assert client.put_money(123, 200) == 'The money was successfully deposited.'


def test_withdraw_money():
    """Test for the withdrawn."""
    client = Client('John Doe', [CurrentAccount(123, 1000, 500)])
    assert client.take_money(123, 200) == 'The money was successfully withdrawn.'


def test_valid_type_money():
    """Test for the money(str) with numbers."""
    client = Client('John Cena', [CurrentAccount(123, 1000, 500)])
    assert client.put_money(123, '200') == 'The money was successfully deposited.'


def test_account_not_found():
    """Test for the wrong account number."""
    client = Client('John Doe', [CurrentAccount(121233, 1000, 500)])
    assert client.put_money(456, 200) == 'The account was not found'


def test_withdraw_money_negative_balance():
    """Test the scenario where withdrawing too much money leads to a negative balance."""
    client = Client('John Doe', [CurrentAccount(123, 1000, 500)])
    assert client.take_money(123, 1200) == 'The transfer did not take place.'
    assert client.accounts[0].balance == 1000


def test_invalid_money():
    """Test for the invalid type of money."""
    with pytest.raises(ValueError, match='Invalid money. Please provide a valid numeric value.'):
        client = Client('John Cena', [CurrentAccount(123, 1000, 500)])
        client.put_money(123, 'inval')


def test_negative_args_account():
    """Test for the negative arguments."""
    with pytest.raises(ValueError, match='Value is expected to be positive.'):
        Client('John John', [SavingsAccount(1029, 1241, -0.5)])
    with pytest.raises(ValueError, match='Value is expected to be positive.'):
        Client('John John', [SavingsAccount(-1029, 1241, 0.5)])
    with pytest.raises(ValueError, match='Value is expected to be positive.'):
        Client('John John2', [SavingsAccount(1029, -1241, 0.5)])


def test_wrong_type_args():
    """Test for the wrong type of arguments."""
    with pytest.raises(TypeError, match='Value is expected to be int.'):
        Client('John John3', [SavingsAccount('1029', 1241, 0.5)])
    with pytest.raises(TypeError, match='Value is expected to be int.'):
        Client('John John3', [SavingsAccount(1029.5, 1241, 0.5)])
    with pytest.raises(TypeError, match='Name is expected to be str.'):
        Client(133123, [SavingsAccount(1029, 1241, 0.5)])
