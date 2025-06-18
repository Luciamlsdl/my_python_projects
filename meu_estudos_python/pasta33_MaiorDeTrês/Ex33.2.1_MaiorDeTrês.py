"""
Faça um programa que leia três números e mostre qual é o mair e o menor valor.
"""

#Este programa esta em sua forma de função

def apresentação():
    print("\n--> Maior e menor de três números".upper())


#Esta parte do código evita a repetição de coleta de variavel do primeiro código  

def ler_numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor! Digite um valor numérico válido!")


def ler_valores():
    numero1 = ler_numero("Primeiro número: ")
    numero2 = ler_numero("Segundo número: ")
    numero3 = ler_numero("Terceiro número: ")
    return numero1, numero2, numero3


def maior_numero(numero1, numero2, numero3):
    maior_numero = max(numero1, numero2, numero3)
    return maior_numero


def menor_numero(numero1, numero2, numero3):
    menor_numero = min(numero1, numero2, numero3)
    return menor_numero


def mostrar_valores(maior, menor):
    print(f"O maior número é = {maior}.\n"
          f"O menor número é = {menor}.")


def executor_do_programa():
    apresentação()
    numero1, numero2, numero3, = ler_valores()
    maior = maior_numero(numero1, numero2, numero3)
    menor = menor_numero(numero1, numero2, numero3)
    mostrar_valores(maior, menor)


#Programa principal
executor_do_programa()