from menu import Menu
from model import Model

wallet =''

class Controller():

    def __init__(self, data_base):
        self.model = data_base

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
                coof=2
                break
            elif choise == 3:
                coof=3
                break
            elif choise==4:
                self.wallet()
        money=float(input('Enter amount of money:'))
        op_name= input('Enter name of operation:')
        balance = float(self.model.str_to_float(self.model.chek(wallet)))
        self.model.minus(money, op_name,balance,coof,wallet)

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
                coof=2
                break
            elif choise == 3:
                coof=3
                break
            elif choise == 4:
                self.wallet()
        money = float(input('Enter amount of money:'))
        op_name = input('Enter name of operation:')
        balance=float(self.model.str_to_float(self.model.chek(wallet)))
        self.model.plus(money,op_name,balance,coof,wallet)

    def ch_balance(self):
        print('\n')
        Menu.balance()
        balance = self.model.chek(wallet)
        print(balance)

    def wallet(self):
        choise = -1
        while choise !=6:
            print('\n')
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
                self.model.history(wallet)

            elif choise == 5:
                self.main()

        input ('Press Enter')

    def ex_wallet(self):
        print('\n' + 'Existing wallets:'+ '\n')
        self.model.wallets()
        global wallet
        wallet = str(input('Choose the wallet:'))
        self.wallet()

    def new_wallet(self):
        print('\n')
        name = input('Enter wallet`s name:')
        balance= input('Enter your balance(in UAH):')
        self.model.new_wallet(name,balance)
        self.main()

    def main(self):
        choise = -1
        while choise !=3:
            print('\n')
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