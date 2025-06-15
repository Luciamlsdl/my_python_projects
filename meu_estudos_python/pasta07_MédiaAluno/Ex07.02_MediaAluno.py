"""
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre sua média.
"""

def valores_notas(a, b):
	media = (a + b) / 2
	return media


def mostra_media(x):
	print(f"A média do aluno segunda suas duas notas é = {x:.2f}.")




# Programa principal
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

nota_val = valores_notas(nota1, nota2)
mostra_media(nota_val)
