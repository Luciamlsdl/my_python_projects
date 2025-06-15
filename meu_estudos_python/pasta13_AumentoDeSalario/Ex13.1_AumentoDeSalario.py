"""
.Faça um algoritmo que leia o salário de um funcionário e mostre
o seu novo salário com 15% de aumento.
"""
# Este programa está na sua forma mais simples.

print()
nome_funcionário = str(input("Nome do funcionário: ")).capitalize() 
salario_funcionário = float(input(f"Qual é o valor do funcionário {nome_funcionário} R$: "))

novo_salário = salario_funcionário + (salario_funcionário * 15 / 100)

print(f"O salário do funcionário {nome_funcionário} é de R$:{salario_funcionário:.2f}.")
print(f"Com o aumento de 15% o novo salário de {nome_funcionário} será de R$:{novo_salário:.2f}.")
print()