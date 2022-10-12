import pytest
from Code.HighNetWorthCustomer.HighNetWorthCustomer import HighNetWorthCustomer

def test_changePreferredInvestment():
    costumerStart = HighNetWorthCustomer(name='sebas',age=21,income=500,acct=5050,preferredInvestment='videojuegos',birthday='28/04' )
    income = costumerStart.changePreferredInvestment(newPreferredInvestment='videojuegos')
    assert income=='videojuegos'

