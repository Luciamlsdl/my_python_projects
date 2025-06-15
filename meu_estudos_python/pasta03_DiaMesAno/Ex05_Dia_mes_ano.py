"""
Este código é um exercício de coleta de dados que 
visa coletar os dados de uma pessoa Nome,dia,mês e ano de aniversario
"""

class Dados_pessoais:
	def __init__(self):
		"""
		Inicializa uma nova instância de classe DadosPessoais.
		"""
		self.nome = ""
		self.dia = 0
		self.mes = ""
		self.ano = 0


	def ler_nome(self):
		"""
		Lê o nome do usuário e armazena no atributo self.nome.
		"""
		try:
			self.nome = str(input("Nome: ")).strip().capitalize()
		except Exception as e:
			print(f"Erro ao ler o nome: {e}")


	def ler_dia(self):
		"""
		Lê o dia de aniversário do usuário e armazena no atributo self.dia.
		Verifica se o dia é um número válido entre 1 a 31.
		"""
		while True:
			try:
				dia_input = input("Dia: ").strip()
				if dia_input.isdigit():
					self.dia = int(dia_input)
					if 1 <= self.dia <= 31:
						break
					else:
						print("Por favor, digite um dia válido (1-31).")
				else:
					print("Por favor, digite um número válido.")
			except Exception as e:
				print(f"Erro ao ler o dia: {e}")


	def ler_mes(self):
		"""
		Lê o mês de aniversário do usuário e armazena no atributo self.mes.
		Verifica se o mês é um texto válido (nome do mês).
		"""
		meses_validos = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", 
				"Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
		while True:
			try:
				mes_input = input("Mês: ").strip().capitalize()
				if mes_input.isalpha():
					if mes_input in meses_validos:
						self.mes = mes_input
						break 
					else:
						print("Por favor, digite um mês válido")
				else:
					print("Por favor, digite o mês no formato de texto")
			except Exception as e:
				print(f"Erro ao ler mês: {e}")


	def ler_ano(self):
		"""
		Lê o ano de aniversário do usuário e armazena no atributo self.ano.
		Verifica se o ano é um número válido entre 1900 e 2025.
		"""
		while True:
			try:
				ano_input = input("Ano: ").strip()
				if ano_input.isdigit():
					self.ano = int(ano_input)
					if 1900 <= self.ano <= 2025:
						break
					else:
						print("Por favor, digite o ano válido (1900-2025).")
				else:
					print("Por favor, digite um número válido.")
			except Exception as e:
				print(f"Erro ao ler o ano: {e}")


	def mostrar_dados(self):
		"""
		Exibe os dados coletados do usuário.
		"""
		dados.m = f"Dodos de {self.nome}.\n{self.dia}/{self.mes}/{self.ano}"
		print(dados.m)


# Código principal
dados = Dados_pessoais()
dados.ler_nome()
dados.ler_dia()
dados.ler_mes()
dados.ler_ano()
dados.mostrar_dados()
