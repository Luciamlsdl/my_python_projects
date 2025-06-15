"""
Crie um script  python que leia dois números e
tente mostrar a soma entre eles.
"""

def somar(n1, n2):
	soma = n1 + n2
	return soma

def mostrar_soma(soma):
	print(f"A soma dos valores é = {soma}.")


# Programa principal
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

soma = somar(n1, n2)
mostrar_soma(soma)
