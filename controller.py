from menu import Menu
from model import Model

class Controller():

    def __init__(self, data_base):
        self.model = data_base

    def history(self):
        self.model.history()

    def minus_money(self):
        choise = -1
        while choise != 4:
            Menu.currency()
            try:
                choise = int(input('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:

            elif choise == 2:

            elif choise == 3:

        input('Press Enter')

        money= float(input('Enter amount of money:'))
        op_name=str(input('Enter name of operation:'))
        self.model.minus(money,op_name)

    def plus_money(self):
        choise = -1
        while choise != 4:
            Menu.currency()
            try:
                choise = int(input('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:

            elif choise == 2:

            elif choise == 3:

        input('Press Enter')

        money = float(input('Enter amount of money:'))
        op_name = str(input('Enter name of operation:'))
        self.model.plus(money,op_name)

    def ch_balance(self):
        Menu.balance()

    def wallet(self):
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
                self.history()

            elif choise == 5:
                self.main()

        input ('Press Enter')

    def ex_wallet(self):

        name=str(input('Choose the wallet:'))
        self.wallet()

    def new_wallet(self):
        name = str(input('Enter wallet`s name:'))
        balance=float(input('Enter your balance(in UAH):'))
        self.model.new_wallet(name,balance)
        self.wallet()

    def main(self):
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