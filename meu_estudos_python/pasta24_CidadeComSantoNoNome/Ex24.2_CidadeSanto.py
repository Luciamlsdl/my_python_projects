"""
Crie um programa que leia o nome de uma cidade e diga se ela esta em uma lista.
"""

# Este programa está em sua forma de função 
# A ideia aqui é que o usuário digite o primeiro nome de cidade para ser analisado
# Talvez até verificar em uma lista de nome ou algo assim

import unicodedata

lista_cidade = ["Guara", "Santos", "Maringá"]


def apresentação():
    print("\nVerificando o primeiro nome de sua cidade")


def valida_nome_cidade(nome):
    if not nome.strip():
        return False, f"A entrada de nome da cidade não pode estar em branco!"

    for caractere in nome:
        letras = unicodedata.category(caractere)

        if not (letras.startswith('L') or caractere.isspace()):
            return False, f"O nome da cidade deve conter apenas letras e espaços!"    
        
    return True, None


def ler_nome_cidade():
    while True:
        nome_cidade = str(input("Escreva o nome completo de sua cidade: ")).strip()
        valido, mensagem_erro = valida_nome_cidade(nome_cidade)

        if not valido:
            print(f"{mensagem_erro}")
            continue
        else:
            nome_valido = nome_cidade
            return nome_valido
        

def analise_nome_cidade(nome_cit):
    if nome_cit  in lista_cidade:
        print("sua cidade está na lista")
    else:
        print("Sua cidade não consta na lista")



# Programa principal
apresentação() 
nome_cidade_valido = ler_nome_cidade()
analise_nome_cidade(nome_cidade_valido)