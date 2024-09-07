from operacoes.operacoes import Soma, Subtracao, Multiplicacao, Divisao

class Menu:
    def __init__(self):
        self.operacoes = {
            1: Soma(),
            2: Subtracao(),
            3: Multiplicacao(),
            4: Divisao()
        }

    def exibir_menu(self):
        print("Bem vindo a Calculadora do projeto\n")
        print("Menu de Operações:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

    def executar_operacao(self, opcao):
        if opcao in self.operacoes:
            operacao = self.operacoes[opcao]
            operacao.obter_valores()
            resultado = operacao.calcular()
            print(f"O resultado da operação é: {resultado}")
        elif opcao == 5:
            print("Saindo...")
            return False
        else:
            print("Opção inválida.")
        return True