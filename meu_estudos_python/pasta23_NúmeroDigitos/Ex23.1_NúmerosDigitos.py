"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
"""
# Este programa está na sua forma mais simples

from time import sleep


while True:
    try:
        numero = int(input("\nDigite um número inteiro de 0 a 9999: "))
    except ValueError:
        print("Digite um valor válido para o número")

    unidade = numero // 1 % 10
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000 % 10

    print(f"\nAnalisando o número : {numero}.")
    sleep(2)
    print(f"Unidade: {unidade}.")
    sleep(1)
    print(f"Dezena: {dezena}.")
    sleep(2)
    print(f"Centena: {centena}.")
    sleep(1)
    print(f"Milhar: {milhar}.")
        

    while True:
        parar = str(input(f"\nQuer analisar outro numero (S = Sim ou N = Não): ")).strip().upper()[0]
        if parar == "N":
            break
        elif parar == "S":
            break
        else:
            print(f"Opção inválida. Digite 'S' para Sim ou 'N' para Não.")
    if parar == "N":
        break
