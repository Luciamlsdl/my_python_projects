"""
Crie um programa que leia um número real qualquer pelo teclado e mostre ma  tela a sua porção inteira.
"""

# Este programa está em sua forma de função.

from math import trunc

def mostrar_valor(x):
    num = trunc(x)
    print(f"O valor inteiro do número digitado é = {num}")


# Programa principal

while True:
    try:
        número = float(input("\nDigite um número real para ver sua forma inteira: "))
        if número == int(número):
            print("Por favor! Digite um número real (com casa decimal)!")
        else:
            mostrar_valor(número)
    except ValueError:
        print("Por favor! Digite um valor válido!")
