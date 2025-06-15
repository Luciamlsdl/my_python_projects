"""
Uma professora quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ela, lendo os nomes deles e escrevendo o
nome do escolhido na tela.
"""

# Este programa está em sua forma simples porem aprimorada usando a importação do biblioteca random

import random

lista_nome = []

print("\nSeja bem-vindo ao sorteador de aluno!")
print("Digite os nomes dos alunos (Digite fim para encerrar!): ")

while True:
    nome = str(input("Digite o nome do aluno: ")).strip().capitalize()
    if nome == "Fim":
        break

    elif nome and nome.replace(" ", "").isalpha:
        lista_nome.append(nome)

    elif not nome:
        print("Por favor! Digite um nome válido!")

    else:
        print("O nome deve conter apenas letras!")


if lista_nome:
    escolhido = random.choice(lista_nome)

    print(f"\nOs alunos escolhidos são {' ,'.join(lista_nome)}.")
    print(f"O aluno escolhido para apagar o quadro é: \033[1m{escolhido}\033[m]")

else:
    print("Nenhum nome foi adiciona a lista!")
    