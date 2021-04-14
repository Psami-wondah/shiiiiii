
class budget:
    
    #balance = {'food':100,'clothing':200}
    
    def __init__(self,cat_select): 
        self.cat_select = cat_select
        
    database = {'food':100,'clothing':200}
    print('Welcome to Budget App')
    print('Available Options \n')
    print('1 Deposit \n')
    print('2 Withdraw \n')
    print('3 Transfer \n')
    select_action = int(input())
    if select_action == 1:
        cat_select = input('Enter category to fund \n')
        if cat_select in database:
            cat_select = budget(cat_select)
            print('ready')
            cat_select.deposit()
        else:
            print('wrong selection \n')
        
               
    else:
        print('Invalid category selected \n')
    
    def balance(self):
        print(self.categories,'balance is: ')
        bul = database[self.categories]
        return categories
        
    def withdraw(self):
        withdraw = int(input('Amount to withdraw: \n'))
        if withdraw <= database[self.categories]:
            print('done')
            #withdraw_1 = self.categories.balance() - withdraw
            #return withdraw
        else:
            print('Insufficient Amount \n')
        return withdraw()
        
    def deposit(self):
        deposit_amount = int(input('How much did you want to deposit \n'))
        print('Deposit successful')
        deposit = database['food'] + deposit_amount
        print(database['food'])
        
    def login():
        balance()





   
    
