"""
Uma professora quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ela, lendo os nomes deles e escrevendo o
nome do escolhido na tela.
"""

# Este programa está em sua forma de classe porem aprimorada usando a importação do biblioteca random
from colorama import init, Fore, Style
from random import choice
from time import sleep


# Cores para o código
Azul = Fore.BLUE
Verde = Fore.GREEN
Amarelo = Fore.YELLOW
Vermelho = Fore.RED
Ciano = Fore.CYAN
Magenta = Fore.MAGENTA
Amar = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL

lista_nomes = []

class SorteiaAluno:
    def __init__(self):
        self.nomes = lista_nomes
        self.escolhido = ""
    

    def sorteador_aluno(self):
        if not self.nomes:
            print(Vermelho+"Não há aluno na lista para sortear!"+reset)
            return None
        self.escolhido = choice(self.nomes)
        return self.escolhido
    

    def mostrar_escolhido(self):
        print()
        print(Azul+f"Segue a lista de alunos:\n{' ,'.join(lista_nomes)}."+reset)
        print()
        print(Magenta+f"E o aluno escolhido para apagar o quadro:\nFoi {self.escolhido}")
        print()
        print(Vermelho+"Fim do código".upper()+reset)
    

class GerenciadorDeSaudação:
    @staticmethod
    def saudação():
        print(Magenta+"\n{:-^60}".format("Seja bem vindo ao soreador de aluno!".upper())+reset)
        print()
        sleep(3)


    @staticmethod
    def dicaDeInicio():
        print(Ciano+"--> Digite os nomes dos alunos ou (Digite 'Fim' para encerrar!)"+reset)
        sleep(3)

class GerenciadorDeAlunos:
    @staticmethod
    def ler_nome_alunos():
        while True:
            nomes = str(input(Amarelo+"Digite o nome do aluno: "+reset)).strip().capitalize()
            if nomes == "Fim":
                break
            elif nomes and nomes.replace(" ","").isalpha():
                lista_nomes.append(nomes)
            elif not nomes:
                print(Vermelho+"Por favor! Digite um nome válido!"+reset)
            else:
                print(Vermelho+"O nome deve conter apenas letras!"+reset)



# programa principal
saudação = GerenciadorDeSaudação()
saudação.saudação()
saudação.dicaDeInicio()

nome_alunos = GerenciadorDeAlunos()
nome_alunos.ler_nome_alunos()

alunos = SorteiaAluno()
alunos.sorteador_aluno()
alunos.mostrar_escolhido()