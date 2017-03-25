
class Model:
    def __init__(self, name):
        self.load(name)

    def new_wallet(self, name, balance):
        file=open('wallet.txt', 'r')
        file.write(name)
        file.write(balance)
        file.close()
    def load(self,name):
        file=open('wallet.txt','wr')

    def balance(self):
        file = open('wallet.txt', 'wr')
        line=file.readline()
        print(line[1])

    def plus(self,money,op_name):
        file = open('wallet.txt', 'wr')
        file.write(money + op_name)

    def minus(self, money, op_name):
        file = open('wallet.txt', 'wr')
        file.write(money + op_name)

    def history(self):
        file = open('wallet.txt', 'wr')
        file.read()


