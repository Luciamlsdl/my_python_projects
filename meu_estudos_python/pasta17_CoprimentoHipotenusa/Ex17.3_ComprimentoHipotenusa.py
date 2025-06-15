"""
Faça um programa que leia o comprimento do cateto oposto e o comprimento
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""

# Este programa está em seu formato de classe e usando a importação do modulo math.hypot.

from math import hypot

class  CalculoDaHipotenusa:
    def __init__(self, cateto_oposto, cateto_adjacente):
        self.cateto_oposto = cateto_oposto
        self.cateto_adjacente = cateto_adjacente
        self.hipotenusa = 0


    def calcula_hipotenusa(self):
        self.hipotenusa = hypot(self.cateto_oposto, self.cateto_adjacente)
        return self.hipotenusa


    def mostrar_hipotenusa(self):
        print(f"O valor da hipotenusa é = {self.hipotenusa:.2f}")


class GerenciadorDeEntrada:
    @staticmethod
    def ler_catetos():
        while True:
            try:    
                cateto_oposto = float(input("\nDigite o valor do cateto oposto: "))
                cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
                if cateto_oposto >= 0 and cateto_adjacente >= 0:
                    return cateto_oposto, cateto_adjacente
            except ValueError:
                print("Por favor! Digite um valor válido!")
                

# Programa principal
cateto_oposto, cateto_adjacente = GerenciadorDeEntrada.ler_catetos()

valor = CalculoDaHipotenusa(cateto_oposto, cateto_adjacente)
valor.calcula_hipotenusa()
valor.mostrar_hipotenusa()


