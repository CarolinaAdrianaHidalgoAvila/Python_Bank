import pytest
from Code.BankAccount.BankAccount import BankAccount


def test_deposit():
    # Arrange
    one_bank_account = BankAccount()
    # Act
    income = one_bank_account.deposit(100)
    # Assert
    assert income == 100

def test_withdraw():
    one_bank_account = BankAccount()
    income = one_bank_account.withdraw(50)
    assert income == -50