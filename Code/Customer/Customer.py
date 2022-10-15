class Customer(object):
    'Represents a customer of a bank'
    def __init__(self, name, age, income, acct):
        self.name = name
        self.age = age
        self.income = income
        self.bankAccount = acct

   
    def makeDeposit(self, amount):
        if(amount>0):
            self.bankAccount.deposit(amount)
            print(f'Successful deposit of {amount} made!')
        else:
            raise Exception("You cannot deposit a negative amount!")
           
        return self.bankAccount.balance
    
    def incrementAge(self, incrementValue=1):
        pastAge = self.age+ incrementValue
        return pastAge

    def changeIncome(self, newIncome):
        self.income = newIncome
        return self.income
    
    def changeBankAccount(self, newAccount):
        self.bankAccount = newAccount
        return self.bankAccount



    def makeWithdrawal(self, amount):
        balance = self.bankAccount.balance
        if(amount<0):
            print('You cannot withdraw a negative amount!')
            return balance
        if(amount>balance):
            print(f'There is not enough money in the account to withdraw ${amount}')
            return balance
        return self.bankAccount.withdraw(amount)
