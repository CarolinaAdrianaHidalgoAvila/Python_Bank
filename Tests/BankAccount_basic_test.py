import pytest
from Code.BankAccount.BankAccount import BankAccount


def test_deposit():
    # Arrange
    one_bank_account = BankAccount(balance=100)
    # Act
    income = one_bank_account.deposit(100)
    # Assert
    assert income == 200

def test_withdraw():
    one_bank_account = BankAccount(balance=100)
    income = one_bank_account.withdraw(50)
    assert income == 50