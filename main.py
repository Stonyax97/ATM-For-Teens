import os
import time as t

class User:
    def __init__(self, name, age, balance):
        self.name=name
        self.age=age
        self.balance=balance

    def deposit(self, deposit_amount):
        self.balance+=deposit_amount

    def withdraw(self, withdraw_amount):
        self.balance-=withdraw_amount

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
            amount=int(input(' Enter deposit amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()

        if amount<=0:
            print('Please enter a valid amount')
            toast()

        else:
            print(f'Depositing ${amount:.2f} into your account...')
            cuser.deposit(amount)
            print(f'${amount:.2f} despoited into your account succesfuly!')
            toast()

    elif c=='3':
        print(f'Withdrawal =========== Balance: ${cuser.balance:.2f}')
        try:
            amount=int(input(' Enter withdrawal amount: '))
        except ValueError:
            print('Please enter a valid amount')
            toast()

        if amount<=0:
            print('Please enter a valid amount')
            toast()

        if amount>cuser.balance:
            print('You are NOT Elon Musk.')
            toast()

        else:
            print(f'Withdrawing ${amount:.2f} from your account...')
            cuser.withdraw(amount)
            print(f'${amount:.2f} succesfully withdrawn from your account!')
            toast()

    elif c=='4':
        raise SystemExit()

    else:
        print('Please choose a valid option')
        toast()

    os.system('clear')