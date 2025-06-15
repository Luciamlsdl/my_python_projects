"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Este código está em sua forma de função e usando a importação do modulo math.

from math import radians, sin, cos, tan

def calculando_valores(x):
    seno = sin(radians(x))
    cosseno = cos(radians(x))
    tangente = tan(radians(x))
    return seno, cosseno, tangente


def mostrar_valores(a, b, c):
    print(f"O seno do ângulo é = {a:.2f}.\n"
          f"O cosseno do ângulo é = {b:.2f}\n"
          f"A tangente do ângulo é = {c:.2f}.")


def ler_angulo():
    while True:
        try:
            angulo = float(input("\nDigite um ângulo qualquer: °"))
            if angulo >= 0:
                return angulo
        except ValueError:
            print("Por favor! Digite um valor válido para o ângulo!")

# Programa principal
angulo = ler_angulo()

seno, cosseno, tangente = calculando_valores(angulo)
mostrar_valores(seno, cosseno, tangente)

