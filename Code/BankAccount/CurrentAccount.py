from Code.BankAccount.CommissionAccount import CommissionAccount
class CurrentAccount(CommissionAccount):
    """ generated source for class CurrentAccount """
    def __init__(self,  acctType='Savings', balance=0):
        """ generated source for method __init__ """
        CommissionAccount.__init__(self,acctType, balance)
        accountInterest = 0.11
       

    def withdraw(self, amount):
        """ generated source for method withdraw """
        resp = "You don't have enough money in your account"
        resp = self.withdrawEnough(amount) if self.balance >= amount else resp
        return resp
