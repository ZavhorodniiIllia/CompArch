class Model:
    def __init__(self, name):
        self.load(name)

    def load(self,name):
        file = open('wallet.txt', 'r')

    def new_wallet(self, name, balance):
        file=open(name + '.txt', 'w')
        file.write(name + '\n')
        file.write(balance + ' (UAH)' + '\n')
        file.close()
        data_base=open('wallet.txt','a')
        data_base.write(name + '\n')
        data_base.close()

    def wallets(self):
        data_base = open('wallet.txt', 'r')
        print(data_base.read())

    def balance(self,name):
        file = open(name + '.txt', 'r')
        line=file.readlines()
        print(line[1])

    def chek(self,name):
        lines=0
        file = open(name + '.txt', 'r')
        line = file.readlines()
        lines=len(line)
        return(line[lines-1])

    def minus(self,money,op_name,balance,coof,name):
        file = open(name + '.txt', 'a')
        if coof==1:
            file.write('-' + str(money) + ' UAH' + ': ' + op_name + '\n')
        elif coof==2:
            file.write('-' + str(money)+' USD' +': '+ op_name + '\n')
            money*=27
        elif coof==3:
            file.write('-' + str(money) + ' EUR' + ': ' + op_name + '\n')
            money *= 29.5
        bm=balance-money
        file.write(str(bm)+' (UAH)' + '\n')

    def plus(self,money,op_name,balance,coof,name):
        file = open(name + '.txt', 'a')
        if coof==1:
            file.write('+' + str(money) + ' UAH' + ': ' + op_name + '\t')
        elif coof==2:
            file.write('+' + str(money)+' USD' +': '+ op_name + '\n')
            money*=27
        elif coof==3:
            file.write('+' + str(money) + ' EUR' + ': ' + op_name + '\n')
            money *= 29.5
        bm=balance+money
        file.write(str(bm)+ ' (UAH)' + '\n')

    def history(self,name):
        file = open(name + '.txt', 'r')
        print('\n' + file.read())

    def str_to_float(self,money):
        mon=''
        for i in money:
            if i!=' ':
                mon+=i
            else:
                break
        return mon
