import random as ran
from datetime import datetime

now = datetime.now()
currentDt = now.strftime("%d/%m/%Y %H:%M:%S")
#register
# - firstname, lastname, password, email
# - generate user account

#login
#- account number and password
#bank operations

database = {
    #this is my ecobank account if you wan sub for me. taink u
    4290010047: ['Okechukwu Samuel', 'Owhondah', 'okechukwusamuel16@gmail.com', 'passwordSam', 5000],

}

currentLoggedInAccount = False

def init():
    isValidOption = False
    print('Welcome to bankPHP')
    while isValidOption == False:
        haveAccount=int(input('Do you have an account with us?: 1 (yes)  2 (No) \n'))
        if haveAccount == 1:
            isValidOption = True
            login()
        elif haveAccount== 2:
            isValidOption = True
            print(register())
        else:
            print('wrong input please try again')

def login():
    print('******* Login *******')
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input('Enter your account number \n'))
        password = input('Enter your password \n')
        for accountNumber, userDetails in database.items():
            if accountNumber == accountNumberFromUser and userDetails[3] == password:
                isLoginSuccessful = True
                global currentLoggedInAccount
                currentLoggedInAccount = accountNumberFromUser
                bankOperations(userDetails)

        if isLoginSuccessful == False:
            print('Invalid account number or password')

def register():
    print('****** Register ******')
    email = input('please enter your email address \n')
    first_name = input('Your First Name? \n')
    last_name = input('Your last name \n')
    password = input('create a password \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, 0]

    print('Your account has been created')
    print(' == ==== ===== ======= ====== ==')
    print('Your account number is:', accountNumber)
    print('Make sure you keep it safe')
    print(' == ==== ===== ======= ====== ===')
    login()

def secondBankOperation():
    isValidOption = False
    while isValidOption == False:
        print('What would you like to do?')
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Balance')
        print('4. Complaint')
        print('5. Logout')
        print('6. Exit')
        selectedOption = int(input('Please select an option \n'))

        if selectedOption == 1:
            isValidOption = True
            withdrawalOperation()
        elif selectedOption == 2:
            isValidOption = True
            depositOperation()
        elif selectedOption == 3:
            isValidOption = True
            balanceCheck()
        elif selectedOption == 4:
            isValidOption = True
            complaintOperation()
        elif selectedOption == 5:
            isValidOption = True
            print('Thank you for Banking with us. ')
            login()
        elif selectedOption == 6:
            isValidOption = True
            print('Thank you for Banking with us. ')
            exit()
        else:
            print('Invalid option selected')

def bankOperations(user):
    print(currentDt)
    print('Welcome', user[0], user[1])
    secondBankOperation()

def withdrawalOperation():
    withdrawalAmount = int(input('How much would you like to withdraw? \n'))
    print('Please take your cash')
    print('Currently dispensing', withdrawalAmount, 'Naira')
    database[currentLoggedInAccount][4] -= withdrawalAmount
    endingRemark()

def depositOperation():
    depositAmount = int(input('How much would you like to deposit? \n'))
    database[currentLoggedInAccount][4] += depositAmount
    print('%d Naira has Been added to your account and now your balance is: %s' % (depositAmount, database[currentLoggedInAccount][4]))
    endingRemark()

def balanceCheck():
    print('Your current balance is: %d Naira' % database[currentLoggedInAccount][4])
    endingRemark()

def complaintOperation():
    issue = input('What issue will you like to report? \n')
    print('Your issue: " %s " will be forwarded to the customer care unit' % issue)
    print('Thank you for contacting us')
    endingRemark()

def logout():
    login()

def endingRemark():
    isValidOption = False
    while isValidOption == False:
        selectedOption = int(input('Would you like to do any other thing?  (1) Yes (2) No \n'))
        if selectedOption == 1:
            isValidOption = True
            secondBankOperation()
        elif selectedOption == 2:
            isValidOption = True
            print('Thank you for Banking with us. ')
            exit()
        else:
            print("wrong input, please try again")

def generateAccountNumber():
    return ran.randrange(1000000000, 9999999999)

#### ACTUAL BANKING SYSTEM ####

init()



