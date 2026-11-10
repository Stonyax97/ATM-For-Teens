# CHANGELOGS ------
#- Removed leftover test stuff from preview
#- Refined transaction history

version='1.2'

import os
import json
import time as t
from datetime import datetime
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
    def __init__(self, username, age, balance, password, transactions):
        self.username=username
        self.age=age
        self.balance=balance
        self.password=password
        self.transactions=transactions

    def deposit(self, deposit_amount):
        if deposit_amount<=0:
            print('Please enter a valid amount')
            toast()
            return
        
        else:
            self.balance+=deposit_amount
            self.transactions.append({'time': datetime.now().strftime("%Y-%m-%d %H:%M"), 
                                      'type': 'Deposit', 
                                      'amount': deposit_amount})
            print(f'${deposit_amount:.2f} despoited into your account succesfuly!')
            toast()

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount<=0:
            print('Please enter a valid amount')
            toast()
            return

        elif withdrawal_amount>self.balance:
            print('You are NOT Elon Musk.')
            toast()
            return

        else:
            self.balance-=withdrawal_amount
            self.transactions.append({'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
                                      'type': 'Withdrawal', 
                                      'amount': withdrawal_amount})
            print(f'${withdrawal_amount:.2f} succesfully withdrawn from your account!')
            toast()

def toast():
    t.sleep(1.5)

def goback():
    input('\nPress Enter to go back ')

def auth(username, age, balance, password, transactions):
    global cuser
    cuser=User(username, age, balance, password, transactions)

def create_account():
    os.system('clear')
    print('----- Create a new ATM For Teens account -----\n')

    while True:
        username=str(input('Username: '))
        if username in accounts:
            print('Username taken, please choose another one.')
            toast()
        else:
            break

    while True:
        try:
            age=float(input('Age: '))
            if 12<=age<18:
                break
            else:
                print("You are not eligible for ATM For Teens. ")
                exit()
        except ValueError:
            print('Enter a valid age')
            toast()
        
    password=input('Password: ')

    while True:
        password_check=input('Verify password: ')
        if password==password_check:
            break
        else:
            print('Passwords do not match')
            toast()
        
    accounts[username] = {
            'age':age,
            'balance':0,
            'password':password,
            'transactions':[]
            }

    print('Account created succesfully')
    auth(username, age, 0, password, [])
    toast()

def log_in():
    os.system('clear')
    while True:
        username=input('Username: ')
        if username in accounts:
            break
        else:
            print('Your account does not exist. ')
            toast()

    while True:
        password=input('Password: ')
        if accounts[username]['password']==password:
            auth(username, accounts[username]['age'], accounts[username]['balance'], password, accounts[username]['transactions'])
            break
        else:
            print('Password is incorecct, try again.')
            toast()

def save():
    global cuser
    accounts[cuser.username]['balance'] = cuser.balance
    accounts[cuser.username]['transactions'] = cuser.transactions
    with open(FILE_PATH, 'w') as file:
        json.dump(accounts, file, indent=4)


#MAIN APP --------------------------------------------
os.system('clear')

print('Welcome back to your ATM!')
c=input('\nPress Enter to Log in\nPress "C" then Enter to create an account\n')

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
    print('4-History')
    print('5-Exit')

    c=input('Choose an option: ')

    if c=='1':
        print(f'Balance', '-'*15, f'{cuser.username}\nYou currently have ${cuser.balance:.2f}')
        goback()

    elif c=='2':
        print(f'Deposit -----------------------')
        try:
            amount=float(input('Enter deposit amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()
            continue

        cuser.deposit(amount)

    elif c=='3':
        print(f'Withdrawal ------------ Balance: ${cuser.balance:.2f}')
        try:
            amount=float(input(' Enter withdrawal amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()
            continue

        cuser.withdraw(amount)

    elif c=='4':
        os.system('clear')
        print(f'Transactions ------------ {len(cuser.transactions)}')
        for banana in range(len(cuser.transactions)):
            print(f'- {cuser.transactions[banana]['type']} of ${cuser.transactions[banana]['amount']:.2f} at {cuser.transactions[banana]['time']}')
        goback()
    
    
    elif c=='5':
        raise SystemExit()

    else:
        print('Please choose a valid option')
        toast()

    save()

    os.system('clear')