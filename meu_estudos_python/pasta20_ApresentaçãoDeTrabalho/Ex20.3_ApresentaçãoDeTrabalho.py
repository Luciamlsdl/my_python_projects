"""
Ordem de apresentação de trabalho de alunos.
Faça um programa que leia o nome de seus alunos e mostre a ordem sorteada. 
"""

# Este programa está em sua forma de classe 
# Porem usando a biblioteca random com a função shuffle 
# Usando a biblioteca colorama para dar cor ao código
# Temos também a biblioteca time importando o sleep para dar tempo ao código

from random import shuffle
from colorama import init,Fore,Style
from time import sleep
import unicodedata

# Cores para o código
init(autoreset=True)

Ciano = Fore.CYAN
Azul = Fore.BLUE
Amarelo = Fore.LIGHTYELLOW_EX
vermelho = Fore.RED
Verde = Fore.GREEN

Reset = Style.RESET_ALL

lista_alunos = []

class ListaDeApresentação:
    def __init__(self):
        self.lista_alunos = []

    def adicionar_aluno(self, nome):
        self.lista_alunos.append(nome)
        

    def mostrar_lista_alunos(self):
        print(Ciano+"\n{:=^70}".format("Lista de alunos cadastrados").center(70)+Reset)

        if self.lista_alunos:
            for aluno in self.lista_alunos:
                print(f"- {Azul}{aluno}{Reset}")
        else:
            print(vermelho+"Alista de alunos está vazia."+Reset)


    def mostrar_ordem_de_trabalho(self):
        if self.lista_alunos:
            shuffle(self.lista_alunos)
            print(Ciano+"\n{:=^70}".format("Ordem de apresentação sorteada").center(70)+Reset)

            for i, aluno in enumerate(self.lista_alunos):
                print(f"{Azul}{i+1}. {Ciano}{aluno}{Reset}")
        else:
            print(vermelho+"Nenhum aluno para sortear."+Reset)

        print(Amarelo+"\n{:=^70}".format("Fim da ordem de apresentação!")+Reset)
        print()


class SaudaçãoDeCódigo:
    @staticmethod
    def saudação_inicial():
        print(Ciano + "\n{:=^70}".format("Bem-vindo a ordem de apresentação de trabalho!").upper() + Reset)
        print()
        sleep(3)

        print(Azul+"---> Digite o nome do aluno (Digite Fim para encerrar)"+Reset)
        sleep(2)


class ValidaçãoDeNome():
    @staticmethod
    def valida_nome(nome):
        if not nome.strip():
            return False, "A entrada não pode estar em branco!"

        for caractere in nome:
            categoria = unicodedata.category(caractere)
            if not (categoria.startswith('L') or caractere.isspace()):
                return False, "O nome deve conter apenas letra e espaço!"
        return True, None
    
    
# Programa principal
lista_de_apresentacao = ListaDeApresentação()
saudação = SaudaçãoDeCódigo.saudação_inicial()
while True:
    nome = str(input(Amarelo+"Digite o nome do aluno: ")).strip().capitalize()
    if nome == "Fim":
        break
    valido, mensagem_erro = ValidaçãoDeNome.valida_nome(nome)

    if not valido:
        print(vermelho + f"ERRO: {mensagem_erro}" +Reset)
        continue
    else:
        lista_de_apresentacao.adicionar_aluno(nome) 

lista_de_apresentacao.mostrar_lista_alunos()
lista_de_apresentacao.mostrar_ordem_de_trabalho()

