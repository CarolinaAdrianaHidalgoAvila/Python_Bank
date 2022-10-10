import pytest
from Code.BankAccount.BankAccount import BankAccount
from Code.Customer.Customer import Customer
def test_newCustomer_vacio():
    georgeCustomer = None
    assert  georgeCustomer is None

def test_newCustomer():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    assert  georgeCustomer is not None