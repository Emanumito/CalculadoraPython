class Operacao:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0

    def obter_valores(self):
        try:
            self.valor1 = float(input("Digite o primeiro valor: "))
            self.valor2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            self.obter_valores()

class Soma(Operacao):
    def calcular(self):
        return self.valor1 + self.valor2

class Subtracao(Operacao):
    def calcular(self):
        return self.valor1 - self.valor2

class Multiplicacao(Operacao):
    def calcular(self):
        return self.valor1 * self.valor2

class Divisao(Operacao):
    def calcular(self):
        if self.valor2 == 0:
            return "Erro: Divisão por zero."
        return self.valor1 / self.valor2

class Raiz(Operacao):
    def calcular(self):
        if self.valor1 < 0 and self.valor2 % 2 == 0:
            return "Erro: Raiz par de número negativo."
        return pow(self.valor1, 1 / self.valor2)