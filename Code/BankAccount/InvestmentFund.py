from tkinter import Message
import CommissionAccount
class InvestmentFund(CommissionAccount):
    """ generated source for class InvestmentFund """
    isBlocked = bool()

    def __init__(self, acctType='Savings', balance=0):
        """ generated source for method __init__ """
        CommissionAccount.__init__(self,acctType, balance)
        accountInterest = 0.33
        self.isBlocked = False

    def withdraw(self, amount):
        """ generated source for method withdraw """
        resp = "You don't have enough money in your account"
        resp = self.withdrawWithCredit(amount) if self.balance + 600 >= amount else resp if not self.getIsBlocked() else "Your account is blocked"
        return resp

    def getIsBlocked(self):
        """ generated source for method getIsBlocked """
        return self.isBlocked

    def equalCredit(self, amount):
        """ generated source for method equalCredit """
        self.isBlocked = True
        return self.withdrawEnough(amount) + " and your account has been blocked"

    def withdrawWithCredit(self, amount):
        """ generated source for method withdrawWithCredit """
        resp ="You don't have enough money in your account"
        resp = self.withdrawEnough(amount) if self.balance + 600 > amount else self.equalCredit(amount)
        return resp