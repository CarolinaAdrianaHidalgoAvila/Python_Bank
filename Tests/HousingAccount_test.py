import pytest
from Code.BankAccount.HousingAccount import HousingAccount


# Aqui esta vacio ¡¡ , guardarlo para la demo
def test_withdraw_happyPath():
    houseAccount = HousingAccount(balance=100)
    assert houseAccount is not None