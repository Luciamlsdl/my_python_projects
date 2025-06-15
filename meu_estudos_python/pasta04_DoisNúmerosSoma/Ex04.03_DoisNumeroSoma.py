"""
Crie um script  python que leia dois números e
tente mostrar a soma entre eles.
Desta vez usando classe
"""

class Somando:
	def __init__(self):
		self.num1 = 0
		self.num2 = 0
		self.soma = 0


	def primeiro_val(self):
		self.num1 = int(input("Primeiro valor: "))


	def segundo_val(self):
		self.num2 = int(input("Segundo valor: "))


	def somar_val(self):
		self.soma = self.num1 + self.num2
		return self.soma


	def mostrar_val(self):
		print(f"A soma dos valores = {self.soma}.")


# Programa principal
somando = Somando()
somando.primeiro_val()
somando.segundo_val()
somando.somar_val()
somando.mostrar_val()


