"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.
"""

# Este programa está em sua forma de função

def encontra_silva_no_nome(nome_completo):
    """
    Procura a substring 'SILVA' (ignorando a capitalização) no nome completo
    e retorna a posição da primeira ocorrência.

    Args:
        nome_completo (str): O nome completo a ser verificado.

    Returns:
        int: O índice da primeira ocorrência de 'SILVA' (em maiúsculas)
             na string em maiúsculas, ou -1 se não for encontrado.
    """
    nome_maiúsculo = nome_completo.strip().upper()
    return nome_maiúsculo.find('SILVA')


# Programa principal
print("\nVamos analisar seu nome para ver se tem 'Silva' em seu nome!")
nome = str(input("Escreva o seu nome completo: ")).strip()

índice_silva = encontra_silva_no_nome(nome)

if índice_silva != -1:
    print(f"'SILVA' Foi encontrado em seu nome na posição: {índice_silva}")
else:
    print("'SILVA' Não foi encontrado no seu nome!")
