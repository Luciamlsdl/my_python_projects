"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Este código está em sua forma de classe e usando a importação do modulo math.

from math import radians, sin, cos, tan

class SenoCossenoTangente:
    def __init__(self, angulo):
        self.angulo = angulo
        self.seno = 0
        self.cosseno = 0
        self.tangente = 0


    def calculo_seno(self):
        self.seno = sin(radians(self.angulo))
        return self.seno


    def calculo_cosseno(self):
        self.cosseno = cos(radians(self.angulo))
        return self.cosseno


    def calculo_tangente(self):
        self.tangente = tan(radians(self.angulo))
        return self.tangente


    def mostrar_valore(self):
        print(f"O seno do ângulo é = {self.seno:.2f}.\n"
              f"O cosseno do ângulo é = {self.cosseno:.2f}.\n"
              f"A tangente do angulo é = {self.tangente:.2f}.")



class GerenciadorDeAngulo:
    @staticmethod
    def ler_angulo():
        while True:
            try:
                angulo = float(input("\nDigite um ângulo qualquer: °"))
                if angulo >= 0:
                    return angulo
            except ValueError:
                print("Por favor! Digite um valor válido para o ângulo!") 


# Program principal
angulo = GerenciadorDeAngulo.ler_angulo()

valores = SenoCossenoTangente(angulo)
valores.calculo_seno()
valores.calculo_cosseno()
valores.calculo_tangente()
valores.mostrar_valore()
