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
    print("""
    Escolha uma das bases de conversão:
    [ 1 ] Conversão para BINÁRIO
    [ 2 ] Conversão para OCTAL
    [ 3 ] Conversão para HEXADECIMAL
    """)


def base_de_conversão():
    while True:
        try:
            opção = int(input("Digite sua escolha de opção desejada: "))
            if opção in [1, 2, 3]:
                return opção
            else:
                print("Opção inválida")
        except ValueError:
            print("Por favor! Digite um valor valido das opções!")


def conversão(opção, numero):
    if opção == 1:
        print(f"{numero} Convertido para BINÁRIO = {bin(numero)[2:]}.")
        espaço_em_branco()

    elif opção == 2:
        print(f"{numero} Convertido para Octal = {oct(numero)[2:]}.")
        espaço_em_branco()

    elif opção == 3:
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
        sleep(3)
        numero = ler_numero()
        mostrar_escolhas()
        opção = base_de_conversão()
        conversão(opção, numero)
        if not deseja_continuar():
            break


#Programa principal
if __name__ == "__main__":
    executor()
