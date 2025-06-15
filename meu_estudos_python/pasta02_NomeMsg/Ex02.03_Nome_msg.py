"""
Crie um script python que leia o nome de uma pessoa e mostre uma
mensagem de boas-vidas de acordo com o valor digitado
"""

class Saudação:
	def __init__(self):
		self.nome = ""


	def ler_nome(self):
		self.nome = str(input("Qual é o seu nome?: ")).strip().capitalize()
		return self.nome


	def msg(self):
		mensagem = f"Olá, {self.nome} seja bem-vindo"
		print(mensagem)

saudação = Saudação()
nome_usuário = saudação.ler_nome()
saudação.msg()
