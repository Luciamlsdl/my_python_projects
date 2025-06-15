"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""

# Este programa vai estar na sua forma mais simples

try:
	n = int(input("Digite um número inteiro para ver sua tabuada: "))
except ValueError:
	print("ERRO: Por favor, insira um número inteiro válido!")
	exit()


for x in range(0, 11):
	print(f"{x } x {n} = {x * n}")


