import CommissionAccount
class CurrentAccount(CommissionAccount):
    """ generated source for class CurrentAccount """
    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(CurrentAccount, self).__init__(customerNumber)
        accountInterest = 0.11
       

    def withdraw(self, amount, balance):
        """ generated source for method withdraw """
        resp = "You don't have enough money in your account"
        resp = CommissionAccount.withdrawEnough(amount) if balance >= amount else resp
        return resp
