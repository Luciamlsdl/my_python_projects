"""
Escreva um número que lei um número inteiro qualquer e peça para o usuário
escolher sua base de conversão.
1 = Para Binário
2 = Para Octal
3 = Para Hexadecimal
"""

#Este programa esta em seu formato de função

import os
from time import sleep
from InquirerPy import prompt
def espaço_em_branco():
    print()


def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")


def apresentação():
    print("---- Programa para conversão de base numérica ----".upper())


def ler_numero():
    while True:
        try:
            numero = int(input("--->Digite o número a ser convertido: "))
            if numero > 0:
                return numero
            else:
                print("O valor não pode ser menor ou igual a 0")
        except ValueError:
            print("Por favor! Digite um valor válido para a conversão!")


def mostrar_escolhas():
    pergunta = [{
        "type": "list",
        "message": "Escolha uma das bases de conversão",
        "choices": ["BINÁRIO", "OCTAL", "HEXADECIMAL"],
        "name": "conversão",
    }] 

    resposta = prompt(pergunta)["conversão"] 
    return resposta


def conversão(opção, numero):
    if opção == "BINÁRIO":
        print(f"{numero} Convertido para BINÁRIO = {bin(numero)[2:]}.")
        espaço_em_branco()

    elif opção == "OCTAL":
        print(f"{numero} Convertido para Octal = {oct(numero)[2:]}.")
        espaço_em_branco()

    elif opção == "HEXADECIMAL":
        print(f"{numero} Convertido para HEXADECIMAL = {hex(numero)[2:]}")
        espaço_em_branco()


def deseja_continuar():
    while True:
        resposta = input("Quer converter outro número (S/N)?: ").strip().upper()
        if resposta == "S":
            return True
        elif resposta == "N":
            print("Muito obrigado por usar nosso programa! Volte sempre!")
            espaço_em_branco()
            return False
        else:
            print("Por favor! Digite somente S para sim ou N para não!")



def executor():
    while True:
        limpa_tela()
        apresentação()
        sleep(2)
        numero = ler_numero()
        opção = mostrar_escolhas()
        conversão(opção, numero)
        if not deseja_continuar():
            break


#Programa principal
if __name__ == "__main__":
    executor()
