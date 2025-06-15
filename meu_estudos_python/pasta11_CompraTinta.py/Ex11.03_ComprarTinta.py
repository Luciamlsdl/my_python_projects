"""
.Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área
e a quantidade de tinta para pinta-la.
.Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
# Este programa está em sua forma de classe

class AreaTintaPorMetrosQuadrados:
    def __init__(self):
        self.altura = 0
        self.largura = 0
        self.area = 0
        self.tinta = 0


    def ler_altura_largura(self):
        try:
            self.altura = float(input("Digite a altura da parede: "))
            self.largura = float(input("Digite a largura da parede: "))
        except ValueError:
            print("Erro! Digite um valor válido!")


    def calcula_area(self):
        self.area = self.altura * self.largura


    def calcula_tinta(self):
        self.tinta = self.area / 2


    def mostrar_valores(self):
        print(f"A sua área é de {self.area:.2f}.")
        print(f"Sera necessário {self.tinta:.2f} litros de tinta.")



# Programa principal
if __name__ == "__main__":
    dados = AreaTintaPorMetrosQuadrados()
    dados.ler_altura_largura()
    dados.calcula_area()
    dados.calcula_tinta()
    dados.mostrar_valores()