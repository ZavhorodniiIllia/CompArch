from controller import Controller, Model

name = Model('wallet.txt')
data_controller = Controller(name)
data_controller.main()