"""
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
# Este programa sera feito no formato de função

# Conversões
# km = num / 1000  # Quilômetros
# hm = num / 100   # Hectômetros
# dam = num / 10   # Decâmetros
# dm = num * 10    # Decímetros
# cm = num * 100   # Centímetros
# mm = num * 1000  # Milímetros


def calcular_conversões(metros):
	return{
		"quilômetros": metros / 1000,
		"hectômetros": metros / 100,
		"decâmetros": metros / 10,
		"decímetros": metros * 10,
		"centímetros": metros * 100,
		"milímetros": metros * 1000
	}


def mostrar_conversões(conversões):
	for unidade, valor in conversões.items():
		print(f"Valor em {unidade.capitalize()}: {valor:.2f}")


# Programa principal
try:
	num = float(input("Digite o valor em metros para ser convertido: "))
	if num < 0:
		print("Por favor, insira um valor positivo!")
	else:
		conversões = calcular_conversões(num)
		mostrar_conversões(conversões)
except ValueError:
	print("Erro: Por favor, insira um número válido!")
