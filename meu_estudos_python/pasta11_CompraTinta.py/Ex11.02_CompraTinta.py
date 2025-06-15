"""
.Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área
e a quantidade de tinta para pinta-la.
.Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
# Este programa está em sua forma de função


def ler_valores():
    altura_parede = float(input("Digite a altura da parde (em metros): "))
    largura_parede = float(input("Digite a largura da parede (em metros): "))  
    return altura_parede, largura_parede


def fazer_calculo(altura, largura):
    area = altura * largura
    quantidade_tinta = area / 2
    return area, quantidade_tinta


def mostrar_resultado(area, quantidade_tinta):
    print(f"A sua área a ser pintada é {area:.2f}m².")
    print(f"E a quantidade necessária para pinta-la é {quantidade_tinta:.2f} litros de tinta")


# Programa principal
altura, largura = ler_valores()
area, quantidade_tinta = fazer_calculo(altura, largura)
mostrar_resultado(area, quantidade_tinta)
