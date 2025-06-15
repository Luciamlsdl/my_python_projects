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


def calcula_km(a):
	return a / 1000 # Quilômetros


def calcula_hm(b):
	return b / 100 # Hectômetros


def calcula_dam(c):
	return c / 10 # Decâmetros


def calcula_dm(d):
	return d * 10 # Decímetros


def calcula_cm(f):
	return f * 100 # Centímetros


def calcula_mm(g):
	return g * 100 # Milímetros


def mostrar_valores(a, b, c, d, f, g):
	print(f"Valor digitado convertido para Quilômetros é = {a}")
	print(f"Valor digitado convertido para Hectômetros é = {b}")
	print(f"Valor digitado convertido para Decâmetros é = {c}")
	print(f"Valor digitado convertido para Decímetros é = {d}")
	print(f"Valor digitado convertido para Centímetros é = {f}")
	print(f"Valor digitado convertido para Milímetros é = {g}")


# Programa principal
num = float(input("Digite o valor em metros par ser convertido em centímetros: "))

quilômetros = calcula_km(num)
hectômetros = calcula_hm(num)
decâmetros = calcula_dam(num)
decímetros = calcula_dm(num)
centímetros = calcula_cm(num)
milímetros = calcula_mm(num)
mostrar_valores(quilômetros, hectômetros, decâmetros,decímetros, centímetros, milímetros) 
