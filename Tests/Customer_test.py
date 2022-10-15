import pytest

from Code.BankAccount.BankAccount import BankAccount
from Code.BankAccount.CommissionAccount import CommissionAccount

from Code.Customer.Customer import Customer

@pytest.fixture
def customer():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    return georgeCustomer

def test_customer_new(customer):
    assert customer.name == "George Curious"
    assert customer.age == 23
    assert isinstance(customer, Customer)

def test_newCustomer():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    assert  georgeCustomer is not None
def test_incrementAge(customer):
    incrementAgeG=customer.incrementAge(incrementValue=1)
    assert  incrementAgeG == 24
def test_changeIncome(customer):
    change=customer.changeIncome(70_000)
    assert change == 70_000
def test_changeBankAccount(customer):
    chanceBack = customer.changeBankAccount(CommissionAccount(balance=50))
    assert chanceBack != BankAccount(balance=130)
def test_makeDeposit_positive(customer):
    balance_George=customer.makeDeposit(100)
    assert balance_George >= 130

def test_makeWithdrawal_1(customer):
    withdrawal= customer.makeWithdrawal(-1)
    assert withdrawal ==  130
def test_makeWithdrawal_2(customer):
    
    withdrawal= customer.makeWithdrawal(120)
    assert withdrawal == 10
def test_makeWithdrawal_3(customer):
    
    withdrawal= customer.makeWithdrawal(135)
    assert withdrawal == 130

def test_name(customer):
    with pytest.raises(Exception):
        assert customer.name("George Curious")

def test_makeDeposit_negative(customer):
    with pytest.raises(Exception):
        assert customer.makeDeposit(0)

