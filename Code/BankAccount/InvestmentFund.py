from tkinter import Message
import CommissionAccount
class InvestmentFund(CommissionAccount):
    """ generated source for class InvestmentFund """
    isBlocked = bool()

    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(InvestmentFund, self).__init__(customerNumber)
        accountInterest = 0.33
        self.isBlocked = False

    def withdraw(self, amount, balance):
        """ generated source for method withdraw """
        resp = "You don't have enough money in your account"
        resp = self.withdrawWithCredit(amount) if balance + 600 >= amount else resp if not self.getIsBlocked() else "Your account is blocked"
        return resp

    def getIsBlocked(self):
        """ generated source for method getIsBlocked """
        return self.isBlocked

    def equalCredit(self, amount):
        """ generated source for method equalCredit """
        self.isBlocked = True
        return CommissionAccount.withdrawEnough(amount) + " and your account has been blocked"

    def withdrawWithCredit(self, amount, balance):
        """ generated source for method withdrawWithCredit """
        resp ="You don't have enough money in your account"
        resp = CommissionAccount.withdrawEnough(amount) if balance + 600 > amount else self.equalCredit(amount)
        return resp