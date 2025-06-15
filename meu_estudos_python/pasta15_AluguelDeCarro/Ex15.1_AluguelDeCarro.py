"""
Escreva um programa que pergunte a quantidade de km percorrido por um carro
e a quantidades de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$:60 por dia e R$:0.15 por km rodado.
"""

# Este programa  está na  sua forma mais simples

print("\n_______ Alugando Sonhos________")

nome_carro = str(input("\nMarca do carro alugado: ")).strip().capitalize()
modelo_carro = str(input("Modelo do carro alugado: ")).strip().capitalize()
quilômetros = int(input("Quantos quilômetros o carro percorreu? km: "))
dias_alugados = int(input("Por quantos dias o carro ficou alugado?: "))

dia = 60
km_rodado = 0.15

valor_km = quilômetros * km_rodado
valor_dia = dias_alugados * dias_alugados

total = valor_km + valor_dia

print(f"\nO carro da marca {nome_carro} do modelo {modelo_carro}.")
print(f"O valor do aluguel do carro ficou num total de R$:{total:.2f}.\n")
