""" Este código é um código de inicialização para quem quer aprender a programar 
Versão 01.02 
"""

class Mensagem:
	def __init__(self):
		"""
		Inicializa a classe Mensagem com o atributo self.msg.
		"""
		self.msg = ""


	def ler_msg(self):
		"""
		Lê a mensagem digitada pelo usuário e atribui a self.msg.
		"""
		self.msg = str(input("Digite a mensagem: ")).strip().capitalize()


	def mostrar_msg(self):
		"""
		Mostra a mensagem armazenada em self.msg.
		"""
		msg = self.msg
		print(msg)


# Código principal
if __name__ == "__main__":
	ler = Mensagem()
	ler.ler_msg()
	ler.mostrar_msg()


