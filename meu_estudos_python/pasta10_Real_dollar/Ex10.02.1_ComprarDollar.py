"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma de classe e com menu de escolha

from InquirerPy import prompt

def conversão(valor, taxa_cambio):
    convertido = valor / taxa_cambio
    return convertido


def mostrar_valor(a, b, resultado):
    print("-" * 50)
    print(f"Com R$:{a:.2f} você pode comprar {b:.2f} {resultado.capitalize()}.")
    print("-" * 50)


#Programa principal
while True:
    try:
        real = float(input("Quanto dinheiro você tem para comprar dollar? R$: "))
        break
    except ValueError:
        print("Por favor! Insira um valor válido!")

# moeda = str(input("Digite o nome da moeda (exemplo: Dollar, Euro): ")).lower()

pergunta = [{
    "type": "list",
    "message": "Para qual moeda você deseja converter?",
    "choices": ["Dollar", "Euro", "BTC", "Ouro"],
    "name": "moeda",
}]


resposta = prompt(pergunta)
resultado = resposta["moeda"]

taxa = {
    "Dollar": 5.76,
    "Euro": 6.25,
    "BTC": 473.218,
    "Ouro": 579.52,
}


if resultado in taxa:
    val_convertido = conversão(real, taxa[resultado])
    mostrar_valor(real, val_convertido, resultado)
else:
    print("Moeda não reconhecida!")
