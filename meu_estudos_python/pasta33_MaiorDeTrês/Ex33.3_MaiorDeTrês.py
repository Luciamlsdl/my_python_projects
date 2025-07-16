"""
Faça um programa que leia três números e mostre qual é o mair e o menor valor.
"""

#Este programa esta em sua forma de classe
#Neste código criamos uma lista para armazenar os valores e fazer oo tratamento de erro para cada número digitado


class MaiorEMenorValor:
    def __init__(self):
        self.numeros = []
        self.num = 0


    def apresentação(self):
        print("\n--> Maior e menor de três números".upper())


    def ler_valores(self):
        for i in range(1, 4):
            while True:
                try:
                    self.num = int(input(f"{i}° número: "))
                    self.números.append(self.num) # Colocando valores na lista
                    break # Sai do loop interno e passa para o próximo número
                except ValueError:
                    print("Por favor! Digite um número válido!")                     


def maior_numero(self):
    return max(self.numeros)
    

def menor_numero(self):
    return min(self.numeros)
    

def mostrar_valores(self, maior, menor):
    print(f"O maior número é = {maior}.\n"
          f"O menor número é = {menor}.")


def executor_do_programa(self):
    self.apresentação()
    self.ler_valores()
    maior = self.maior_numero()
    menor = self.menor_numero()
    self.mostrar_valores(maior, menor)


#Programa principal
if __name__ == "__main__":
    meu_programa = MaiorEMenorValor()
    meu_programa.executor_do_programa()