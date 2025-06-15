"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""

#Este programa esta em sua forma simples

numero = int(input("\nDigite um número inteiro para ver se ele é par ou ímpar: "))


if numero % 2 == 0:
    print(f"O número {numero} é um número par!")
else:
    print(f"O número {numero} é um número ímpar!")

