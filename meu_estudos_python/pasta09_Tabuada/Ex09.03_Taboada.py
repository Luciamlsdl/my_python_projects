"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""

# Este programa vai estar na sua forma de classe

class Tabuada:
	def __int__(self):
		self.num = 0



	def ler_valor(self):
		try:
			self.num = int(input("Digite um número inteiro para ver sua tabuada: "))
		except ValueError:
			print("ERRO: Digite um valor válido!")




# Programa principal
tabuada = Tabuada()
tabuada.ler_valor()



