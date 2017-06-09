from datetime import date, time
import datetime
import os

import self as self


class Model:
    def __init__(self, name):
        """
            Initialize Model class
            :param name: wallet`s name
        """
        self.load(name)

    def load(self, name):
        """
            Method open file with wallet`s names
            :param name: wallet`s name
        """
        file = open('wallet.txt', 'r')

    def new_wallet(self, name, balance):
        """
            Method to create a file for a new wallet and write it`s name to the purse list
            :param name: wallet`s name
            :param balance: balance
            Example:
                >>> new_wallet("example", 200)
        """
        with open(name + '.txt', 'w') as file:
            file.write(name + '\n')
            file.write(balance + ' (UAH)' + '\n')
        with open('wallet.txt', 'a') as data_base:
            data_base.write(name + '\n')

    def chek(self, name):
        """
            Method to display the current balance
            :param name: wallet`s name
            :return: row with balance
            Examples:
                >>> chek("example")
                200 (UAH)
        """
        lines = 0
        with open(name + '.txt', 'r') as file:
            line = file.readlines()
            lines = len(line)
            return(line[lines-1])

    def minus(self, money, op_name, balance, coof, name):
        """
            Method for recording the operation of withdrawing money and updating the balance sheet
            :param money: amount of money
            :param op_name: operation`s name
            :param balance: current balance
            :param coof: currency`s flag
            :param name: wallet`s name
            Examples:
                >>> minus(50, "test1", 200, 1, example)
        """
        with open(name + '.txt', 'a') as file:
            now_time = datetime.datetime.now()
            if coof == 1:
                file.write('-' + str(money) + ' UAH' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            elif coof == 2:
                file.write('-' + str(money)+' USD' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
                money *= 27
            elif coof == 3:
                file.write('-' + str(money) + ' EUR' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
                money *= 29.5
            bm = balance - money
            file.write(str(bm)+' (UAH)' + '\n')

    def plus(self, money, op_name, balance, coof, name):
        """
            Method for recording the operation of replenishing money and updating the balance
            :param money: amount of money
            :param op_name: operation`s name
            :param balance: current balance
            :param coof: currency`s flag
            :param name: wallet`s name
            Example:
                >>> minus(50, "test2", 200, 1, example)
        """
        with open(name + '.txt', 'a') as file:
            now_time = datetime.datetime.now()
            if coof == 1:
                file.write('+' + str(money) + ' UAH' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            elif coof == 2:
                file.write('+' + str(money)+' USD' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
                money *= 27
            elif coof == 3:
                file.write('+' + str(money) + ' EUR' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
                money *= 29.5
            bm = balance + money
            file.write(str(bm) + ' (UAH)' + '\n')

    def history(self, name):
        """
            Method for displaying the history of the wallet
            :param name: wallet`s name
            :return: operation history
            Example:
                >>> history("example")
                example
                200 (UAH)
                -50.0 UAH: test1; operation time
                150.0 (UAH)
                +50.0 UAH: test2; operation time
                200.0 (UAH)

        """
        with open(name + '.txt', 'r') as file:
            print(file.read())

    def str_to_float(self, money):
        """
            Method for changing string to float
            :param money: string value
            Example:
                >>> str_to_float("200")
                200.0

        """
        mon = ''
        for i in money:
            if i != ' ':
                mon += i
            else:
                break
        return mon

    def delete(self, name):
        """
            Method deletes the purse and deletes its name in the purse list
            :param name: wallet`s name
            Examples:
                >>> delete("example")
        """
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name + '.txt')
        os.remove(path)
        rst = []
        with open('wallet.txt', 'r') as data_base:
            lines = data_base.read().splitlines()
            for line in lines:
                if line != name:
                    rst.append(line)

        with open('wallet.txt', 'w') as data_base:
            data_base.write('\n'.join(rst) + '\n')

    def wallet(self):
        """
            Method displays wallet`s list
            Exapmle:
                >>> wallet()
                1)example
                2)Back to main menu
        """
        with open('wallet.txt', 'r') as data_base:
            count = 0
            lines = data_base.read().splitlines()
            for line in lines:
                count += 1
                print(str(count)+')' + line)
            print(str(count+1) + ')Back to main menu')
        return count

    def wallet_ch(self, choise):
        """
            Method chooses wallet
            :param choise: wallet`s number
            :return: wallet`s name
            Example:
                >>> wallet_ch(1)
        """
        with open('wallet.txt', 'r') as data_base:
            lines = data_base.read().splitlines()
            wallet = lines[choise - 1]
        return wallet

    def wallet_del(self,choise):
        """
            Method delete wallet
            :param choise: wallet`s number
            Example:
                >>> wallet_del(1)
        """
        with open('wallet.txt', 'r') as data_base:
                name = []
                lines = data_base.read().splitlines()
                name = lines[choise - 1]
        self.delete(name)
