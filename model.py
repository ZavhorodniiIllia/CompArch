
class Model:
    def __init__(self, name):
        self.load(name)

    def new_wallet(self, name, balance):
        file=open('wallet.txt', 'w')
        file.write(name + '\n')
        file.write(balance + '\n')
        file.close()

    def load(self,name):
        file=open('wallet.txt','r')

    def balance(self):
        file = open('wallet.txt', 'r')
        line=file.readlines()
        print(line[1])

    def chek(self):
        lines=0
        file = open('wallet.txt', 'r')
        line = file.readlines()
        lines=len(line)
        return(line[lines-1])

    def minus(self,money,op_name,balance):
        file = open('wallet.txt', 'a')
        file.write(str(money) +':'+ op_name + '\n')
        bm=balance-money
        file.write(str(bm) + '\n')

    def plus(self,money,op_name,balance):
        file = open('wallet.txt', 'a')
        file.write(str(money) +':'+ op_name + '\n')
        bm=balance+money
        file.write(str(bm) + '\n')

    def history(self):
        file = open('wallet.txt', 'r')
        print(file.read())


