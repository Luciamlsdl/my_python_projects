"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""

#Este programa esta em sua forma classe

class NumeroParOuÍmpar:
    def __init__(self):
        self.numero = 0


    def apresentação(self):
        print("\nPrograma para ver se o numero é par ou ímpar!".upper())


    def ler_número(self):
        while True:
            try:
                self.numero = int(input("--> Digite o número para a verificação!: "))
                if self.numero <= 0:
                    print("O valor não pode ser um valor negativo!")
                else:
                    return self.numero    
            except  ValueError:
                print("Por favar! Digite um valor válido!")


    def verifica_valor(self):
        if self.numero % 2 == 0:
            print(f"O número {self.numero} é um número (par).")
        else:
            print(f"O número {self.numero} é um número (Ímpar).")


#Programa principal
if __name__ == "__main__":
    numero = NumeroParOuÍmpar()
    numero.apresentação()
    numero.ler_número()
    numero.verifica_valor()