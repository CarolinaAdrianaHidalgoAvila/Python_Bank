import pytest
from Code.BankAccount.CommissionAccount import CommissionAccount

# Arrange
@pytest.fixture
def oneCommisionAccount():
    anyCommisionAccount = CommissionAccount(balance=50)
    return anyCommisionAccount

def test_getMonthlyReport(oneCommisionAccount):
    income = oneCommisionAccount.getMonthlyReport( 0.03)
    assert income == 50.4

def test_withdrawEnough(oneCommisionAccount):
    message = oneCommisionAccount.withdrawEnough(20)
    assert message == "You withdrew: 20"
