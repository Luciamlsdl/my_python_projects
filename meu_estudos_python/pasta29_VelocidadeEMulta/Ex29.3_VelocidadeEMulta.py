"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por km acima do limite de velocidade.  
"""

from time import sleep
from random import randint
from colorama import init, Fore

init(autoreset=True)
VERDE = Fore.GREEN
AZUL = Fore.BLUE
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN
VERMELHO = Fore.RED
MAGENTA = Fore.MAGENTA



class MultaVelocidade:
    def __init__(self):
        self.total_veículos = 0
        self.velocidade = 0
        self.multa = 0
        self.sem_multa = 0
        self.todas_as_multas = 0
        self.total_valor_multas = 0
        self.somar_multas = 0
        self.total_multa = 0
        self.veículos = 0

        self.multas = []


    def apresentação(self):
        print(AMARELO+"\nMonitoramento de velocidade na via".upper())


    def coleta_velocidade(self):
        self.velocidade = randint(40, 200)


    def total_de_veículos(self):
        while True:
            try:
                self.total_veículos = int(input(MAGENTA+"\nQual a quantidade de veículos trafegando va via: "))
                break
            except ValueError:
                print("Por favor! Digite um valor válido")


    def gerenciador_de_multa(self):
        if self.velocidade > 80:
            print(VERDE+ f"\n--> Você foi multado por exceder a velocidade da via.")
            self.multa = (self.velocidade - 80) * 7
            self.multas.append(self.multa)
            self.total_multa += 1

            print(VERMELHO+ f"--> Sua velocidade é de {self.velocidade}Km/h.")
            print(MAGENTA+ f"--> O valor da multa é de R$:{self.multa:.2f}.")
            print()
        else:
            print(CIANO+ "\nTenha um bom dia! Dirija com segurança.")
            self.sem_multa += 1
            print()

    
    def dados_coletados(self):
        self.todas_as_multas = self.total_multa
        self.somar_multas = sum(self.multas)

        print(AMARELO+ "Dados da rodovia".upper())
        print(AZUL+ f"--> A quantidade de pessoas multadas foram {self.todas_as_multas} pessoas.")
        print(AZUL+ f"--> O valor total de todas as multas foram R$:{self.somar_multas:.2f}.")
        print(AZUL+ f"--> O total de pessoa que não foram multadas são {self.sem_multa} pessoas.")


    def sistema(self):
        self.apresentação()
        self.total_de_veículos()
        for i in range(0, self.total_veículos):
            sleep(1)
            self.coleta_velocidade()
            self.gerenciador_de_multa()
        self.dados_coletados()


#Programa principal
if __name__ == "__main__":
    start = MultaVelocidade()
    start.sistema()