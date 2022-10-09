class CurrentAccount(CommissionAccount, IWithdrawMoney):
    """ generated source for class CurrentAccount """
    def __init__(self, accountNumber, customerNumber):
        """ generated source for method __init__ """
        super(CurrentAccount, self).__init__(customerNumber)
        accountInterest = Constants.ACCOUNT_INTEREST_CURRENT
        type_ = AccountType.CURRENT

    def withdraw(self, amount):
        """ generated source for method withdraw """
        resp = Messages.NOT_ENOUHG
        resp = withdrawEnough(amount) if balance >= amount else resp
        return resp
