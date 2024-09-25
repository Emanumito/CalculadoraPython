import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from menu.menu import Menu

class Main:
    def __init__(self):
        self.menu = Menu()

    def iniciar(self):
        continuar = True
        while continuar:
            self.menu.exibir_menu()
            try:
                opcao = int(input("Escolha uma opção: "))
                continuar = self.menu.executar_operacao(opcao)
                if continuar:
                    continuar = self.perguntar_continuar()
            except ValueError:
                print("Por favor, insira uma opção válida.")

    def perguntar_continuar(self):
        while True:
            resposta = input("Deseja fazer uma nova operação (S/N)? ").strip().upper()
            if resposta == 'S':
                return True
            elif resposta == 'N':
                return False
            else:
                print("Resposta inválida. Por favor, responda com 'S' ou 'N'.")

if __name__ == "__main__":
    app = Main()
    app.iniciar()