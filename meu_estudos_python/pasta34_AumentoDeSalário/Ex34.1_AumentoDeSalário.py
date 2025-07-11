"""
Escreva um programa que leia o salário de um funcionário e calcule o seu aumento.
Para salário superior a R$:1250.00 calcule um aumento de 10%.
Para salário inferior o igual o aumento é de 15%.
"""

#Este programa está em sua forma simples

print("\nPrograma para calcular aumento de salário".upper())

salário = float(input("Digite o valor do salário R$: "))

if salário <= 1250:
    novo_salário = salário + (salário * 15 / 100)

else:
    novo_salário = salário + (salário * 10 / 100)

print(f"Para salário igual a R$:{salário:.2f}\n"
      f"Seu novo salário sera de R$:{novo_salário:.2f}")