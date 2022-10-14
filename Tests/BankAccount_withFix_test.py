import pytest
from Code.BankAccount.BankAccount import BankAccount

# Arrange
@pytest.fixture
def oneBankAccount():
    georgeBankAccout = BankAccount(balance=100)
    return georgeBankAccout

def test_deposit(oneBankAccount):
    income = oneBankAccount.deposit(100)
    assert income == 200

def test_withdraw(oneBankAccount):
    income = oneBankAccount.withdraw(50)
    assert income == 50