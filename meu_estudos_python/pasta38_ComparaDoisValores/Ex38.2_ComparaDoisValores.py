"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato função

def compara_valor(x, y):
    if x > y:
        return f"o primeiro valor é maior!"
    elif y > x :
        return f"O segundo valor é maior!"
    else:
        return f"Os dois valore são iguais"


#Código principal
primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
print(compara_valor(primeiro_valor, segundo_valor))
