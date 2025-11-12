
"""
.Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar
e se é a hora exata de se alistar ou se já passou do tempo do alistamento.
.Seu programa também devera mostrar o tempo que falta ou que ja passou do prazo.    
"""

# Programa em sua forma função

from datetime import date

# 1. Função para ler e validar o ano de nascimento (Está OK)
def ler_data_nascimento():
    while True:
        try:
            data_nascimento = int(input("Digite sua data de nascimento (entre 1900 e 2025): "))
            # A validação de intervalo (1900 a 2025) está correta
            if data_nascimento < 1900 or data_nascimento > 2025:
                print("A data de nascimento tem que estar entre 1900 e 2025.") 
            else:
                return data_nascimento
        except ValueError:
            print("Por favor! Digite um valor numérico inteiro válido para data de nascimento!")


# 2. Função para obter o ano atual (Está OK)
def retorna_data():
    data_atual = date.today().year
    return data_atual


# 3. Função para calcular a idade (CORRIGIDA)
def retorna_idade(data_atual, data_nascimento):
    # Recebe os dois argumentos necessários para o cálculo
    idade_atual = data_atual - data_nascimento
    return idade_atual


# 4. Função para mostrar o resultado e a situação de alistamento (Está OK)
def mostrar_resultado(data_de_nascimento, idade_atual, data_atual):
    print(f"\n--- Situação do Alistamento ---")
    print(f"Quem nasceu em **{data_de_nascimento}** tem **{idade_atual}** anos em {data_atual}.")

    if idade_atual == 18:
        print("🎉 É HORA EXATA! Você tem que se alistar **IMEDIATAMENTE**!")

    elif idade_atual < 18:
        saldo_faltando = 18 - idade_atual
        print(f"⏳ Ainda faltam **{saldo_faltando} anos** para o alistamento.")
        print("Você **ainda vai** se alistar.")
        
        ano_alistamento = data_atual + saldo_faltando
        print(f"Seu alistamento será em **{ano_alistamento}**.")

    elif idade_atual > 18:
        saldo_sobrando = idade_atual - 18
        print(f"⚠️ Já **passou** do tempo! Você já deveria ter se alistado há **{saldo_sobrando} anos**.")
        
        ano_alistamento = data_atual - saldo_sobrando
        print(f"Seu alistamento foi em **{ano_alistamento}**.")
    print("-------------------------------\n")


# Código principal
# -------------------------------------------------------------
data_nascimento = ler_data_nascimento()
data_atual = retorna_data()
# Chamada CORRIGIDA
idade_atual = retorna_idade(data_atual, data_nascimento)
mostrar_resultado(data_nascimento, idade_atual, data_atual)
# -------------------------------------------------------------