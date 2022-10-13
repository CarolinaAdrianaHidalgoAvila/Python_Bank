import pytest
from Code.BankAccount.NocommissionAccount import NoCommissionAccount

def test_getMonthlyReport():
    nocommission = NoCommissionAccount(balance=100)
    resp = nocommission.getMonthlyReport(0.07)
    assert resp == 107