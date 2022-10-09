from Code.BankAccount.NocommissionAccount import NoCommissionAccount


class HousingAccount(NoCommissionAccount):
    """ generated source for class HousingAccount """
    def __init__(self, acctType='Savings', balance=0):
        """ generated source for method __init__ """
        NoCommissionAccount.__init__(self, acctType, balance)
        accountInterest = 0.22
      
