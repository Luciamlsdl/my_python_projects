"""
Escreva um programa que leia o salário de um funcionário e calcule o seu aumento.
Para salário superior a R$:1250.00 calcule um aumento de 10%.
Para salário inferior o igual o aumento é de 15%.
"""
#Este programa esta em formato de função

def apresentação():
    print("\n---Programa para calcular aumento de salário---".upper())


def ler_salario():
    while True:
        try:
            salario = float(input("\nDigite o valor do salário do funcionário R$: "))
            if salario > 0:
                return salario
            else:
                print("-->Salário não pode ser um valor menor que 0!")
        except ValueError:
            print("--->Por favor! Digite um valor válido para salário!")


def aumento_de_salario(salario):
    if salario <= 1250:
        novo_salario = salario + (salario * 15/ 100)
    else:
        novo_salario = salario + (salario * 10 / 100)

    return novo_salario


def mostrar_aumento(salario, novo_valor):
    print(f"Para o salário de R$:{salario:.2f}.\n"
          f"O seu novo salário é de R$:{novo_valor:.2f}.")


def executador_de_programa():
    apresentação()
    salario = ler_salario()
    novo_salario = aumento_de_salario(salario)
    mostrar_aumento(salario, novo_salario)



#Programa principal
executador_de_programa()