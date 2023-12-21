"""Test module for Bank Account Management module."""
import pytest

from hw3 import Client, Current_account, Deposit_account

DEPOSIT_ACCOUNT_NUMBER = 99999999999999999999
CREDIT_ACCOUNT_NUMBER = 99999999999999999998

deposit_account = Deposit_account(DEPOSIT_ACCOUNT_NUMBER, 99999999999, 100.0)
credit_account = Current_account(CREDIT_ACCOUNT_NUMBER, 10, 1000)


def test_current_account_creation():
    """Test for Current_account object creation."""
    account = Current_account(10000000000000000001, 0, 55)
    assert account.account_number == 10000000000000000001
    assert account.balance == 0
    assert account.credit_limit == 55


def test_deposit_account_creation():
    """Test for Deposit_account object creation."""
    account = Deposit_account(10000000000000000001, 0, 3)
    assert account.account_number == 10000000000000000001
    assert account.balance == 0
    assert account.interest_rate == 3


def test_client_creation():
    """Test for Client object creation."""
    client = Client('NoskovMichael', [deposit_account, credit_account])
    assert client.name == 'NoskovMichael'
    assert client.accounts == [deposit_account, credit_account]


def transactions_test():
    """Test for successful completion of transactions."""
    client = Client('NoskovMichael', [deposit_account, credit_account])

    client.deposit_money(DEPOSIT_ACCOUNT_NUMBER, 1)
    assert client.accounts[0].balance == 100000000000
    client.withdraw_money(DEPOSIT_ACCOUNT_NUMBER, 2)
    assert client.accounts[0].balance == 99999999998

    client.withdraw_money(CREDIT_ACCOUNT_NUMBER, 1010)
    assert client.accounts[0].balance == -1000

    with pytest.raises(ValueError):
        client.withdraw_money(CREDIT_ACCOUNT_NUMBER, 1010)

    with pytest.raises(ValueError):
        client.deposit_money(CREDIT_ACCOUNT_NUMBER, -1010)


def test_creation_raises_error():
    """Test for wrong arguments."""
    with pytest.raises(ValueError):
        Current_account(1000000000, 0, 5.5)
    with pytest.raises(TypeError):
        Current_account(DEPOSIT_ACCOUNT_NUMBER, '0', 5.5)
    with pytest.raises(TypeError):
        Current_account(DEPOSIT_ACCOUNT_NUMBER, 0, '5.5')
