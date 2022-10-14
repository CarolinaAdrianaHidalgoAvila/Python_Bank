import re
import pytest
from Code.Bank.Bank import Bank
from Code.Customer.Customer import Customer
from collections.abc import Iterable
from Code.BankAccount.BankAccount import BankAccount
@pytest.fixture
def customers():
    georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
    sebastianCustomer = Customer('Sebastian Curious', 23, 60_000, BankAccount(balance=130))
    carolinaCustomer = Customer('Carolina Curious', 23, 60_000, BankAccount(balance=130))
    luisCustomer = Customer('Luis Curious', 23, 60_000, BankAccount(balance=130))
    return [georgeCustomer,sebastianCustomer,carolinaCustomer,luisCustomer]
@pytest.fixture
def bank(customers):
    bank=Bank("BancoSol",customers)
    return bank
def test_newBank(bank):
    assert bank.name=="BancoSol"
    assert isinstance(bank.customers, Iterable)
    assert len(bank.customers)==4
    assert isinstance(bank, Bank)

def test_addCustomer(bank):
    reneCustomer = Customer('Rene Curious', 23, 60_000, BankAccount(balance=130))
    res = bank.addCustomer(reneCustomer)
    assert len(bank.customers)>4
    assert res == True
def test_addCustomer_fail(bank):
    res = bank.addCustomer(bank.customers[2])
    assert len(bank.customers) == 4
    assert res == False
def test_removeCustomer_path_4(bank):
    resp = bank.removeCustomer(customer=bank.customers[2], customerName=None)
    assert resp == True

def test_removeCustomer_path_5(bank):
    reneCustomer = Customer('Rene Curious', 23, 60_000, BankAccount(balance=130))
    bank.addCustomer(reneCustomer)   
    resp = bank.removeCustomer(customer=None, customerName=bank.customers[2].name)
    assert resp == True

def test_removeCustomer_path_6(bank):
    reneCustomer = Customer('Rene Curious', 23, 60_000, BankAccount(balance=130))
    bank.addCustomer(reneCustomer)
    resp = bank.removeCustomer(customer=None, customerName=bank.customers[4].name) 
    assert resp == True


def test_removeCustomer_path_7(bank,): 
    resp = bank.removeCustomer(customer=None, customerName=bank.customers[2].name)
    assert resp == True

def test_removeCustomer_path_8(bank):
    resp = bank.removeCustomer(customer=None, customerName="Jorge")
    assert resp == False

def test_removeCustomer_path_9(bank):
    resp = bank.removeCustomer(customer=None, customerName=None)
    assert resp == False
