class Menu:
    @staticmethod
    def base_menu():
        print('Program accounting profits and expenses\n--------------')
        print('Choose your path:')
        print('1)Open existing wallet')
        print('2)Create new wallet')
        print('3)Exit')

    @staticmethod
    def wallet_menu():
        print('Operations with wallet:')
        print('1)Check balance')
        print('2)Top up the balance')
        print('3)Withdraw money')
        print('4)History')
        print('5)Back to main menu')

    @staticmethod
    def balance():
        print('Your balance:')

    @staticmethod
    def currency():
        print('Choose the currency:')
        print('1)UAH')
        print('2)USD')
        print('3)EUR')
        print('4)Back')

    @staticmethod
    def success(message):
        print(message + '\n')

    @staticmethod
    def error(message):
        print('\n[ERROR]: ' + message + '. Please try again')
