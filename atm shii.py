from datetime import datetime

now = datetime.now()
currentDt = now.strftime("%d/%m/%Y %H:%M:%S")

allowedUsers = ['Seyi', 'Sam', 'Love']
allowedPassword = ['passwordSeyi', 'passwordSam', 'passwordLove']
Balance = 0
name = input('What is your name? \n')
if name in allowedUsers:
    password = input('Your password \n')
    userId = allowedUsers.index(name)
    if password == allowedPassword[userId]:
        print(currentDt)
        print('Welcome ', name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        
        selectedOption = int(input('Please select an option \n'))
        if selectedOption == 1:
            withdrawalAmount = int(input('How much would you like to withdraw? \n'))
            print('Take your cash')
        elif selectedOption == 2:
            depositAmount = int(input('How much would you like to deposit \n'))
            Balance = Balance + depositAmount
            print('Your balance is:', Balance)
        elif selectedOption == 3:
            issue = input('What issue will you like to report? \n')
            print('Thank you for contacting us')
        else:
            print('Invalid option selected, please try again')

    else:
        print('Password incorrect please try again')

else:
    print("Name not found please try again")




