"""
Crie um programa que leia um nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas 
-> O nome com todas as letras minúsculas
-> Quantas letras tem ao todo (Sem espaços)
-> Quantas letras tem o primeiro nome
"""

# Este código está em sua forma de função 

# Importação da biblioteca time para por tempo de execução no código
from time import sleep

# Importação do unicodedata para fazer a validação do nome para não aceitar caracteres indesejados
import unicodedata 

# Importação da biblioteca de cores
from colorama import init, Fore, Style
Verde = Fore.GREEN
Vermelho = Fore.RED
Azul = Fore.BLUE
Amarelo = Fore.LIGHTYELLOW_EX
Ciano = Fore.CYAN

Reset = Style.RESET_ALL

init(autoreset=True)

def valida_nome(nome):
    if not nome.strip():
        return False, f"{Vermelho}A entrada de nome não pode estar em branco!{Reset}"

    for caractere in nome:
        letras = unicodedata.category(caractere)

        if not (letras.startswith('L') or caractere.isspace()):
            return False, f"{Vermelho}O nome deve conter apenas letras e espaços!{Reset}"
    return True, None


def apresentação():
    print(Ciano + "\n{:*^70}".format(" Seja bem-vindo ao analisador de nome! ".upper()) + Reset)
    sleep(3)
    print()


def firulas():
    print(f"{Vermelho}-{Reset}" * 60)


def nome_maiúsculo(nome):
    firulas()
    print(f"{Amarelo}O seu nome em letras maiúsculas:{Reset}.")
    print(f"{Verde}{nome.upper()}{Reset}.")
    firulas()
    sleep(3)
    print()


def nome_minúsculo(nome):
    firulas()
    print(f"{Amarelo}O seu nome em letras minúsculas:{Reset}")
    print(f"{Verde}{nome.lower()}{Reset}")
    firulas()
    sleep(3)
    print()


def quantidade_de_letras(nome):
    firulas()
    print(f"{Amarelo}O seu nome tem ao todo {len(nome) - nome.count(' ')} letras.{Reset}")
    firulas()
    sleep(3)
    print()


def quantidade_letras_primeiro_nome(nome):
    firulas()
    print(f"{Amarelo}O seu primeiro nome tem ao todo {nome.find(' ')} letras.{Reset}")
    firulas()
    print()



def ler_nome():
    while True:
        nome = str(input(f"{Azul}\n--> Escreva seu nome completo: {Reset}")).strip().capitalize()
        print()
        sleep(3)
        valido, mensagem_erro = valida_nome(nome)

        if not valido:
            print(f"{mensagem_erro}")
            continue
        else:
            nome_valido = nome
            return nome_valido
        

# Programa principal
while True:
        apresentação()
        valor_nome = ler_nome()
        nome_maiúsculo(valor_nome)
        nome_minúsculo(valor_nome)
        quantidade_de_letras(valor_nome)
        quantidade_letras_primeiro_nome(valor_nome)

        while True: 
            parar = str(input(f"{Ciano}Quer analisar outro nome (S = Sim ou N = Não): {Reset}")).strip().upper()[0]
            if parar == "N":
                break 
            elif parar == "S":
                break 
            else:
                print(f"{Vermelho}Opção inválida. Digite 'S' para Sim ou 'N' para Não.{Reset}")
        if parar == "N":
            break 
