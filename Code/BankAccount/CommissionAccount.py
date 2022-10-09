import BankAccount
class CommissionAccount(BankAccount):
    """ generated source for class CommissionAccount """
    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(CommissionAccount, self).__init__(customerNumber)

    def getMonthlyReport(self,accountInterest):
        """ generated source for method getMonthlyReport """
        balance = balance + (balance * accountInterest) - 1.1
        return balance

    def withdrawEnough(self, amount):
        """ generated source for method withdrawEnough """
        balance -= amount
        return "You withdrew: " + amount
