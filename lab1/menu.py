class Menu:
    @staticmethod
    def base_menu():
        print('\n')
        print('Program accounting profits and expenses\n--------------')
        print('Choose your path:')
        print('1)Open existing wallet')
        print('2)Create new wallet')
        print('3)Delete existing wallet')
        print('4)Exit')

    @staticmethod
    def wallet_menu():
        print('\n')
        print('Operations with wallet:')
        print('1)Check balance')
        print('2)Top up the balance')
        print('3)Withdraw money')
        print('4)History')
        print('5)Back to main menu')

    @staticmethod
    def balance():
        print('\n')
        print('Your balance:')

    @staticmethod
    def currency():
        print('\n')
        print('Choose the currency:')
        print('1)UAH')
        print('2)USD')
        print('3)EUR')
        print('4)Back')

    @staticmethod
    def Ex_wallet():
        print('\n' + 'Existing wallets:' + '\n')

    @staticmethod
    def success(message):
        print(message + '\n')

    @staticmethod
    def error(message):
        print('\n[ERROR]: ' + message + '. Please try again')
