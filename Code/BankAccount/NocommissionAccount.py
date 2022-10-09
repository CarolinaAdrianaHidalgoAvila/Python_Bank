import BankAccount
class NoCommissionAccount(BankAccount):
    """ generated source for class NoCommissionAccount """
    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(NoCommissionAccount, self).__init__(customerNumber)

    def getMonthlyReport(self, accountInterest):
        """ generated source for method getMonthlyReport """
        balance = balance + (balance * accountInterest)
        return balance