"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""

#Este programa esta em sua forma função

def apresentação():
    print("\nPrograma para ver se o numero é par ou ímpar!".upper())


def ler_número():
    while True:
        try:
            numero = int(input("--> Digite o número para a verificação!: "))
            if numero <= 0:
                print("O valor não pode ser um valor negativo!")
            else:
                return numero    
        except  ValueError:
            print("Por favar! Digite um valor válido!")


def verifica_valor(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é um número (par).")
    else:
        print(f"O número {numero} é um número (Ímpar).")


#Programa principal
apresentação()
numero = ler_número()
verifica_valor(numero)