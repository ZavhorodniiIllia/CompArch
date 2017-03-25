from menu import Menu
from model import Model

class Controller():

    def __init__(self, name):
        self.model = name

    def minus_money(self):
        print('\n')
        choise = -1
        coof=1
        while choise != 5:
            Menu.currency()
            try:
                choise = int(input('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:
                coof=1
                break
            elif choise == 2:
                coof=27
                break
            elif choise == 3:
                coof=29.5
                break
            elif choise==4:
                self.wallet()
        money= coof * float(input('Enter amount of money:'))
        op_name= input('Enter name of operation:')
        self.model.minus(money,op_name)

    def plus_money(self):
        print('\n')
        choise = -1
        coof=1
        while choise != 5:
            Menu.currency()
            try:
                choise = int(input('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:
                coof=1
                break
            elif choise == 2:
                coof=27
                break
            elif choise == 3:
                coof=29.5
                break
            elif choise == 4:
                self.wallet()
        money = coof * float(input('Enter amount of money:'))
        op_name = input('Enter name of operation:')
        self.model.plus(money,op_name)

    def ch_balance(self):
        print('\n')
        Menu.balance()
        self.model.balance()

    def wallet(self):
        print('\n')
        choise = -1
        while choise !=6:
            Menu.wallet_menu()
            try:
                choise=int(input ('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:
                self.ch_balance()

            elif choise == 2:
                self.plus_money()

            elif choise == 3:
                self.minus_money()

            elif choise == 4:
                print('\n')
                self.model.history()

            elif choise == 5:
                self.main()

        input ('Press Enter')

    def ex_wallet(self):
        print('\n')
        name=str(input('Choose the wallet:'))
        self.wallet()

    def new_wallet(self):
        print('\n')
        name = input('Enter wallet`s name:')
        balance= input('Enter your balance(in UAH):')
        self.model.new_wallet(name,balance)
        self.main()

    def main(self):
        print('\n')
        choise = -1
        while choise !=3:
            Menu.base_menu()
            try:
                choise=int(input ('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:
                self.ex_wallet()

            elif choise == 2:
                self.new_wallet()

        input('Press Enter')