class Divisao:
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

    def dividir(self):
        return self.valor1 / self.valor2


# Exemplo de uso
if __name__ == "__main__":
    calc = Divisao()
    calc.obter_valores()
    resultado = calc.dividir()
    print(f"O resultado da soma é: {resultado}")
