"""
Escreva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem cobrando R$:0,50 por km para viagem de até 200Km
e R$:0,45 para viagem mais longas.
"""

#Este programa está em forma de classe


class GerenciadorDeViagem:
    def __init__(self, valor_normal=0.50, valor_longo=0.45):
        self.valor_normal = valor_normal
        self.valor_longo = valor_longo
        self.distancia = 0
        self.valor = 0
        self.preço = 0
        
        
    def apresentação(self):
        print("\nBem vindo! Ao gerenciador de viagem!".upper())


    def distancia_viagem(self):
        while True:
            try:
                self.distancia = int(input("\nQual é a distancia de sua viagem? Km: "))
                if self.distancia < 10 :
                    print(f"A distancia da viagem não pode ser inferior a 10Km")
                else:
                    return self.distancia
            except ValueError:
                print("Por favor! Digite um valor válido para a distancia")


    def calculo_valor(self):
        if self.distancia > 200:
            self.preço = self.distancia * self.valor_longo
            self.valor = self.valor_longo
        else:
            self.preço = self.distancia * self.valor_normal
            self.valor = self.valor_normal

            
    def mostrar_resultado(self):
        print(f"Sua viagem no valor de R$:{self.valor} por Km")
        print(f"O valor de sua viagem é de R$:{self.preço:.2f}")


    def executar_programa(self):
        self.apresentação()
        self.distancia_viagem()
        self.calculo_valor()
        self.mostrar_resultado()


#Programa principal
viagem = GerenciadorDeViagem()
viagem.executar_programa()