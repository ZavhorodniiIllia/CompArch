from controller import Controller, Model

data_base = Model('wallet.txt')
data_controller = Controller(data_base)
data_controller.main()