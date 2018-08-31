# students = []
# student1 = { 'name': 'Frank', 'age': 24}
# student2 = { 'name': 'Luke', 'age': 18}

# students.append(student1)
# students.append(student2)

# for student in students:
#     print(student)
#     for key in student:
#         print("%s : %s" % (key, student[key]))
userAccounts =[]

def createUser(accountNo, name, age):
    newUser = {accountNo: {
        'account': accountNo,
        'name': name,
        'age': age
    }}
    userAccounts.append(newUser)
def printAccounts():
    for accounts in userAccounts:
        for account, value in accounts.items():
            print('%s: %s' % (account, value))

createUser(4444444, 'Sam', 23)
createUser(5555555, 'Frank', 29)
printAccounts()