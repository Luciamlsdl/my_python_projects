"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""

#Este programa esta em sua forma classe.
#Este código está com uma nova função qe é a de Executar_programa que é uma excelente ideia.

class NumeroParOuÍmpar:
    def __init__(self):
        self.numero = 0

    def apresentação(self):
        print("\nPrograma para ver se o numero é par ou ímpar!".upper())

    def ler_número(self):
        while True:
            try:
                self.numero = int(input("--> Digite o número para a verificação!: "))
                return self.numero
            except ValueError:
                print("Por favor! Digite um valor válido!")

    def verifica_valor(self):
        if self.numero % 2 == 0:
            print(f"O número {self.numero} é um número (par).")
        else:
            print(f"O número {self.numero} é um número (Ímpar).")

    def executar_programa(self): # Novo método
        self.apresentação()
        self.ler_número() # Atribui ao self.numero
        self.verifica_valor()

# Programa principal
if __name__ == "__main__":
    programa = NumeroParOuÍmpar()
    programa.executar_programa()