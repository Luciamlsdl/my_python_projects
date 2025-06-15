"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma mis simples

real = float(input("Quanto dinheiro você tem na sua carteira?: ")) 
dollar = 5.76
compra = real / dollar

print(f"Com R$:{real:.2f} da para comprar US:{compra:.2f} dollars.")
