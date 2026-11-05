# CHANGELOGS ------
version='1.0.1'
#Fixed a bug where error checks would still move to the next loop.
#Structure and code improvements
import os
import time as t

class User:
    def __init__(self, name, age, balance):
        self.name=name
        self.age=age
        self.balance=balance

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

#Test mode:
user1=User('Ziyad', 16, 500)

cuser=user1

def toast():
    t.sleep(1.5)

def goback():
    input('Press Enter to go back ')

while True:
    print('=============================\n             ATM            \n=============================\n')
    print('1-Check Balance')
    print('2-Deposit Money')
    print('3-Withdraw Money')
    print('4-Exit')

    c=input('Choose an option: ')

    if c=='1':
        print(f'Balance ================ {cuser.name}\nYou currently have ${cuser.balance:.2f}')
        goback()

    elif c=='2':
        print(f'Deposal =======================')
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

    os.system('clear')