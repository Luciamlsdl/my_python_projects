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
            if ano:
                return ano
        except ValueError:
            print("Por favor! Digite um ano válido")


def executador_de_programa():
    apresentação()
    ano_para_analise()


#programa principal
executador_de_programa()