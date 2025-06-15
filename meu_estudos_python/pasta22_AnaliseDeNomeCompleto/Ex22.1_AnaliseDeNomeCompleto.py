"""
Crie um programa que leia um nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas 
-> O nome com todas as letras minúsculas
-> Quantas letras tem ao todo (Sem espaços)
-> Quantas letras tem o primeiro nome
"""

# Este código está em sua forma mais simples 

# Importação da biblioteca time para por tempo de execução no código
from time import sleep

# Importação da biblioteca de cores
from colorama import init, Fore, Style
Verde = Fore.GREEN
Vermelho = Fore.RED
Azul = Fore.BLUE
Amarelo = Fore.LIGHTYELLOW_EX
Ciano = Fore.CYAN

Reset = Style.RESET_ALL

init(autoreset=True)

print(Ciano+"\n{:*^70}".format(" Seja bem-vindo ao analisador de nome ".upper())+Reset)
sleep(3)

nome = str(input(f"\n{Azul}Escreva o seu nome completo: {Reset}")).strip().capitalize()
sleep(2)
print()

print("-"* 60 )
print(f"{Verde}O seu nome com todas as letras maiúsculas:{Reset}")
print(f"{Azul}{nome.upper()}{Reset}")
print("-"* 60 )
sleep(2)
print()

print("-"* 60 )
print(f"{Verde}O seu nome com todas as letras minúsculas:{Reset}")
print(f"{Azul}{nome.lower()}{Reset}")
print("-"* 60 )
sleep(2)
print()

print("-"* 60 )
print(f"{Verde}O seu nome tem ao todo {len(nome) - nome.count(' ')} leras (Sem contar os espaços):{Reset}")
print("-"* 60 )
sleep(2)
print()

print("-"* 60 )
print(f"{Verde}O seu primeiro nome tem {nome.find(' ')} letras{Reset}")
print(f"{Azul}{nome.lower()}{Reset}")
print("-"* 60 )
print()