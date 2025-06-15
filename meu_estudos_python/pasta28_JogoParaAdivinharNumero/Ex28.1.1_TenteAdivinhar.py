"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

# Definindo constantes para os limites do jogo
NUM_MINIMO = 0
NUM_MAXIMO = 5

print("-=" * 25)
print(f"Vou pensar em um número de {NUM_MINIMO} a {NUM_MAXIMO}. Tente adivinhar!")
print("-=" * 25)

computador = randint(NUM_MINIMO, NUM_MAXIMO)
jogador = -1 # Inicializa com um valor fora do range para entrar no loop

# Loop para garantir que o usuário digite um número válido
while True:
    try:
        jogador = int(input("\nEm que número eu pensei?: "))
        if NUM_MINIMO <= jogador <= NUM_MAXIMO: # Verifica se o número está dentro do range
            break # Sai do loop se a entrada for válida
        else:
            print(f"Por favor, digite um número entre {NUM_MINIMO} e {NUM_MAXIMO}.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Processando..")
sleep(1)
print("Processando....")
sleep(1)
print("Processando......")
sleep(2)

if jogador == computador:
    print("Parabéns! Você venceu!")
else:
    print(f"Computador venceu! Eu pensei no número {computador}, não no {jogador}.")