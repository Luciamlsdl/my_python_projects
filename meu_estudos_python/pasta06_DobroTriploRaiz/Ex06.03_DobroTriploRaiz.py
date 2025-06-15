"""
Crie um algorítimo que lei um número e mostre o seu
dobro, triplo e raiz quadrada
"""

class Dados_numéricos:
	def __inti__(self):
		self.num = 0
		self.dobro = 0
		self.triplo = 0
		self.raiz = 0


	def ler_val(self):
		self.num = int(input("Digite um número para ver seu Dobro, triplo e Raiz: "))
		return self.num


	def dobro_val(self):
		self.dobro = self.num * 2
		return self.dobro


	def triplo_val(self):
		self.triplo = self.num * 3
		return self.triplo


	def raiz_val(self):
		self.raiz = self.num ** (1/2)
		return self.raiz


	def mostrar_val(self):
		print(f"O dobro de {self.num} é = {self.dobro}")
		print(f"O triplo de {self.num} é = {self.triplo}")
		print(f"A raiz quadrada de {self.num} é = {self.raiz}")



# Programa principal
dados = Dados_numéricos()
dados.ler_val()
dados.dobro_val()
dados.triplo_val()
dados.raiz_val()

dados.mostrar_val()




