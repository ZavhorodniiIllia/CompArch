from menu import Menu
from model import Model

wallet =''

class Controller():

    def __init__(self, data_base):
        self.model = data_base

    def minus_money(self):
        """Контроллер для выбора валюты и записи количества денег для снятия и название операции"""
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
            else:
                Menu.error('Incorrect value')
        money=float(input('Enter amount of money:'))
        op_name= input('Enter name of operation:')
        balance = float(self.model.str_to_float(self.model.chek(wallet)))
        self.model.minus(money, op_name,balance,coof,wallet)

    def plus_money(self):
        """Контроллер для выбора валюты и записи количества денег для пополнения и название операции"""
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
            else:
                Menu.error('Incorrect value')
        money = float(input('Enter amount of money:'))
        op_name = input('Enter name of operation:')
        balance=float(self.model.str_to_float(self.model.chek(wallet)))
        self.model.plus(money,op_name,balance,coof,wallet)

    def ch_balance(self):
        """Контроллер для проверки баланса"""
        print('\n')
        Menu.balance()
        balance = self.model.chek(wallet)
        print(balance)

    def wallet(self):
        """Контроллер для меню кошелька"""
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

        Menu.error('Incorrect value')
        self.wallet()

    def ex_wallet(self):
        """Контроллер для выбора кошелька"""
        with open('wallet.txt', 'r') as data_base:
            choise = -1
            print('\n' + 'Existing wallets:'+ '\n')
            count=0
            lines = data_base.read().splitlines()
            for line in lines:
                count+=1
                print(str(count)+')' + line)
            print(str(count+1) + ')Back to main menu')
        while choise != count:
            try:
                choise=int(input ('\n Enter menu item:'))
            except ValueError:\
                    Menu.error('Incorect value')
            if choise <= count :
                global wallet
                wallet = lines[choise-1]
                self.wallet()
            if choise == count+1:
                self.main()
            else:
                Menu.error('No such wallet')
                self.ex_wallet()


    def new_wallet(self):
        """Контроллер для создания нового кошелька """
        print('\n')
        name = input('Enter wallet`s name:')
        try:
            with open(name + '.txt', 'x') as check:
                pass
        except:
            Menu.error('Wallet with this name already exist')
            self.main()
        try:
            balance= int(input('Enter your balance(in UAH):'))
        except:
            Menu.error('Wrong input')
            self.main()
        self.model.new_wallet(name,str(balance))


    def main(self):
        """Контроллер для главного меню"""
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

            elif choise == 3:
                exit(0)
            else:
                Menu.error('Incorrect value')
