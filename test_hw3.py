"""Test module for Bank Account Management module."""

import pytest

from hw3 import Current_account, Deposit_account, Client


def test_Current_account_creation():
    """Test for Current_account object creation."""
    account = Current_account(10000000000000000001, 0, 5.5)
    assert account.account_number == 10000000000000000001
    assert account.balance == 0
    assert account.credit_limit == 5.5


def test_Deposit_account_creation():
    """Test for Deposit_account object creation."""
    account = Deposit_account(10000000000000000001, 0, 3.5)
    assert account.account_number == 10000000000000000001
    assert account.balance == 0
    assert account.interest_rate == 3.5


def test_Client_creation():
    """Test for Client object creation."""
    deposit_account = Deposit_account(99999999999999999999, 99999999999, 100.0)
    credit_account = Current_account(99999999999999999998, 9999999999900, 1000)
    client = Client('NoskovMichael', [deposit_account, credit_account])
    assert client.name == 'NoskovMichael'
    assert client.accounts == [deposit_account, credit_account]


def transactions_test():
    """Test for successful completion of transactions."""
    deposit_account = Deposit_account(99999999999999999999, 99999999999, 100.0)
    credit_account = Current_account(99999999999999999998, 10, 1000)
    client = Client('NoskovMichael', [deposit_account, credit_account])

    client.deposit_money(99999999999999999999, 1)
    assert client.accounts[0].balance == 100000000000
    client.withdraw_money(99999999999999999999, 2)
    assert client.accounts[0].balance == 99999999998

    client.withdraw_money(99999999999999999998, 1010)
    assert client.accounts[0].balance == -1000

    with pytest.raises(ValueError):
        client.withdraw_money(99999999999999999998, 1010)

    with pytest.raises(ValueError):
        client.deposit_money(99999999999999999998, -1010)


def test_creation_raises_error():
    """Test for wrong arguments."""
    with pytest.raises(ValueError):
        Current_account(1000000000, 0, 5.5)
    with pytest.raises(TypeError):
        Current_account(10000000000000000001, '0', 5.5)
    with pytest.raises(TypeError):
        Current_account(10000000000000000001, 0, '5.5')
