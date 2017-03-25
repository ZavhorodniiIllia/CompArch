
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

    def plus(self,money,op_name):
        file = open('wallet.txt', 'a')
        file.write(money +':'+ op_name)

    def minus(self, money, op_name):
        file = open('wallet.txt', 'a')
        file.write(money +':'+ op_name)

    def history(self):
        file = open('wallet.txt', 'r')
        file.read()


