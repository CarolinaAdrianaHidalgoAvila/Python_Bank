from Code.BankAccount.NocommissionAccount import NoCommissionAccount


class HousingAccount(NoCommissionAccount):
    """ generated source for class HousingAccount """
    def __init__(self, account_number, customer_number):
        """ generated source for method __init__ """
        super(HousingAccount, self).__init__(customer_number)
        accountInterest = 0.22
      
