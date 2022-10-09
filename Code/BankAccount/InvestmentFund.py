class InvestmentFund(CommissionAccount, IWithdrawMoney):
    """ generated source for class InvestmentFund """
    isBlocked = bool()

    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(InvestmentFund, self).__init__(customerNumber)
        accountInterest = Constants.ACCOUNT_INTEREST_INVEST
        self.isBlocked = False
        type_ = AccountType.INVEST

    def withdraw(self, amount):
        """ generated source for method withdraw """
        resp = Messages.NOT_ENOUHG
        resp = withdrawWithCredit(amount) if balance + Constants.CREDIT >= amount else resp if not getIsBlocked() else Messages.BLOCKED
        return resp

    def getIsBlocked(self):
        """ generated source for method getIsBlocked """
        return self.isBlocked

    def equalCredit(self, amount):
        """ generated source for method equalCredit """
        self.isBlocked = True
        return withdrawEnough(amount) + Messages.EXCEED_CREDIT

    def withdrawWithCredit(self, amount):
        """ generated source for method withdrawWithCredit """
        resp = Messages.NOT_ENOUHG
        resp = withdrawEnough(amount) if balance + Constants.CREDIT > amount else equalCredit(amount)
        return resp