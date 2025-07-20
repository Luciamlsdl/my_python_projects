"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado. 
"""

# Programa em sua forma simples

casa = float(input("\nQual é o valor da casa? R$: "))
salario = float(input("Qual e o valor do seu salário? R$: "))
anos = int(input("Em quantos anos você quer pagar?: "))


prestacao =  casa / (anos *  12)
minimo = salario * 30 / 100

print(f'''
Para comprar uma casa de R$:{casa:.2f} em {anos} anos\n
A prestação será de R$:{prestacao:.2f}
''')

if prestacao <= minimo:
    print("Empréstimo aprovado!")

else:
    print("Empréstimo negado!")