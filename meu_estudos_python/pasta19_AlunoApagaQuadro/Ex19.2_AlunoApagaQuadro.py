"""
Uma professora quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ela, lendo os nomes deles e escrevendo o
nome do escolhido na tela.
"""

# Este programa está em sua forma de função porem aprimorada usando a importação do biblioteca random

from random import choice # Função para choice da biblioteca random para embaralhar os nomes e escolher um 
from colorama import init, Fore, Style # Biblioteca colorama para dar cor ao código
from time import sleep # Função para dar tem ao código

# Cria as variáveis com suas determinadas cores
verde = Fore.GREEN
vermelho = Fore.RED
azul = Fore.BLUE
amarelo = Fore.YELLOW
ciano = Fore.CYAN
reset = Style.RESET_ALL

lista_aluno = []

def saudação():
    print(azul+"\n     Seja bem-vindo ao programa sorteia aluno!".upper()+reset)
    sleep(4)
    print(amarelo+"Digite o nome do aluno (digite Fim para encerrar!)\n".upper()+reset)
    sleep(3)


def coleta_nome():
    while True:
        nome = str(input(verde+"Digite os nomes dos alunos!: "+reset)).strip().capitalize()
        if nome == "Fim":
            break
        elif nome and nome.replace(" ", "").isalpha:
            lista_aluno.append(nome)
        elif not nome:
            print(vermelho+"Por favor! Digite um nome válido!"+reset)
        else:
            print(vermelho+"O nome deve conter apenas letras!"+reset)
        

def sorteia_aluno():
    if not lista_aluno:
        print(vermelho+"Não há aluno na lista para sortear!"+reset)
        return None
    escolhido = choice(lista_aluno)
    return escolhido


def mostrar_escolhido(aluno):
    print()
    print(ciano+f"Lista de alunos:\n{' ,'.join(lista_aluno)}.\n"+reset)
    print(verde+f"O aluno escolhido para apagar o quadro foi {aluno}.\n"+reset)
    print(vermelho+"Fim do programa!"+reset)


# Programa principal
if __name__ == "__main__":
    init(autoreset = True)
    saudação()
    coleta_nome()
    escolhido = sorteia_aluno()
    mostrar_escolhido(escolhido)
    