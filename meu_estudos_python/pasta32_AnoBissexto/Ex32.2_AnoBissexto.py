"""
Faça um programa que leia um ano qualquer e mostre se ele e ano bissexto
"""

#Este programa está em sua forma de função
#Mais com a importação da biblioteca datetime para analisar a data atual

from datetime import date

def apresentação():
    print("\nAnalisador de ano bissexto".upper())


def ano_para_analise():
    while True:
        try:
            ano = int(input("Digite o ano para a analise ou 0 para o ano atual: "))
            return ano
        except ValueError:
            print("Por favor! Digite um ano válido")


def analisa_ano(ano):
    if ano == 0:
        ano = date.today().year
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano de {ano} é um ano bissexto!")

    else:
        print(f"O ano de {ano} não é um ano bissexto!")


def executador_de_programa():
    apresentação()
    ano = ano_para_analise()
    analisa_ano(ano)



#programa principal
executador_de_programa()