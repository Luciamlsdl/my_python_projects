"""
Escreva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem cobrando R$:0,50 por km para viagem de até 200Km
e R$:0,45 para viagem mais longas.
"""

#Este programa está em forma de função

valor_normal = 0.50
valor_longo = 0.45

def apresentação():
    print("\nBem vindo! Ao gerenciador de viagem!".upper())


def distancia_viagem():
    while True:
        try:
            distancia = int(input("\nQual é a distancia de sua viagem? Km: "))
            if distancia < 10 :
                print(f"A distancia da viagem não pode ser inferior a 10Km")
            else:
                return distancia
        except ValueError:
            print("Por favor! Digite um valor válido para a distancia")


def calculo_valor(valor_distancia):
    if valor_distancia > 200:
        preço = valor_distancia * valor_longo
        return preço, valor_longo
    else:
        preço = valor_distancia * valor_normal
        return preço, valor_normal


def mostrar_resultado(valor, valor_passagem):
    print(f"Sua viagem no valor de R$:{valor_passagem} por Km")
    print(f"O valor de sua viagem é de R$:{valor:.2f}")


def executar_programa():
    apresentação()
    valor_distancia = distancia_viagem()
    valor, valor_passagem = calculo_valor(valor_distancia)
    mostrar_resultado(valor, valor_passagem)


#Programa principal
executar_programa()
