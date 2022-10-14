import pytest
from Code.BankAccount.InvestmentFund import InvestmentFund

@pytest.fixture
def investment():
    investment = InvestmentFund(balance=100)
    return investment

def test_withdraw(investment):
    resp = investment.withdraw(20)
    assert resp == "You withdrew: 20"

def test_getIsBlocked(investment):
    resp = investment.getIsBlocked()
    assert resp == False

def test_equalCredit(investment):
    resp = investment.equalCredit(10)
    assert resp == 'You withdrew: 10 and your account has been blocked'