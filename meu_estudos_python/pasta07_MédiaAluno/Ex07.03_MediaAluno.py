"""
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre sua média.
"""
# O mesmo programa agora em modelo de classe

class MediaAluno:
	def __init__(self):
		self.media = 0.0
		self.nota1 = 0.0
		self.nota2 = 0.0


	def ler_nota1(self):
		self.nota1 = float(input("Primeira nota do aluno: "))
		return self.nota1


	def ler_nota2(self):
		self.nota2 = float(input("Segunda nota  do aluno: "))
		return self.nota2


	def calcula_media(self):
		self.media = (self.nota1 + self.nota2) / 2
		return self.media


	def mostrar_media(self):
		print(f"A média do aluno é = {self.media:.2f}.")



# Programa principal
val_media = MediaAluno()
val_media.ler_nota1()
val_media.ler_nota2()
val_media.calcula_media()
val_media.mostrar_media()

