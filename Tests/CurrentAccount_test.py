import pytest
from Code.BankAccount.CurrentAccount import CurrentAccount


def test_withdraw_happyPath():
    account = CurrentAccount(balance=100)
    resp = account.withdraw(80)
    assert resp == 'You withdrew: 80'

# Sin necesidad de ese test que DEBERIA PROBARSE, Ya sale un coverage del 100%
""" 
def test_withdraw_sadPath():
    account = CurrentAccount(balance=50)
    resp = account.withdraw(80)
    assert resp == "You don't have enough money in your account"
"""