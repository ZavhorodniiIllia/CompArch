from datetime import date, time
import datetime

class Model:
    def __init__(self, name):
        self.load(name)

    def load(self,name):
        file = open('wallet.txt', 'r')

    def new_wallet(self, name, balance):
        """Функция для создания файла для нового кошелька и запись его названия в список кошельков"""
        file=open(name + '.txt', 'w')
        file.write(name + '\n')
        file.write(balance + ' (UAH)' + '\n')
        file.close()
        data_base=open('wallet.txt','a')
        data_base.write(name + '\n')
        data_base.close()

    def wallets(self):
        """Функция для вывода всех кошельков и их нумерацией"""
        count=0
        data_base = open('wallet.txt', 'r')
        line = data_base.readlines()
        for i in line:
            count+=1
            print(str(count)+')' + i)

    def ch_wal(self):
        """Функция для выбора кошелька"""
        count = 0
        var=''
        data_base = open('wallet.txt', 'r')
        line = data_base.readlines()
        while 1:
            num = input('Choose wallet`s number:')
            for i in line:
                count += 1
                if int(count)==int(num):
                    for j in i:
                        if j != '\n':
                            var+=j
                    return var
            print('Incorrect number. Please try again')

    def chek(self,name):
        """Функция для вывода текущего баланса"""
        lines=0
        file = open(name + '.txt', 'r')
        line = file.readlines()
        lines=len(line)
        return(line[lines-1])

    def minus(self,money,op_name,balance,coof,name):
        """Функция для записи операции снятия денег и нового баланса"""
        file = open(name + '.txt', 'a')
        now_time = datetime.datetime.now()
        if coof==1:
            file.write('-' + str(money) + ' UAH' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
        elif coof==2:
            file.write('-' + str(money)+' USD' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            money*=27
        elif coof==3:
            file.write('-' + str(money) + ' EUR' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            money *= 29.5
        bm=balance-money
        file.write(str(bm)+' (UAH)' + '\n')

    def plus(self,money,op_name,balance,coof,name):
        """Функция для записи операции пополнения денег и нового баланса"""
        file = open(name + '.txt', 'a')
        now_time = datetime.datetime.now()
        if coof==1:
            file.write('+' + str(money) + ' UAH' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
        elif coof==2:
            file.write('+' + str(money)+' USD' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            money*=27
        elif coof==3:
            file.write('+' + str(money) + ' EUR' + ': ' + op_name + '; operation time: ' + now_time.strftime("%d.%m.%Y %I:%M %p") + '\n')
            money *= 29.5
        bm=balance+money
        file.write(str(bm)+ ' (UAH)' + '\n')

    def history(self,name):
        """Функция для вывода истории кошелька"""
        file = open(name + '.txt', 'r')
        print(file.read())

    def str_to_float(self,money):
        """Функция для изменения string в float"""
        mon=''
        for i in money:
            if i!=' ':
                mon+=i
            else:
                break
        return mon