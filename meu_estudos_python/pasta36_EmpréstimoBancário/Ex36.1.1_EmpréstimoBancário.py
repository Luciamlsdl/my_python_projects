"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado. 
"""

#Código feito pela Gemini IA


# Programa para aprovar empréstimo bancário para compra de casa

print("\n--- Simulador de Empréstimo Bancário ---")

# Solicita as informações ao usuário
valor_casa = float(input("Qual é o valor total da casa desejada? R$: "))
salario_comprador = float(input("Qual é o seu salário mensal? R$: "))
anos_pagamento = int(input("Em quantos anos você pretende pagar o empréstimo? "))

# Calcula o número total de meses para pagamento
meses_pagamento = anos_pagamento * 12

# Calcula o valor da prestação mensal
prestacao_mensal = valor_casa / meses_pagamento

# Calcula o limite de 30% do salário
limite_salario_30_porcento = salario_comprador * 0.30 # 30% é o mesmo que 0.30

print(f'''
--- Detalhes da Simulação ---
Para comprar uma casa de R$:{valor_casa:.2f} em {anos_pagamento} anos,
a prestação mensal será de R$:{prestacao_mensal:.2f}.
Seu limite de 30% do salário é de R$:{limite_salario_30_porcento:.2f}.
''')

# Verifica se a prestação excede o limite e aprova ou nega o empréstimo
if prestacao_mensal <= limite_salario_30_porcento:
    print("🎉 Parabéns! Empréstimo aprovado!")
else:
    print("😔 Empréstimo negado. A prestação excede 30% do seu salário.")

print("---------------------------------------")