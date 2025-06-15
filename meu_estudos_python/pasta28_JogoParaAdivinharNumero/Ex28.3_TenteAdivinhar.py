"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

#Este programa esta em sua forma de classe 
# Biblioteca Random usando Randint para embaralhar os números
# Biblioteca Time para colocar tempo no código
# Biblioteca Colorama para dar cor ao código


from random import randint
from time import sleep
from colorama import init, Fore, Style

init(autoreset=True)

VERDE = Fore.GREEN
AZUL = Fore.BLUE
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN



class JogoDeAdivinhação:
    def __init__(self, min_num=0, max_num=5):
        self.computador = 0
        self.jogador = 0
        self.NUM_MINIMO = min_num
        self.NUM_MAXIMO = max_num


    def apresentação(self):
        print()
        print(AMARELO + "-=-" * 13)
        print(CIANO + "seja bem vindo a o jogo de adivinhação".upper())
        print(AMARELO + "-=-" * 13)
        sleep(2)


    def escolhaComputador(self):
        self.computador = randint(self.NUM_MINIMO, self.NUM_MAXIMO)
        return self.computador
    

    def conviteDoComputador(self):
        print(VERDE + "\nCOMPUTADOR")
        print(AZUL + f"-->Vou pensar em um número de {self.NUM_MINIMO} a {self.NUM_MAXIMO}. Tente adivinhar!")
        sleep(2)


    def escolhaDoJogador(self):
        while True:
            try:
                self.jogador = int(input(AMARELO + f"Em que número eu pensei (entre {self.NUM_MINIMO} e {self.NUM_MAXIMO})?: "))
                if self.NUM_MINIMO <= self.jogador <= self.NUM_MAXIMO:
                    return self.jogador
                else:
                    print(VERMELHO + f"O valor digitado deve ser entre {self.NUM_MINIMO} e {self.NUM_MAXIMO}.")
            except ValueError:
                print(VERMELHO + "Entrada inválida. Por favor, digite um número inteiro.")


    def tempoParaPensar(self):
        print()
        print(AMARELO + "Processando..")
        sleep(1)
        print(AMARELO+"Processando....")
        sleep(1)
        print(AMARELO+"Processando......")
        sleep(1)
        print()


    def exibirVencedor(self):
        if self.jogador == self.computador:
            print(VERDE + "Parabéns! Você venceu!")
        else:
            print(VERMELHO + f"Vitória do Computador! Eu pensei no número {self.computador}, não no {self.jogador}.")
        print()


#Programa principal
if __name__ == "__main__":
    jogo = JogoDeAdivinhação()
    jogo.apresentação()
    while True:
        jogo.escolhaComputador()
        jogo.conviteDoComputador()
        jogo.escolhaDoJogador()
        jogo.tempoParaPensar()
        jogo.exibirVencedor()

        while True:
            parar = str(input(CIANO + "Deseja jogar novamente? Digite (S) para Sim ou (N) para Não: ")).strip().upper()
            if parar == "N":
                jogar_novamente = False
                print(AMARELO + "Obrigado por jogar! Até a próxima!")
                break
            elif parar == "S":
                break
            else:
                print(VERMELHO + "Opção inválida! Digite 'S' para Sim ou 'N' para Não!")

        if parar == "N":
            break
