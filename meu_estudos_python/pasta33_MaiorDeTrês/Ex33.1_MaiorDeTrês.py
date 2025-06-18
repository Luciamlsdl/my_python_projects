"""
Faça um programa que leia três números e mostre qual é o mair e o menor valor.
"""

#Este programa esta em sua forma simples

print("\n-> Maior e menor número de três números".upper())

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Terceiro número: "))

maior_numero = max(numero1, numero2, numero3)
menor_numero = min(numero1, numero2, numero3)

print(f"O maior número = {maior_numero}.")
print(f"O menor número = {menor_numero}.")