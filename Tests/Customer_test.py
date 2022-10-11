import pytest
from Code.BankAccount.BankAccount import BankAccount
from Code.BankAccount.CommissionAccount import CommissionAccount

from Code.Customer.Customer import Customer
def test_newCustomer_vacio():
    georgeCustomer = None
    assert  georgeCustomer is None

def test_newCustomer():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    assert  georgeCustomer is not None
def test_incrementAge():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    incrementAgeG=georgeCustomer.incrementAge(incrementValue=1)
    assert  incrementAgeG == 24
def test_changeIncome():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    change=georgeCustomer.changeIncome(70_000)
    assert change == 70_000
def test_changeBankAccount():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    chanceBack = georgeCustomer.changeBankAccount(CommissionAccount(balance=50))
    assert chanceBack != BankAccount(balance=130)
def test_makeDeposit_positive():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    balance_George=georgeCustomer.makeDeposit(100)
    assert balance_George >= 130
def test_makeDeposit_negative():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    balance_George=georgeCustomer.makeDeposit(-1)
    assert balance_George == 130
