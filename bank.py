from account import Account
from client import Client
class Bank:
    allAccounts = []
    def createAccount(self, accountNumber, firstName, lastName):
        account = Account(accountNumber)
        account.client.firstName = firstName
        account.client.lastName = lastName
        account.client.accounts.append(account)
        newAccount = { accountNumber: accountNumber, firstName: firstName, lastName: lastName }
        self.allAccounts.append(newAccount)

    def displayAllAccounts(self):
         print('Accounts in the Bank')
         print('-------------------------------------')
         print('%d accounts found' % (len(self.allAccounts)))
         for account in self.allAccounts:
            print('-------------------------------------')
            for key in account:
                print('%s' % (account[key]))

    def displayClientAccounts(self, accountNumber):
        for account in self.allAccounts:
            if account.accountNumber in self.allAccounts:
                for clientAccount in account.client.accounts:
                     print('Account Number: %d' % (account.accountNumber))
                     print ('Account Name: %s' % (clientAccount.firstName + " " + clientAccount.lastName))
                     print('Account Balance: %d' % (account.balance))
            else:
                print('Account number %d was not found!' % (account.accountNumber))

myBank = Bank()
myBank.createAccount(444444444, 'Frank', 'Atukunda')
myBank.createAccount(555555555, 'Simon', 'Lee')
myBank.displayAllAccounts()