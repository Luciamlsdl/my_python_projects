"""
faça um programa que tenha um número inteiro
e mostre na tela o seu sucessor e seu antecessor
"""

# Script na sua forma de função

def numero1(num):
	sus = num + 1
	return sus


def numero2(num):
	ant = num - 1
	return ant


def mostrar_val(sus, ant):
	print(f"Sucessor {sus}.")
	print(f"Antecessor {ant}.")


# Programa principal
num = int(input("Digite o número para analise: "))
sucessor = numero1(num)
antecessor = numero2(num)
mostrar_val(sucessor, antecessor)

