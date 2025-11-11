"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato função

"""
Programa: Comparação entre dois valores inteiros
Autor: Luciano Soares
Descrição:
    Lê dois números inteiros e mostra qual é o maior,
    ou se ambos são iguais.
"""

def comparar_valores(x, y):
    if x > y:
        return f"O primeiro valor ({x}) é maior que o segundo ({y})."
    elif y > x:
        return f"O segundo valor ({y}) é maior que o primeiro ({x})."
    else:
        return f"Os dois valores são iguais ({x})."


# Código principal
print("="*50)
print(" PROGRAMA DE COMPARAÇÃO DE VALORES ".center(50, "="))
print("="*50)

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

print()
print(comparar_valores(primeiro_valor, segundo_valor))
