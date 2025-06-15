"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por km acima do limite de velocidade.  
"""

#Este programa esta em sua forma de função

from  random import randint

def apresentação():
    print("\nMonitoramento de velocidade na via".upper())


def velocidade_carro():
    carro = randint(50, 200)
    return carro


def calcula_multa(carro):
    if carro > 80:
        print("\nVocê foi multado! Por exceder a velocidade de 80km/h.")
        print(f"-->Sua velocidade é de {carro}Km/h")
        velocidade = (carro - 80) * 7
        print(f"-->Você foi multado em R$:{velocidade:.2f}")
    else:
        print(f"\nSua velocidade é de {carro}Km/h")
        print("Tenha um bom dia! E dirija com segurança!")


#Programa principal
apresentação()
carro = velocidade_carro()
calcula_multa(carro)



