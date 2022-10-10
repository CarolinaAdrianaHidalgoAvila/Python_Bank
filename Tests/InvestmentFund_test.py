import pytest
from Code.BankAccount.InvestmentFund import InvestmentFund

def test_withdraw():
    investment = InvestmentFund(balance=100)
    resp = investment.withdraw(20)
    assert resp == "You withdrew: 20"

def test_getIsBlocked():
    investment = InvestmentFund(balance=100)
    resp = investment.getIsBlocked()
    assert resp == False

def test_equalCredit():
    investment = InvestmentFund(balance=100)
    resp = investment.equalCredit(10)
    assert resp == 'You withdrew: 10 and your account has been blocked'
