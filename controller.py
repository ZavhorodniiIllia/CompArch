from menu import Menu
from model import Model

class Controller():

    def wallet(self):
        choise = -1
        while choise !=6:
            Menu.wallet_menu()
            try:
                choise=int(input ('Enter menu item:'))
            except ValueError:
                Menu.error('Incorrect value')

            if choise == 1:
                self.

            elif choise == 2:
                self.

            if choise == 3:
                self.

            elif choise == 4:
                self.

            if choise == 5:
                self.main()

        input ('Press Enter')

    def ex_wallet(self):
        Menu.open_menu()

    def new_wallet(self):
        Menu.create_menu()

        Menu.balance_menu()

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