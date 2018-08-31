from account import Account
from client import Client
class Bank:
    allAccounts = []
    # create an account which creates a new client and saves their information in a dictionary
    def createAccount(self, accountNumber, firstName, lastName):
        account = Account(accountNumber)
        account.client.firstName = firstName
        account.client.lastName = lastName
        newAccount = {accountNumber: {
            'First Name': firstName,
            'Last Name' : lastName,
            'Balance' : account.balance
        }}
        account.client.accounts.append(newAccount)
        self.allAccounts.append(newAccount)
# Print all the accounts in the bank
    def displayAllAccounts(self):
         print('Accounts in the Bank')
         print('-------------------------------------')
         print('%d accounts found' % (len(self.allAccounts)))
         print(self.allAccounts)
         for account in self.allAccounts:
            print('-------------------------------------')
            for key in account:
                print('%s : %s' % (key, account[key]))
# Search for a specific account given the account Number
    def searchAccount(self, accountNumber):
        for account in self.allAccounts:
            for clientAccount in account:
                if clientAccount == accountNumber:
                    print('Account number %d details ' % (accountNumber))
                    print('----------------------------------------')
                    for accountDetail in account[clientAccount]:
                        print('%s: %s' % (accountDetail, account[clientAccount][accountDetail]))
# Deposit money 
    def deposit(self, accountNumber, amount):
        for accounts in self.allAccounts:
            for clientAccount, value in accounts.items():
                if clientAccount == accountNumber:
                    value['Balance'] += amount
        self.searchAccount(accountNumber)

# Withdraw money
    def withdraw(self, accountNumber, amount):
        for accounts in self.allAccounts:
            for clientAccount, value in accounts.items():
                if clientAccount == accountNumber:
                    if value['Balance'] > amount:
                        value['Balance'] -= amount
                    else:
                        print('You have insufficient funds on your account')
        self.searchAccount(accountNumber)
                    

            




myBank = Bank()
myBank.createAccount(444444444, 'Frank', 'Atukunda')
myBank.createAccount(555555555, 'Simon', 'Lee')
# myBank.displayAllAccounts()
#myBank.searchAccount(555555555)
myBank.deposit(444444444, 500)
myBank.deposit(555555555, 200)
myBank.withdraw(555555555, 100)
myBank.withdraw(555555555, 100)

