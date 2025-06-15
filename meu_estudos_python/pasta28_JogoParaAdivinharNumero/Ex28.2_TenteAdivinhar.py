"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

# Este código esta em sua forma de função 
# Biblioteca Random usando Randint para embaralhar os números
# Biblioteca Time para colocar tempo no código
# Biblioteca Colorama para dar cor ao código


from random import randint
from time import sleep
from colorama import init, Fore, Style

VERDE = Fore.GREEN
AZUL = Fore.BLUE
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN

RESET = Style.RESET_ALL


def apresentação():
    print()
    print(AMARELO+"-=-" * 13 +RESET)
    print(CIANO+"seja bem vindo a o jogo de adivinhação".upper()+RESET)
    print(AMARELO+"-=-" * 13 +RESET)
    sleep(3)


def escolhaComputador():
    computador = randint(0, 5)
    return computador


def conviteDoComputador():
    print(VERDE+"\nCOMPUTADOR"+RESET)
    print(AZUL+"-->Vou pesar em um número de 0 a 5. Tente adivinhar!"+RESET)
    sleep(3)


def escolhaDoJogador():
    while True:
        try:
            jogador = int(input(AMARELO+"Enque número eu pesei?: "+RESET))
            if jogador < 0 or jogador > 5:
                print(VERMELHO+"O valor digitado não pode ser menor que 0 ou maior que 5"+RESET)
            else:    
                return jogador
        except ValueError:
            print(VERMELHO+"Por favor! Digite um valor válido!"+RESET)


def tempoPAraPesar():
    print()
    print(AMARELO+"Processando..")
    sleep(2)
    print("Processando....")
    sleep(2)
    print("Processando......"+RESET)
    sleep(2)
    print()


def lerOVencedor(computador, jogador):
    if jogador == computador:
        print(VERDE+"Para bens! Você venceu!"+RESET)
    else:
        print(VERDE+"Vitória Do Computador"+RESET)
    print()


# Programa principal
apresentação()

while True:
    computador = escolhaComputador()
    conviteDoComputador()
    jogador = escolhaDoJogador()
    tempoPAraPesar()
    lerOVencedor(computador, jogador)

    while True:
        parar = str(input(CIANO+"Digite (S) para continuar ou (N) para parar?: "+RESET)).strip().upper()[0]
        if parar == "N":
            break

        elif parar == "S":
            break

        else:
            print(VERMELHO+"Opção inválida! Digite 'S' para Sim ou 'N' para não!"+RESET)

    if parar == "N":
        break




