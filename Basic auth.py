import random as ran
#register
# - username, password, email
# - generate user account

#login
#- username  or email and password
#bank operations

database = {}

def init():
    isValidOption = False
    print('welcome to bankPHP')
    while isValidOption == False:
        haveAccount=int(input('do you have an account with us?: 1 (yes)  2 (No) \n'))
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
            if accountNumber == accountNumberFromUser and userDetails[3]:
                bankOperations(userDetails)
                isLoginSuccessful = True
        if isLoginSuccessful == False:
            print('Invalid account number or password')



def register():
    print('****** Register ******')
    email = input('please enter your email address \n')
    first_name= input('Your First Name? \n')
    last_name = input('Your last name \n')
    password = input('create a password \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]

    print('Your account has been created')
    print(' == ==== ===== ======= ====== ==')
    print('Your account number is:', accountNumber)
    print('Make sure you keep it safe')
    print(' == ==== ===== ======= ====== ===')
    login()

def bankOperations(user):
    print('Welcome', user[0], user[1])
    isValidOption = False
    while isValidOption == False:
        selectedOption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

        if selectedOption == 1:
            isValidOption = True
            depositOperation()
        elif selectedOption == 2:
            isValidOption = True
            withdrawalOperation()
        elif selectedOption == 3:
            isValidOption = 1
            login()
        elif selectedOption == 4:
            isValidOption = 1
            exit()
        else:
            print('Invalid option selected')


def withdrawalOperation():
    print('Withdrawal')
def depositOperation():
    print('deposit operations')





def generateAccountNumber():
    return ran.randrange(1000000000, 9999999999)


#### ACTUAL BANKING SYSTEM ####


init()



