from Code.BankAccount.BankAccount import BankAccount
class CommissionAccount(BankAccount):
    """ generated source for class CommissionAccount """
    def __init__(self, acctType='Savings', balance=0):
        """ generated source for method __init__ """
        BankAccount.__init__(self,acctType, balance)
        # super(CommissionAccount, self).__init__(customerNumber)

    def getMonthlyReport(self,accountInterest):
        """ generated source for method getMonthlyReport """
        self.balance = self.balance + (self.balance * accountInterest) - 1.1
        return self.balance

    def withdrawEnough(self, amount):
        """ generated source for method withdrawEnough """
        self.balance -= amount
        return "You withdrew: " + str(amount)
