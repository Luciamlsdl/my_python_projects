"""
.Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área
e a quantidade de tinta para pinta-la.
.Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
# Este programa está em sua forma mias simples

altura_parede = float(input("Digite a altura da parede em metros: "))
largura_parede = float(input("Digite a largura da parede em metros: "))

area = altura_parede * largura_parede
tinta = area * 2

print("-" * 50)
print(f"A área de sua parede é de {area} metros quadrados.")
print(f"Sera necessário {tinta} litros de tinta para pinta-la.")
print("-" * 50)