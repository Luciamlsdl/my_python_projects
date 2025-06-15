"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Este código está em sua forma de classe e usando a importação do modulo math.

from math import radians, sin, cos, tan


class SenoCossenoTangente:
    """Calcula e mostra o seno, cosseno e tangente de um ângulo."""
    def __init__(self, angulo):
        """Inicializa a classe com o ângulo."""
        self.angulo = angulo
        self.seno = 0
        self.cosseno = 0
        self.tangente = 0

    def calcular_valores(self):
        """Calcula o seno, cosseno e tangente do ângulo."""
        radianos = radians(self.angulo)
        self.seno = sin(radianos)
        self.cosseno = cos(radianos)
        if cos(radianos) == 0:
            self.tangente = "Indefinida"
        else:
            self.tangente = tan(radianos)

    def mostrar_valore(self):
        """Mostra o seno, cosseno e tangente do ângulo formatados."""
        tangente_str = f"A tangente do angulo é = {self.tangente:.2f}." if isinstance(self.tangente, float) else f"A tangente do angulo é = {self.tangente}."
        print(f"O seno do ângulo é = {self.seno:.2f}.\n"
              f"O cosseno do ângulo é = {self.cosseno:.2f}.\n"
              f"{tangente_str}")

class GerenciadorDeAngulo:
    """Gerencia a entrada do ângulo do usuário."""
    @staticmethod
    def ler_angulo():
        """Lê um ângulo do usuário e o retorna como um float."""
        while True:
            try:
                angulo = float(input("\nDigite um ângulo qualquer: °"))
                if angulo >= 0:
                    return angulo
            except ValueError:
                print("Por favor! Digite um valor válido para o ângulo!")