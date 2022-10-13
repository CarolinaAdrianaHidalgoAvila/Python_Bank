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
    assert isinstance(bank, Bank)