import BankAccount
class NoCommissionAccount(BankAccount):
    """ generated source for class NoCommissionAccount """
    def __init__(self, acctType='Savings', balance=0):
        """ generated source for method __init__ """
        BankAccount.__init__(self, acctType, balance)

    def getMonthlyReport(self, accountInterest):
        """ generated source for method getMonthlyReport """
        self.balance = self.balance + (self.balance * accountInterest)
        return self.balance