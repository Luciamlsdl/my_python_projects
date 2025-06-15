"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
"""
# Este programa está na sua forma de função
from time import sleep

def calcula_digito(valor_numero):
    valor_dígitos = {
                        "unidade": valor_numero // 1 % 10,
                        "dezena": valor_numero // 10 % 10,
                        "centena": valor_numero // 100 % 10,
                        "milhar": valor_numero // 1000 % 10
                    }
    return valor_dígitos


def mostrar_resultado(resultado, valor_numero):
    sleep(2)
    print(f"\nO resultado da analise de dígitos do número {valor_numero}:")
    sleep(1)
    print(f"Unidade = {resultado["unidade"]}")
    sleep(1)
    print(f"Dezena = {resultado["dezena"]}")
    sleep(1)
    print(f"Centena = {resultado["centena"]}")
    sleep(1)
    print(f"Milhar = {resultado["milhar"]}")
    sleep(1)


def ler_numero():
    while True:
        try:
            numero = int(input("\nDigite um número de 0 a 9999 para ver seu dígitos: "))
            if numero >= 0 and numero <= 9999:
                return numero
            else:    
                print("O valor só pode ter 4 dígitos que é de 0 a 9999!")
            
        except ValueError:
            print("Por favor! Digite um valor válido para o número!")    


# Programa principal
while True:
    valor_numero = ler_numero()
    resultado = calcula_digito(valor_numero)
    mostrar_resultado(resultado, valor_numero)


    pare = str(input("\nDigite S = sim para continuar e N = não para parar: ")).strip().upper()[0]
    if pare == "N":
        break
    elif pare == "S":
        continue
    else:
        print("Digite somente S para sim ou N para não!")
