"""
Crie um algorítimo que lei um número e mostre o seu
dobro, triplo e raiz quadrada
"""

def calcula_dobro(x):
	return x * 2


def calcula_triplo(y):
	return y * 3


def calcula_raiz(h):
	return h ** (1/2)


def mostra_calculo(a, b, c):
	print(f"O dobro {a}\nO triplo {b}\nA raiz {c}.")



# Programa principal
num = int(input("Digite um número para ver o seu dobro, triplo e raiz: "))

dobro = calcula_dobro(num)
triplo = calcula_triplo(num)
raiz = calcula_raiz(num)
mostra_calculo(dobro, triplo, raiz)
