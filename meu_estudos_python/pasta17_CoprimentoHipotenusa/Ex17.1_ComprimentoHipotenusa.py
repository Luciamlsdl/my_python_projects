"""
Faça um programa que leia o comprimento do cateto oposto e o comprimento
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""

# Este programa está em sua forma mias simples com sua formula de calculo.

cateto_oposto = float(input("\nDigite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) # Forma para fazer o calculo

print(f"O valor da hipotenusa é = {hipotenusa:.2f}.")
print()