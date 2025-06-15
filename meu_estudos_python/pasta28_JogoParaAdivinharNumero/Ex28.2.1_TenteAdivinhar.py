"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
from colorama import init, Fore, Style

# Inicializa o colorama no início do programa
init(autoreset=True) # autoreset=True garante que a cor volte ao normal após cada print

# --- Constantes de Cores ---
VERDE = Fore.GREEN
AZUL = Fore.BLUE
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN

# --- Constantes do Jogo ---
NUM_MINIMO = 0
NUM_MAXIMO = 5

def apresentação():
    print()
    print(AMARELO + "-=-" * 13)
    print(CIANO + "seja bem vindo a o jogo de adivinhação".upper())
    print(AMARELO + "-=-" * 13)
    sleep(2) # Tempo de apresentação um pouco menor para agilizar

def escolhaComputador():
    return randint(NUM_MINIMO, NUM_MAXIMO)

def conviteDoComputador():
    print(VERDE + "\nCOMPUTADOR")
    print(AZUL + f"-->Vou pensar em um número de {NUM_MINIMO} a {NUM_MAXIMO}. Tente adivinhar!")
    sleep(2) # Tempo de convite um pouco menor

def escolhaDoJogador():
    while True:
        try:
            jogador = int(input(AMARELO + f"Em que número eu pensei (entre {NUM_MINIMO} e {NUM_MAXIMO})?: "))
            if NUM_MINIMO <= jogador <= NUM_MAXIMO:
                return jogador
            else:
                print(VERMELHO + f"O valor digitado deve ser entre {NUM_MINIMO} e {NUM_MAXIMO}.")
        except ValueError:
            print(VERMELHO + "Entrada inválida. Por favor, digite um número inteiro.")

def tempoParaPensar():
    print()
    print(AMARELO + "Processando..")
    sleep(1) # Tempos mais curtos
    print("Processando....")
    sleep(1)
    print("Processando......")
    sleep(1)
    print()

def exibirVencedor(computador, jogador):
    if jogador == computador:
        print(VERDE + "Parabéns! Você venceu!")
    else:
        print(VERMELHO + f"Vitória do Computador! Eu pensei no número {computador}, não no {jogador}.")
    print()

# --- Programa Principal ---
apresentação()

jogar_novamente = True
while jogar_novamente:
    computador = escolhaComputador()
    conviteDoComputador()
    jogador = escolhaDoJogador()
    tempoParaPensar()
    exibirVencedor(computador, jogador)

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