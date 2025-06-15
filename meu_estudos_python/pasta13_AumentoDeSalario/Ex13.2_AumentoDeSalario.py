"""
.Faça um algoritmo que leia o salário de um funcionário e mostre
o seu novo salário com 15% de aumento.
"""
# Este programa está na sua forma de função.

def ler_nome_funcionário():
    print()
    while True:
        nome_funcionário = str(input("Nome do funcionário: ")).capitalize()
        if nome_funcionário and not nome_funcionário.isnumeric():
            return nome_funcionário            
        else:
            print("Por favor! Digite um nome válido para o funcionário.")
        

def ler_salario(nome_funcionário):        
        while True:
            try:
                valor_salario = float(input(f"Digite o valor do salário de {nome_funcionário} R$: "))
                if valor_salario > 0:
                    return valor_salario
                else:
                    print("O valor do salário do funcionário tem  que ser maior que zero.")
            except ValueError:
                print("Por favor! Digite um valor válido.")


def aumento_salario(valor_salario):
    novo_salario = valor_salario + (valor_salario * 15 / 100)
    return novo_salario


def mostrar_aumento(nome_funcionário, valor_salario, novo_salario):
    print(f"O salário de {nome_funcionário} é de R$:{valor_salario}.")
    print(f"Com aumento de 15% o salário de {nome_funcionário} sera de R$:{novo_salario:.2f}.")
    print()



# Programa principal
if __name__ == "__main__":
    while True:
        nome_funcionário = ler_nome_funcionário() 
        valor_salario = ler_salario(nome_funcionário)
        if valor_salario:
            novo_salario = aumento_salario(valor_salario)
            mostrar_aumento(nome_funcionário, valor_salario, novo_salario)
            break
