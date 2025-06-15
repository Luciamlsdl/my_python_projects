"""
Faça um programa que leia um ano qualquer e mostre se ele e ano bissexto
"""

#Este programa está em sua forma simples


print("\nAnalisando se o ano é ano bissexto!".upper())

ano = int(input("-->Digite o ano a ser analisado: "))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f"O ano de {ano} é um ano bissexto!")
else:
    print(f"O ano de {ano} não é um ano bissexto!\n")
