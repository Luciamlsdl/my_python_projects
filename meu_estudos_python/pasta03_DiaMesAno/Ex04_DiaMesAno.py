"""
Crie um scrip python que leia o dia, mês e ano de nascimento de uma pessoa e
mostre uma mensagem com a data formatada
"""
# Este código é o código mais aprimorado

class DadosPessoais:
	def __init__(self):
		self.nome = ""
		self.dia = 0
		self.mes = ""
		self.ano = 0


	def ler_nome(self):
		self.nome = str(input("Nome?: ")).strip().capitalize()


	def ler_dia(self):
		while True:
			dia_input = input("Dia?: ").strip()
			if dia_input.isdigit():
				self.dia = int(dia_input)
				if 1 <= self.dia <= 31:
					break
				else:
					print("Por favor, digite umm dia válido (1-31).")
			else:
				print("Por favor, digite um número válido.")


	def ler_mes(self):
		self.mes = str(input("Mês?: ")).strip().capitalize()


	def ler_ano(self):
		while True:
			ano_input = input("Ano?: ").strip()
			if ano_input.isdigit():
				self.ano = int(ano_input)
				if 1900 <= self.ano <= 2100:
					break
				else:
					print("Por favor, digite um ano válido (1900-2100).")
			else:
				print("Por favor, digite um numero válido")


	def mostrar_dados(self):
		print(f"Olá, {self.nome}")
		print(f"Data de nascimento: {self.dia:02d}/{self.mes}/{self.ano}")


# programa principal
dados = DadosPessoais()
dados.ler_nome()
dados.ler_dia()
dados.ler_mes()
dados.ler_ano()
dados.mostrar_dados()


