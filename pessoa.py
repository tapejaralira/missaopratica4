class Pessoa:
    def __init__(self, nome, numero_conta, data_abertura_conta, status):
        self.__nome = nome
        self.__numero_conta = numero_conta
        self.__data_abertura_conta = data_abertura_conta
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @property
    def data_abertura_conta(self):
        return self.data_abertura_conta

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def status(self):
        return self.__status

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_abertura_conta.setter
    def data_abertura_conta(self, data_abertura_conta):
        self.__data_abertura_conta = data_abertura_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    @status.setter
    def status(self, status):
        self.__status = status

    def imprimir_valores(self):
        attrs = vars(self)
        print('\nInstancia da classe Pessoa: ')
        print(', '.join("%s: %s" % item for item in attrs.items()))
