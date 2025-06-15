"""
Faça um algoritmo que leia o preço de um produto
e mostre o seu novo preço, com 5 % de desconto. 
"""
# ESte programa está na  sua forma mais simples.

print()
preço_produto = float(input("Qual é o valor do produto R$: "))

novo_valor = preço_produto - (preço_produto * 5 / 100)

print(f"O valor do produto é R$:{preço_produto:.2f}.")
print(f"E o valor do produto com 5% de desconto é R$:{novo_valor:.2f}.")
print()