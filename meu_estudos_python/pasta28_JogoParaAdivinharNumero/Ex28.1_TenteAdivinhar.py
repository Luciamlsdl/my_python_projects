"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

# Este programa esta em sua forma simples com importação da biblioteca random e time

from random import randint
from time import sleep

computador = randint(0, 5)
print("-="*25)
print("Vou pensar em um número de 0 a 5. Tente adivinhar!")
print("-="*25)
jogador = int(input("\nEm que número eu pensei?: "))

print("Processando..")
sleep(1)
print("Processando....")
sleep(1)
print("Processando......")
sleep(2)

if jogador == computador:
    print("Para bens! Você venceu!")
else:
    print("Computador venceu!")



