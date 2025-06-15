"""
Crie um scrip python que leia o dia, mês e ano de nascimento de uma pessoa e
mostre uma mensagem com a data formatada
"""

class Dados_pessoais:

	def  __init__(self):
		self.nome = ""
		self.dia = ""
		self.mes = ""
		self.ano = ""


	def ler_nome(self):
		self.nome = str(input("Nome?: ")).strip().capitalize()
		return self.nome


	def ler_dia(self):
		self.dia = int(input("Dia?: "))
		return self.dia


	def ler_mes(self):
		self.mes = str(input("Mês?: ")).strip().capitalize()
		return self.mes


	def ler_ano(self):
		self.ano = int(input("Ano?: "))


	def mostrar_dados(self):
		print(f"Olá, {self.nome}")
		print(f"Dia de nascimento {self.dia}")
		print(f"Mês de nascimento {self.mes}")
		print(f"Ano de nascimento {self.ano}")


# Programa principal
dados = Dados_pessoais()
nome_usuário = dados.ler_nome()
dia_usuário = dados.ler_dia()
mes_usuário = dados.ler_mes()
ano_usuário = dados.ler_ano()
dados.mostrar_dados()


