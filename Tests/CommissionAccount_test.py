import pytest
from Code.BankAccount.BankAccount import BankAccount
from Code.BankAccount.CommissionAccount import CommissionAccount

def test_getMonthlyReport():
    commission = CommissionAccount(balance=50)
    income = commission.getMonthlyReport( 0.03)
    assert income == 50.4

def test_withdrawEnough():
    commission = CommissionAccount(balance=50)
    message = commission.withdrawEnough(20)
    assert message == "You withdrew: 20"