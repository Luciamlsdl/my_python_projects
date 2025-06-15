"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro nome e o ultimo nome separadamente
"""

#Este programa está em sua forma mais simples

nome = str(input("\nEscreva o seu nome completo: ")).strip()
n = nome.split()


print(f"O primeiro nome é {n[0]}\n"
      f"O ultimo nome é {n[-1]}")