import pytest
from Code.BankAccount.InvestmentFund import InvestmentFund

def test_getMonthlyReport():
    investment = InvestmentFund(balance=100)
    resp = investment.getMonthlyReport(0.07)
    assert resp == 105.9