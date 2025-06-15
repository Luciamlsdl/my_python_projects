"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma de função.

def conversão(valor):
    dollar = 5.76
    convertido = valor / dollar
    return convertido


def mostra_valor(a, b):
    print(f"Com R$:{a:.2f} Reais da para comprar R$:{b:.2f} Dollars.")
    

# Program principal
real = float(input("Quanto dinheiro você tem na carteira R$: "))
val_convertido = conversão(real)
mostra_valor(real, val_convertido)
