"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato simples 


def comparar_valores(a, b):
    if a > b:
        return f"O primeiro valor ({a}) é o maior."
    elif b > a:
        return f"O segundo valor ({b}) é o maior."
    else:
        return f"Não existe maior valor, ambos são iguais ({a} = {b})."

primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))
print(comparar_valores(primeiro, segundo))
