"""
Faça um programa que leia um ano qualquer e mostre se ele e ano bissexto
"""

#Este programa está em sua forma simples
#Mais com a importação da biblioteca datetime para analisar a data atual

from datetime import date

print("\nAnalisador de ano bissexto!".upper())

ano = int(input("Digite um  ano para ser analisado ou 0 para o ano atual!: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é um ano bissexto!")

else:
    print(f"O ano de {ano} não é um ano bissexto!")
