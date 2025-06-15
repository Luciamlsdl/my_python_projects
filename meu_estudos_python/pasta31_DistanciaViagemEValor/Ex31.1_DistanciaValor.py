"""
Escreva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem cobrando R$:0,50 por km para viagem de até 200Km
e R$:0,45 para viagem mais longas.
"""

#Este programa está em forma simples

print("\nBem vindo! Ao gerenciador de viagem!".upper())
print()

valor_normal = 0.50
valor_longa = 0.45

distancia = int(input("Qual é a distancia de sua viagem? Km: "))

if distancia > 200:
    preço = distancia * valor_longa
else:
    preço = distancia * valor_normal

print(f"A distancia de sua viagem é de {distancia}Km e o valor é R$:{preço:.2f}.")
