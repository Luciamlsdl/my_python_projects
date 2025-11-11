"""
.Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar
e se é a hora exata de se alistar ou se já passou do tempo do alistamento.
.Seu programa também devera mostrar o tempo que falta ou que ja passou do prazo.    
"""

# Programa em sua forma simples

from datetime import date

data_atual = date.today().year

data_de_nascimento = int(input("Digite seu ano de nascimento (EX. 1995): "))
idade_atual = data_atual -data_de_nascimento

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