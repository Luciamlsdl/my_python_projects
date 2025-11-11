"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato simples 

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor é o maior, número-1: {primeiro_valor}.")

elif segundo_valor > primeiro_valor:
    print(f"O segundo valor é o maior, número-2: {segundo_valor}.")

else:
    print(f"Não existe maior valor os dois valores são iguais\nnumero-1: {primeiro_valor}, numero-2: {segundo_valor}.")