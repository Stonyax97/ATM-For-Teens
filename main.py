# CHANGELOGS ------
#-Changed the structure of accounts fron a list to a dict of dicts.
#-Fixed a bug where the balance doesnt get updated in the JSON file.
version='1.1.1'

import os
import json
import time as t
import random
os.system('clear')

FILE_PATH=os.path.join(os.path.dirname(__file__), "accounts.json")

accounts={}

#FILE READING --------------------

    #CREATING FILE STRUCTURE ------
if not os.path.isfile(FILE_PATH) or os.path.getsize(FILE_PATH)==0: #if it doesn't exist OR is empty
    with open(FILE_PATH, "w") as file:
        json.dump(accounts, file, indent=4)

    #CHECKING FOR CORRUPTED FILE -------
with open(FILE_PATH, "r") as file:
    try:
        json.load(file)
    except json.JSONDecodeError:
        print("File is corrupted... Formating file.")
        with open (FILE_PATH, "w") as file:
            json.dump(accounts, file, indent=4)
            t.sleep(1.5)

    ##UPDATING VARIABLES ------
with open(FILE_PATH, 'r') as file:
    accounts=json.load(file)
    
class User:
    def __init__(self, username, age, balance, password):
        self.username=username
        self.age=age
        self.balance=balance
        self.password=password

    def deposit(self, deposit_amount):
        if deposit_amount<=0:
            print('Please enter a valid amount')
            toast()
            return
        
        else:
            self.balance+=deposit_amount
            print(f'${deposit_amount:.2f} despoited into your account succesfuly!')
            toast()

    def withdraw(self, withdraw_amount):
        if withdraw_amount<=0:
            print('Please enter a valid amount')
            toast()
            return

        elif withdraw_amount>self.balance:
            print('You are NOT Elon Musk.')
            toast()
            return

        else:
            self.balance-=withdraw_amount
            print(f'${withdraw_amount:.2f} succesfully withdrawn from your account!')
            toast()

def toast():
    t.sleep(1.5)

def goback():
    input('\nPress Enter to go back ')

def auth(username, age, balance, password):
    global cuser
    cuser=User(username, age, balance, password)

def create_account():
    os.system('clear')
    print('----- Create a new ATM For Teens account -----\n')
    username=str(input('Username: '))
    for account in accounts:
        if username in account:
            print('Username taken, please choose another one.')
            toast()
            create_account()

    check = False

    while check == False:
        try:
            age=float(input('Age: '))
            check = True
        except ValueError:
            print('Enter a valid age')
            toast()
        

    password=input('Password: ')

    check = False

    while check == False:
        password_check=input('Verify password: ')
        if password==password_check:
            check = True
        else:
            print('Passwords do not match')
            toast()
        
   
    accounts[username] = {
            'age':age,
            'balance':0,
            'password':password}

    print('Account created succesfully')
    auth(username, age, 0, password)
    toast()

def log_in():
    os.system('clear')
    username=input('Username: ')

    password=input('Password: ')
    if username in accounts:
        if accounts[username]['password']==password:
            auth(username, accounts[username]['age'], accounts[username]['balance'], password)
            return
        else:
            print('Password is incorecct, try again.')
            toast()
            log_in()

    else:
        print('Your account does not exist. ')
        toast()
        log_in()

def save():
    with open(FILE_PATH, 'r') as file:
        accounts=json.load(file)
        accounts[cuser.username]['balance']=cuser.balance
    with open(FILE_PATH, 'w') as file:
       json.dump(accounts, file, indent=4)


#MAIN APP --------------------------------------------
os.system('clear')

print('Welcome back to your ATM!')
c=input('\nPress Enter to Log in, Press c + enter to create an account\n')

if c=='':
    log_in()
    save()

else:
    create_account()
    save()

while True:
    os.system('clear')
    print('===============================\n         ATM For Teens         \n===============================')
    print('1-Check Balance')
    print('2-Deposit Money')
    print('3-Withdraw Money')
    print('4-Exit')

    c=input('Choose an option: ')

    if c=='1':
        print(f'Balance', '-'*15, f'{cuser.username}\nYou currently have ${cuser.balance:.2f}')
        goback()

    elif c=='2':
        print(f'Deposit =======================')
        try:
            amount=float(input('Enter deposit amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()
            continue

        cuser.deposit(amount)

    elif c=='3':
        print(f'Withdrawal =========== Balance: ${cuser.balance:.2f}')
        try:
            amount=float(input(' Enter withdrawal amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()
            continue

        cuser.withdraw(amount)

    elif c=='4':
        raise SystemExit()

    else:
        print('Please choose a valid option')
        toast()

    save()

    os.system('clear')