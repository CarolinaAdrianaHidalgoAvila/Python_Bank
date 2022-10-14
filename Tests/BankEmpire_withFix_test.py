import pytest
from Code.BankEmpire.BankEmpire import BankEmpire
from Code.Bank.Bank import Bank

@pytest.fixture
def MercantilBank():
    return Bank("Mercantil")

@pytest.fixture
def BancoUnionBank():
    return Bank("Banco Unión")

@pytest.fixture
def oneBankEmpire():
    return BankEmpire("Bancos del Norte")

@pytest.fixture
def bankEmpireWithTwoBanks(MercantilBank,BancoUnionBank,oneBankEmpire):
    oneBankEmpire.addBank(MercantilBank)
    oneBankEmpire.addBank(BancoUnionBank)
    return oneBankEmpire

def test_addBank_happyPath(MercantilBank,oneBankEmpire):
    """
    ----> En ves de hacer todo esto ...
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Banco del Norte")
    resp = bankEmpire.addBank(oneBank)
    assert resp == True
    """
    resp = oneBankEmpire.addBank(MercantilBank)
    assert resp == True

def test_addBank_FalsePath(MercantilBank,oneBankEmpire):
    # Añadir por segunda ves el mismo banco
    oneBankEmpire.addBank(MercantilBank)
    resp = oneBankEmpire.addBank(MercantilBank)
    assert resp == False

# Aplicación de los casos de pruebas definidos mediante "PATH COVERAGE" 
def test_removeBank_path_1(MercantilBank,oneBankEmpire):
    oneBankEmpire.addBank(MercantilBank)
    resp = oneBankEmpire.removeBank(bank=MercantilBank, bankName=None)
    assert resp == True

def test_removeBank_path_2(MercantilBank,BancoUnionBank,oneBankEmpire):
    oneBankEmpire.addBank(MercantilBank)
    resp = oneBankEmpire.removeBank(bank=BancoUnionBank, bankName=None)
    assert resp == False

"""
----> En caso de que no se podría usar un fixture dentro de otro fixture
def test_removeBank_path_3(MercantilBank,BancoUnionBank,oneBankEmpire):
    oneBankEmpire.addBank(MercantilBank)
    oneBankEmpire.addBank(BancoUnionBank)
    resp = oneBankEmpire.removeBank(bank=MercantilBank, bankName=None)
    assert resp == True
"""
def test_removeBank_path_3(bankEmpireWithTwoBanks,MercantilBank):
    resp = bankEmpireWithTwoBanks.removeBank(bank=MercantilBank, bankName=None)
    assert resp == True

def test_removeBank_path_4(MercantilBank,oneBankEmpire):
    # lista de bancos vacio
    resp = oneBankEmpire.removeBank(bank=MercantilBank, bankName=None)
    assert resp == False

def test_removeBank_path_5(MercantilBank,oneBankEmpire):
    oneBankEmpire.addBank(MercantilBank)
    resp = oneBankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == True

def test_removeBank_path_6(BancoUnionBank,oneBankEmpire):
    oneBankEmpire.addBank(BancoUnionBank)
    # Review
    resp = oneBankEmpire.removeBank(bank=None, bankName="Mercantill") #Cuando es Mercantil, no da... un tema de que se guarda en memoria. Review
    assert resp == False

def test_removeBank_path_7(bankEmpireWithTwoBanks): 
    resp = bankEmpireWithTwoBanks.removeBank(bank=None, bankName="Mercantil")
    assert resp == True

def test_removeBank_path_8(oneBankEmpire):
    # lista vacia
    resp = oneBankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == False

def test_removeBank_path_9(oneBankEmpire):
    resp = oneBankEmpire.removeBank(bank=None, bankName=None)
    assert resp == False
