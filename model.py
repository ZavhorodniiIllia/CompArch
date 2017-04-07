from datetime import date, time
import datetime
import os


class Model:
    def __init__(self, name):
        self.load(name)

    def load(self, name):
        file = open('wallet.txt', 'r')

    def new_wallet(self, name, balance):
        """
        Функция для создания файла для нового кошелька и запись его названия в список кошельков
        :param name: название кошелька
        :param balance: баланс
        :return: функция ни чего не возвращает
        """
        with open(name + '.txt', 'w') as file:
            file.write(name + '\n')
            file.write(balance + ' (UAH)' + '\n')
        with open('wallet.txt', 'a') as data_base:
            data_base.write(name + '\n')

    def chek(self, name):
        """
        Функция для вывода текущего баланса
        :param name: название кошелька
        :return: строка в которой хранится баланс
        """
        lines = 0
        with open(name + '.txt', 'r') as file:
            line = file.readlines()
            lines = len(line)
            return(line[lines-1])

    def minus(self, money, op_name, balance, coof, name):
        """
        Функция для записи операции снятия денег и обновления баланса
        :param money: количество денег
        :param op_name: название операции
        :param balance: текущий баланс
        :param coof: флаг валюты
        :param name: имя кошелька
        :return: функция ни чего не возвращает
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
        Функция для записи операции пополнения денег и обновления баланса
        :param money: количество денег
        :param op_name: название операции
        :param balance: текущий баланс
        :param coof: флаг валюты
        :param name: имя кошелька
        :return: функция ни чего не возвращает
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
        Функция для вывода истории кошелька
        :param name: название кошелька
        :return: полная история операций
        """
        with open(name + '.txt', 'r') as file:
            print(file.read())

    def str_to_float(self, money):
        """
        Функция для изменения string в float
        :param money: значение типа strinig
        :return: значение типа float
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
        Функция удаляет кошелек и удалает его имя в списке кошельков
        :param name: название кошелька
        :return: функция ни чего не возвращает
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
        with open('wallet.txt', 'r') as data_base:
            count = 0
            lines = data_base.read().splitlines()
            for line in lines:
                count += 1
                print(str(count)+')' + line)
            print(str(count+1) + ')Back to main menu')
        return count

    def wallet_ch(self, choise):
        with open('wallet.txt', 'r') as data_base:
            lines = data_base.read().splitlines()
            wallet = lines[choise - 1]
        return wallet

    def wallet_del(self,choise):
        with open('wallet.txt', 'r') as data_base:
                name = []
                lines = data_base.read().splitlines()
                name = lines[choise - 1]
        self.delete(name)
