"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma de classe.

class Comprar_dollar:
    def __init__(self, valor):
        self.valor = valor
        self.dollar = 5.76
        self.tot_valor = 0


    def converti_valor(self):
        self.tot_valor = self.valor / self.dollar        
        return self.tot_valor
    

    def mostra_valor(self):
        print(f"Com R$:{self.valor:.2f} Reais da para comprar US$:{self.tot_valor:.2f} Dollars.")



class Ler_valor:
    @staticmethod
    def pegar_valor():
        while True:
            try:
                valor = float(input("Quantos Reais você tem para comprar Dollar? R$: "))
                return valor
            except ValueError:
                print("Por favor! Digite um valo válido!")
            

    @staticmethod
    def resultado_val(valor):
        comprar = Comprar_dollar(valor)
        comprar.converti_valor()
        comprar.mostra_valor()


if __name__ == "__main__":
    valor = Ler_valor.pegar_valor()
    if valor is not None:
        Ler_valor.resultado_val(valor)
