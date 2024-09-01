class Calculadora:
    def __init__(self, valor_a=0, valor_b=0, operacao='+'):
        self.__valor_a = valor_a
        self.__valor_b = valor_b
        self.__operacao = operacao

    @property
    def valor_a(self):
        return self.__valor_a

    @valor_a.setter
    def valor_a(self, valor_a):
        self.__valor_a = valor_a

    @property
    def valor_b(self):
        return self.__valor_b

    @valor_b.setter
    def valor_b(self, valor_b):
        self.__valor_b = valor_b

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    @staticmethod
    def validar_operacao(operacao):
        operacoes_validas = ('+', '-', '*', '/')
        return operacao in operacoes_validas

    def calcular(self):
        if not Calculadora.validar_operacao(self.operacao):
            print("Operação inválida!")
            exit()

        if self.operacao == '+':
            return self.valor_a + self.valor_b
        elif self.operacao == '-':
            return self.valor_a - self.valor_b
        elif self.operacao == '*':
            return self.valor_a * self.valor_b
        elif self.operacao == '/':
            if self.valor_b == 0:
                print("Não é possível dividir por zero!")
                exit()
            return self.valor_a / self.valor_b

    def mostrar_resultado(self):
        resultado = self.calcular()
        if resultado.is_integer():
            resultado = int(resultado)

        print(f"{self.valor_a} {self.operacao} {self.valor_b} = {resultado}")

    def entrada_dados(self):
        while True:
            try:
                self.valor_a = float(input("Digite o valor A: "))
                if self.valor_a.is_integer():
                    self.valor_a = int(self.valor_a)

                self.operacao = input("Digite a operação (+, -, *, /): ")
                if not Calculadora.validar_operacao(self.operacao):
                    print("Operação inválida!")
                    exit()

                self.valor_b = float(input("Digite o valor B: "))
                if self.valor_b.is_integer():
                    self.valor_b = int(self.valor_b)
                break

            except ValueError:
                print("Entrada inválida! Por favor, insira números válidos.")
