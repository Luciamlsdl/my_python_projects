"""
Escreva um programa que converta uma temperatura digitada em
graus célsius e converta em graus fahrenheit
"""

# Este programa está em sua forma mais simples


célsius = float(input("\nDigite a temperatura para conversão Cº: "))
fahrenheit = ((9 * célsius) / 5) + 32

print(f"\nA temperatura Cº:{célsius:.2f} convertida para Fº:{fahrenheit:.2f}.")
