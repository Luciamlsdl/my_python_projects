"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato simples 

# Programa: Comparação entre dois valores inteiros

print("="*60)
print(" PROGRAMA DE COMPARAÇÃO DE VALORES ".center(60, "="))
print("="*60)

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor ({primeiro_valor}) é o maior.")
elif segundo_valor > primeiro_valor:
    print(f"O segundo valor ({segundo_valor}) é o maior.")
else:
    print(f"Não existe maior valor, ambos são iguais ({primeiro_valor}).")
