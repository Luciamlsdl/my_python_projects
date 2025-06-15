"""
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
# Este programa sera feito no formato de classe

# Conversões
# km = num / 1000  # Quilômetros
# hm = num / 100   # Hectômetros
# dam = num / 10   # Decâmetros
# dm = num * 10    # Decímetros
# cm = num * 100   # Centímetros
# mm = num * 1000  # Milímetros


class Conversão:
	def __init__(self):
		self.num = 0


	def ler_num(self):
		try:
			self.num = float(input("Digite o valor em metros para ser convertido: "))
			if self.num < 0:
				print("Por favor, insira um valor positivo!")
				return False
			return True
		except ValueError:
			print("ERRO: Por favor, insira um número válido!")
			return False



	def acucular_valor(self):
		return{
		"quilômetros": self.num / 1000,
		"hectômetros": self.num / 100,
		"decâmetros": self.num / 10,
		"decímetros": self.num * 10,
		"centímetros": self.num * 100,
		"milímetros": self.num * 100
		}


	def mostrar_val(self):
		conversões = self.acucular_valor()
		for unidade, valor in conversões.items():
			print(f"Valor em {unidade}: {valor:.2f}.")

# Programa principal
conversão = Conversão()
if conversão.ler_num():
	conversão.mostrar_val()

