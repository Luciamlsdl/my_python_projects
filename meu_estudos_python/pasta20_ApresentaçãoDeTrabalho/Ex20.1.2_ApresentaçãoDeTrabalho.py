"""
Ordem de apresentação de trabalho de alunos.
Faça um programa que leia o nome de seus alunos e mostre a ordem sorteada. 
"""

# Este programa está em sua forma mais simples mais usando a biblioteca random com a função shuffle
# Biblioteca colorama para dar cores ao código
# Biblioteca time para dar tempo
# Biblioteca re aqui usada para validar a string ou variável nome
# Para  que se no caso do usuário escrever o nome como José Luiz não dar erro por ter um acento no è de José
# Ou qualquer nome que tenha um acento


import re
from  colorama import init,Fore,Style
from random import shuffle
from time import sleep

Azul = Fore.BLUE
Ciano  = Fore.CYAN
Amarelo = Fore.LIGHTYELLOW_EX
Vermelho = Fore.RED
Verde = Fore.GREEN

Reset = Style.RESET_ALL


lista_alunos = []

print(Azul+"\n{:=^70}".format("Seja bem-vindo a ordem de apresentação de trabalho!".upper())+Reset)
print()
sleep(4)

print(Ciano+"---> Escreva os nomes dos alunos (Para encerrar digite 'Fim')"+Reset)
sleep(3)

while True:
    nome = str(input(Amarelo+"Digite o nome do aluno: "+Reset)).strip().capitalize()
    if nome == "Fim":
        break

    if not re.match(r"^[a-zA-ZáàâãéèêíìîïóòôõúùûüçñÁÀÂÃÉÈÊÍÌÎÏÓÒÔÕÚÙÛÜÇÑ\s-]+$", nome):# Para fazer validação dos caracteres da variável nome. 
        print(Vermelho + "Erro: O nome deve conter apenas letras e espaços." + Reset)
        continue  # Volta para o início do loop sem adicionar à lista

    elif not nome:
        print(Vermelho + "Erro: A entrada não pode estar em branco." + Reset)
        continue  # Volta para o início do loop sem adicionar à lista

    else:
        lista_alunos.append(nome)


print(Azul+"\n{:=^70}".format("Lista de alunos cadastrados").center(70)+Reset)
if lista_alunos:
    for aluno in lista_alunos:# Para iterar pela lista de alunos
        print(f"- {Ciano}{aluno}{Reset}")


if lista_alunos:
    shuffle(lista_alunos) # Embaralha a lista de alunos
    print(Azul+"\n{:=^70}".format("Ordem de apresentação sorteada").center(70)+Reset)
    for i, aluno in enumerate(lista_alunos):# Para iterar pela lista  de alunos depois de embaralhar 
        print(f"{Verde}{i+1}. {Ciano}{aluno}{Reset}")

else:
    print(Vermelho+"Nenhum aluno para sortear."+Reset)

print(Azul+"\n{:=^70}".format("Fim da ordem de apresentação")+Reset)
print()