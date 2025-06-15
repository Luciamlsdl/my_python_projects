"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Este código está em sua forma mais simples e usando a importação do modulo math.

from math import radians, sin, cos, tan

angulo = float(input("\nDigite um ângulo qual qualquer: \n"))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo é = {angulo}.\n"
      f"O seno do angulo é = {seno:.2f}.\n"
      f"O cosseno do angulo é {cosseno:.2f}.\n"
      f"E a tangente do angulo é = {tangente:.2f}.")

