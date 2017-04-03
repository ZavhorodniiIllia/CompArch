from datetime import date, time
import datetime

class Model:
    def __init__(self, name):
        self.load(name)

    def load(self,name):
        file = open('wallet.txt', 'r')

    def new_wallet(self, name, balance):
        """Функция для создания файла для нового кошелька и запись его названия в список кошельков
            В функцию передается имя нового кошелька и баланс
        """
        with open(name + '.txt', 'w') as file:
            file.write(name + '\n')
            file.write(balance + ' (UAH)' + '\n')
        with open('wallet.txt', 'a') as data_base:
            data_base.write(name + '\n')

    def chek(self,name):
        """Функция для вывода текущего баланса
            В функцию передается имя кошелька
            Функция возвращает строку в которой храниться баланс
        """
        lines = 0
        with open(name + '.txt', 'r') as file:
            line = file.readlines()
            lines = len(line)
            return(line[lines-1])

    def minus(self,money,op_name,balance,coof,name):
        """Функция для записи операции снятия денег и обновления баланса
            В функцию предается количество денег, название операции, текущий баланс, флаг валюты и имя кошелька
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
            bm=balance-money
            file.write(str(bm)+' (UAH)' + '\n')

    def plus(self,money,op_name,balance,coof,name):
        """Функция для записи операции пополнения денег и обновления баланса
            В функцию предается количество денег, название операции, текущий баланс, флаг валюты и имя кошелька
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
            bm=balance+money
            file.write(str(bm) + ' (UAH)' + '\n')

    def history(self,name):
        """Функция для вывода истории кошелька
            В функцию передается название кошелька
            Функция аозвращает полную историю операций
        """
        with open(name + '.txt', 'r') as file:
            print(file.read())

    def str_to_float(self,money):
        """Функция для изменения string в float
            В функцию передается значение типа strinig
            Функция возвращает значение типа float
        """
        mon=''
        for i in money:
            if i != ' ':
                mon += i
            else:
                break
        return mon
