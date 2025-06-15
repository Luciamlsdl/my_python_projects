"""
Faça um programa que leia o comprimento do cateto oposto e o comprimento
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""

# Este programa está em seu formato de função e usando a importação do modulo math.hypot.


import math

def calcula_hipotenusa(x, y):
    hipotenusa = math.hypot(x, y)
    return hipotenusa
    

def mostrar_valor_hipotenusa(hipotenusa):
    print(f"E valor da hipotenusa é = {hipotenusa:.2f}.")
    print()


# Programa principal
while True:
    try:
        cateto_oposto = float(input("\nDigite o valor do cateto oposto: "))
        cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

        hipotenusa = calcula_hipotenusa(cateto_oposto, cateto_adjacente)
        mostrar_valor_hipotenusa(hipotenusa)
    except ValueError:
        print("Por favor! Digite um valor válidos!")
