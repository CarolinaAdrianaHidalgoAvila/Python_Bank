import pytest
from Code.BankEmpire.BankEmpire import BankEmpire
from Code.Bank.Bank import Bank

def test_addBank_happyPath():
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Banco del Norte")
    resp = bankEmpire.addBank(oneBank)
    assert resp == True

def test_addBank_FalsePath():
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Banco del Norte", [oneBank])
    resp = bankEmpire.addBank(oneBank)
    assert resp == False

# Aplicación de los casos de pruebas definidos mediante "PATH COVERAGE" 

def test_removeBank_path_1():
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Banco del Norte", [oneBank])
    bankEmpire.addBank(oneBank)
    resp = bankEmpire.removeBank(bank=oneBank, bankName=None)
    assert resp == True

def test_removeBank_path_2():
    oneBank = Bank("Mercantil")
    anotherBank = Bank("Banco Unión")
    bankEmpire = BankEmpire( "Bancos del Norte", [oneBank])
    bankEmpire.addBank(oneBank)
    resp = bankEmpire.removeBank(bank=anotherBank, bankName=None)
    assert resp == False

def test_removeBank_path_3():
    oneBank = Bank("Mercantil")
    anotherBank = Bank("Banco Unión")
    bankEmpire = BankEmpire( "Bancos del Norte", [oneBank])
    bankEmpire.addBank(oneBank)
    bankEmpire.addBank(anotherBank)
    resp = bankEmpire.removeBank(bank=oneBank, bankName=None)
    assert resp == True

def test_removeBank_path_4():
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Bancos del Norte") # lista de bancos vacio
    resp = bankEmpire.removeBank(bank=oneBank, bankName=None)
    assert resp == False

def test_removeBank_path_5():
    oneBank = Bank("Mercantil")
    bankEmpire = BankEmpire( "Bancos del Norte")
    bankEmpire.addBank(oneBank)
    resp = bankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == True

def test_removeBank_path_6():
    oneBank = Bank("Banco Unión")
    bankEmpire = BankEmpire( "Bancos del Norte")
    bankEmpire.addBank(oneBank)
    # Review
    resp = bankEmpire.removeBank(bank=None, bankName="Mercantill") #Cuando es Mercantil, no da... un tema de que se guarda en memoria. Review
    assert resp == False

def test_removeBank_path_7(): 
    oneBank = Bank("Mercantil")
    anotherBank = Bank("Banco Unión")
    bankEmpire = BankEmpire( "Bancos del Norte")
    bankEmpire.addBank(oneBank)
    bankEmpire.addBank(anotherBank)
    resp = bankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == True

def test_removeBank_path_8():
    bankEmpire = BankEmpire( "Bancos del Norte") # lista vacia
    resp = bankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == False

def test_removeBank_path_8():
    bankEmpire = BankEmpire( "Bancos del Norte") # lista vacia
    resp = bankEmpire.removeBank(bank=None, bankName="Mercantil")
    assert resp == False

def test_removeBank_path_9():
    bankEmpire = BankEmpire( "Bancos del Norte")
    resp = bankEmpire.removeBank(bank=None, bankName=None)
    assert resp == False
