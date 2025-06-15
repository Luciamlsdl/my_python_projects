"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela seo usuário venceu ou perdeu.
"""

#Este programa esta em sua forma de classe 
# Biblioteca Random usando Randint para embaralhar os números
# Biblioteca Time para colocar tempo no código
# Biblioteca Colorama para dar cor ao código


from random import randint
from time import sleep
from colorama import init, Fore, Style

init(autoreset=True)

# --- Constantes de Cores ---
VERDE = Fore.GREEN
AZUL = Fore.BLUE
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN

class JogoDeAdivinhação:
    def __init__(self, min_num=0, max_num=5):
        self.computador = 0
        self.jogador = 0
        self.NUM_MINIMO = min_num
        self.NUM_MAXIMO = max_num
        self.pontos_jogador = 0  # Pontos do jogador
        self.pontos_computador = 0 # Pontos do computador
        self.rodada_atual = 0    # Rodada atual
        self.total_rodadas = 0   # Total de rodadas a serem jogadas

    def apresentação(self):
        print()
        print(AMARELO + "-=-" * 13)
        print(CIANO + "seja bem vindo a o jogo de adivinhação".upper())
        print(AMARELO + "-=-" * 13)
        sleep(2)

    def perguntar_numero_rodadas(self):
        while True:
            try:
                rodadas_input = input(CIANO + "Quantas rodadas você gostaria de jogar? (Pressione Enter para 5 rodadas): ").strip()
                if not rodadas_input:
                    self.total_rodadas = 5
                    print(AZUL + "Ok! Vamos jogar 5 rodadas.")
                    break
                
                num_rodadas = int(rodadas_input)
                if num_rodadas > 0:
                    self.total_rodadas = num_rodadas
                    print(AZUL + f"Ok! Vamos jogar {self.total_rodadas} rodadas.")
                    break
                else:
                    print(VERMELHO + "Por favor, digite um número positivo de rodadas.")
            except ValueError:
                print(VERMELHO + "Entrada inválida. Por favor, digite um número inteiro.")

    def escolhaComputador(self):
        self.computador = randint(self.NUM_MINIMO, self.NUM_MAXIMO)

    def conviteDoComputador(self):
        print(VERDE + "\nCOMPUTADOR")
        print(AZUL + f"-->Vou pensar em um número de {self.NUM_MINIMO} a {self.NUM_MAXIMO}. Tente adivinhar!")
        sleep(2)

    def escolhaDoJogador(self):
        while True:
            try:
                self.jogador = int(input(AMARELO + f"Em que número eu pensei (entre {self.NUM_MINIMO} e {self.NUM_MAXIMO})?: "))
                if self.NUM_MINIMO <= self.jogador <= self.NUM_MAXIMO:
                    break
                else:
                    print(VERMELHO + f"O valor digitado deve ser entre {self.NUM_MINIMO} e {self.NUM_MAXIMO}.")
            except ValueError:
                print(VERMELHO + "Entrada inválida. Por favor, digite um número inteiro.")

    def tempoParaPensar(self):
        print()
        print(AMARELO + "Processando..")
        sleep(1)
        print(AMARELO + "Processando....")
        sleep(1)
        print(AMARELO + "Processando......")
        sleep(1)
        print()

    def exibirVencedor(self):
        if self.jogador == self.computador:
            print(VERDE + "Parabéns! Você venceu esta rodada!")
            self.pontos_jogador += 1
        else:
            print(VERMELHO + f"Vitória do Computador! Eu pensei no número {self.computador}, não no {self.jogador}.") # type: ignore
            self.pontos_computador += 1
        print()

    def exibir_placar_final(self):
        print(AMARELO + "\n--- Placar Final ---")
        print(CIANO + f"Você: {self.pontos_jogador} vitórias")
        print(CIANO + f"Computador: {self.pontos_computador} vitórias") # type: ignore

        if self.pontos_jogador > self.pontos_computador:
            print(VERDE + "Parabéns! Você é o grande vencedor do jogo!")
        elif self.pontos_jogador < self.pontos_computador:
            print(VERMELHO + "O Computador foi o grande vencedor do jogo!")
        else:
            print(AZUL + "O jogo terminou empatado!")
        
        print(AMARELO + "Obrigado por jogar! Até a próxima!")


    def jogar(self):
        """Método principal para iniciar e gerenciar o ciclo completo do jogo."""
        self.apresentação()
        self.perguntar_numero_rodadas()

        for self.rodada_atual in range(1, self.total_rodadas + 1):
            print(AMARELO + f"\n--- Rodada {self.rodada_atual}/{self.total_rodadas} ---")
            self.escolhaComputador()
            self.conviteDoComputador()
            self.escolhaDoJogador()
            self.tempoParaPensar()
            self.exibirVencedor()
            print(CIANO + f"Placar atual: Você {self.pontos_jogador} x {self.pontos_computador} Computador")

        self.exibir_placar_final()


# --- Programa principal ---
if __name__ == "__main__":
    jogo = JogoDeAdivinhação(min_num=0, max_num=5) # Você pode ajustar os limites aqui
    jogo.jogar()