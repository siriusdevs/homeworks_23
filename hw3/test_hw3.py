"""Tests for hw3."""

import pytest

from hw3 import BankAccount, CheckingAccount, Client, SavingsAccount

ACCOUNT_NUMBER = '123456789'
BANK_BALANCE = 1000.0

CHECK_ACCOUNT_NUM = '987654321'
CHECK_ACCOUNT_BALANCE = 2000.0
CHECK_ACCOUNT_LIMIT = 500.0

SAVE_ACCOUNT_NUM = '135792468'
SAVE_ACCOUNT_BALANCE = 3000.0
SAVE_ACCOUNT_RATE = 0.05

BANK_ACCOUNT1 = BankAccount(ACCOUNT_NUMBER, BANK_BALANCE)
CHECKING_ACCOUNT1 = CheckingAccount(CHECK_ACCOUNT_NUM, CHECK_ACCOUNT_BALANCE, CHECK_ACCOUNT_LIMIT)
SAVINGS_ACCOUNT1 = SavingsAccount(SAVE_ACCOUNT_NUM, SAVE_ACCOUNT_BALANCE, SAVE_ACCOUNT_RATE)

client1 = Client('Till Lindemann', [BANK_ACCOUNT1, CHECKING_ACCOUNT1, SAVINGS_ACCOUNT1])


@pytest.fixture
def bank_account() -> BankAccount:
    """Instantiate and retutn a bank account.

    Returns:
        BankAccount: bank account instantiate with account number and balance
    """
    return BankAccount(ACCOUNT_NUMBER, BANK_BALANCE)


@pytest.fixture
def checking_account() -> CheckingAccount:
    """Instantiate and retutn a checking account.

    Returns:
        CheckingAccount: bank account instantiate with account number, balance and credit_limit
    """
    return CheckingAccount(CHECK_ACCOUNT_NUM, CHECK_ACCOUNT_BALANCE, CHECK_ACCOUNT_LIMIT)


@pytest.fixture
def savings_account() -> SavingsAccount:
    """Instantiate and retutn a saving account.

    Returns:
        SavingsAccount: saving account instantiate with account number, balance and interest_rate
    """
    return SavingsAccount(SAVE_ACCOUNT_NUM, SAVE_ACCOUNT_BALANCE, SAVE_ACCOUNT_RATE)


@pytest.fixture
def client() -> Client:
    """Instantiate and retutn a client.

    Returns:
        Client: client instantiate with name and accounts
    """
    return Client('Till Lindemann', [BANK_ACCOUNT1, CHECKING_ACCOUNT1, SAVINGS_ACCOUNT1])


def test_bank_account_init(bank_account: BankAccount) -> None:
    """Test BankAccount initialization.

    Args:
        bank_account (BankAccount): bank account instantiate with number and balance
    """
    assert bank_account.account_number == ACCOUNT_NUMBER
    assert bank_account.balance == BANK_BALANCE


def test_checking_account_init(checking_account: CheckingAccount) -> None:
    """Test CheckingAccount initialization.

    Args:
        checking_account (CheckingAccount): instantiate with number, balance, limit
    """
    assert checking_account.account_number == CHECK_ACCOUNT_NUM
    assert checking_account.balance == CHECK_ACCOUNT_BALANCE
    assert checking_account.credit_limit == CHECK_ACCOUNT_LIMIT


def test_savings_account_init(savings_account: SavingsAccount) -> None:
    """Test SavingsAccount initialization.

    Args:
        savings_account (SavingsAccount): instantiate number, balance and interest_rate
    """
    assert savings_account.account_number == SAVE_ACCOUNT_NUM
    assert savings_account.balance == SAVE_ACCOUNT_BALANCE
    assert savings_account.interest_rate == SAVE_ACCOUNT_RATE


def test_client_init(client: Client) -> None:
    """Test Client initialization.

    Args:
        client (Client): client instantiate with name and accounts
    """
    assert client.name == 'Till Lindemann'
    assert len(client.accounts) == 3
    assert client.accounts[0].account_number == BANK_ACCOUNT1.account_number
    assert client.accounts[1].account_number == CHECKING_ACCOUNT1.account_number
    assert client.accounts[2].account_number == SAVINGS_ACCOUNT1.account_number
