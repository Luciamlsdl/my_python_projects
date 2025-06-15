"""
faça um programa que tenha um número inteiro
e mostre na tela o seu sucessor e seu antecessor
"""

# Script na sua forma de classe

class AntecessorSucessor:
	"""
	Inicializa uma nova instância de classe AntecessorSucessor
	"""
	def __init__(self):
		self.num = 0
		self.ant = 0
		self.sus = 0


	def ler_val(self):
		"""
		Lê o número digitado e armazena no atributo self.num
		"""
		numero = int(input("Digite o número para para ver seu antecessor e seu sucessor: "))
		self.num = numero


	def antecessor(self):
		"""
		Armazena o antecessor do atributo self.num no atributo self.ant
		"""
		self.ant = self.num - 1
		return self.ant


	def sucessor(self):
		"""
		Armazena o sucessor do atributo self.num no atributo self.sus
		"""
		self.sus = self.num + 1
		return self.sus


	def mostrar_val(self):
		"""
		Exibe o sucessor e o antecessor de self.num
		"""
		print(f"O antecessor de {self.num} é = {self.ant}.")
		print(f"O sucessor de {self.num} é = {self.sus}.")


# Programa principal
chamada = AntecessorSucessor()
chamada. ler_val()
chamada.antecessor()
chamada.sucessor()
chamada.mostrar_val()
