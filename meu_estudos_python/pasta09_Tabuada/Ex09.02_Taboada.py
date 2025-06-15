"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""

# Este programa vai estar na sua forma mais de função

def cal_tabuada(x):
	print("-" * 20)
	for i in range(0, 11):
		print(f"{i:2} x {x} = {i * x}")
	print("-" * 20)


# Programa principal
try:
	n = int(input("Digite um valor para ver sua tabuada: "))
except ValueError:
	print("Erro: Por favor, insira um valor inteiro valido")
	exit()

cal_tabuada(n)

