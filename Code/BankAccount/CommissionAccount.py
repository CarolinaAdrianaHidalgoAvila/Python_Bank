class CommissionAccount(Account):
    """ generated source for class CommissionAccount """
    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(CommissionAccount, self).__init__(customerNumber)

    def getMonthlyReport(self):
        """ generated source for method getMonthlyReport """
        balance = balance + (balance * accountInterest) - Constants.COMMISSION
        return balance

    def withdrawEnough(self, amount):
        """ generated source for method withdrawEnough """
        balance -= amount
        return Messages.WITHDREW + Double.toString(amount)
