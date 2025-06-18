"""
Faça um programa que leia três números e mostre qual é o mair e o menor valor.
"""

#Este programa esta em sua forma de função
#Neste código criamos uma lista para armazenar os valores e fazer oo tratamento de erro para cada número digitado

def apresentação():
    print("\n--> Maior e menor de três números".upper())


def ler_valores():
    números = [] # Lista vazia
    for i in range(1, 4):
        while True:
            try:
                num = int(input(f"{i}° número: "))
                números.append(num) # Colocando valores na lista
                break # Sai do loop interno e passa para o próximo número
            except ValueError:
                print("Por favor! Digite um número válido!")                     
    return números[0], números[1], números[2] # Retorna como tupla para a compatibilidade


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