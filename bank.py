from account import Account
from client import Client
class Bank:
    allAccounts = []
    def createAccount(self, accountNumber, firstName, lastName):
        account = Account(accountNumber)
        account.client.firstName = firstName
        account.client.lastName = lastName
        account.client.accounts.append(account)
        newAccount = { "Account Number": accountNumber, "First Name": firstName, "Last Name": lastName, "Balance": account.balance}
        self.allAccounts.append(newAccount)

    def displayAllAccounts(self):
         print('Accounts in the Bank')
         print('-------------------------------------')
         print('%d accounts found' % (len(self.allAccounts)))
         print(self.allAccounts)
         for account in self.allAccounts:
            print('-------------------------------------')
            for key in account:
                print('%s : %s' % (key, account[key]))

    def searchAccount(self, accountNumber):
        for account in self.allAccounts:
            for clientAccount in account:
                if account[clientAccount] == accountNumber:
                     print('Account number %d details ' % (accountNumber))
                     print('--------------------------------')
                     print('%s: %s' % (clientAccount, account[clientAccount]))
                     print('First Name: %s' % (account['First Name']))
                     print('Last Name: %s' % (account['Last Name']))
            

myBank = Bank()
myBank.createAccount(444444444, 'Frank', 'Atukunda')
myBank.createAccount(555555555, 'Simon', 'Lee')
#myBank.displayAllAccounts()
myBank.searchAccount(555555555)