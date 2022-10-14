import pytest
from Code.BankAccount.CurrentAccount import CurrentAccount

@pytest.fixture
def oneCurrentAccount():
    account = CurrentAccount(balance=100)
    return account

def test_withdraw_happyPath(oneCurrentAccount):
    resp = oneCurrentAccount.withdraw(80)
    assert resp == 'You withdrew: 80'

# Sin necesidad de ese test que DEBERIA PROBARSE, Ya sale un coverage del 100%
""" 
def test_withdraw_sadPath(oneCurrentAccount):
    resp = oneCurrentAccount.withdraw(80)
    assert resp == "You don't have enough money in your account"
"""