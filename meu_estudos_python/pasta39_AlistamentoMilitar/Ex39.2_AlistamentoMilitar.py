"""
.Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar
e se é a hora exata de se alistar ou se já passou do tempo do alistamento.
.Seu programa também devera mostrar o tempo que falta ou que ja passou do prazo.    
"""

# Programa em sua forma função

from datetime import date

def ler_data_nascimento():
    while True:
        try:
            data_nascimento = int(input("Digite sua data de nascimento entre 1900 e 2025: "))
            if data_nascimento < 1900 or data_nascimento > 2025:
                print("A data de nascimento tem que estar entre (1900 a 2025)") 
            else:
                return data_nascimento
        except ValueError:
            print("Por favor! Digite um valor válido para data de nascimento!")


def retorna_data():
    data_atual = date.today().year
    return data_atual


def retorna_idade(data_atual, data_nascimento):
    idade_atual = data_atual - data_nascimento
    return idade_atual


def mostrar_resultado(data_de_nascimento, idade_atual, data_atual):
    print(f"Quem nasceu em {data_de_nascimento} tem {idade_atual} anos em {data_atual}.")

    if idade_atual == 18:
        print("Você tem que se alistar imediatamente!")

    elif idade_atual < 18:
        saldo_faltando = 18 - idade_atual
        print(f"Ainda faltam {saldo_faltando} anos para o alistamento!")

        ano_alistamento = data_atual + saldo_faltando
        print(f"Seu alistamento será em {ano_alistamento}!")

    elif idade_atual > 18:
        saldo_sobrando = idade_atual - 18
        print(f"Você já deveria ter se alistado há {saldo_sobrando} anos!")
        ano_alistamento = data_atual - saldo_sobrando
        print(f"Seu alistamento foi em {ano_alistamento}")


#Código principal
data_nascimento = ler_data_nascimento()
data_atual = retorna_data()
idade_atual = retorna_idade(data_atual, data_atual)
mostrar_resultado(data_nascimento, idade_atual, data_atual)
