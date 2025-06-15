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
from colorama import init, Fore

init(autoreset=True)

# --- Constantes  de Cores ---

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
        self.ponto_jogador = 0
        self.ponto_computador = 0
        self.rodada_atual = 0
        self.total_rodadas = 0
        self.fases = [
            (0, 3), #Fase 1 (índice 0 )
            (0, 5), #Fase 2 (índice 1)
            (0, 7), #Fase 3 (índice 2)
            (0, 9) #Fase 4 (índice 3)
        ]
        self.fase_atual_indice = 0
        self.rodadas_por_fase = 3


    def apresentação(self):
        print()
        print(AMARELO + "-=-" * 13)
        print(CIANO + "seja bem vindo a o jogo de adivinhação".upper())
        print(AMARELO + "-=-" * 13)
        sleep(2)
        
    def iniciar_nova_fase(self):
        if self.fase_atual_indice < len(self.fases):
            self.NUM_MINIMO, self.NUM_MAXIMO = self.fases[self.fase_atual_indice]
            print(AMARELO + f"\n--- Entrando na Fase {self.fase_atual_indice + 1}! ---")
            print(AZUL + f"Agora vou pensar em um número entre {self.NUM_MINIMO} e {self.NUM_MAXIMO}.")
    
            self.pontos_jogador = 0
            self.pontos_computador = 0
            self.rodada_atual = 0
            return True
        else:
            return False # Todas as fases foram completadas    


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

        while self.fase_atual_indice < len(self.fases):
            if not self.iniciar_nova_fase():
                break # Sai se não houver mais fases

            print(AMARELO + f"Prepare-se para a Fase {self.fase_atual_indice + 1}!")
            sleep(1)

            for self.rodada_atual in range(1, self.rodadas_por_fase + 1):
                print(AMARELO + f"\n--- Fase {self.fase_atual_indice + 1} - Rodada {self.rodada_atual}/{self.rodadas_por_fase} ---")
                self.escolhaComputador()
                self.conviteDoComputador() # Esta mensagem pode ser adaptada para a fase
                self.escolhaDoJogador()
                self.tempoParaPensar()
                self.exibirVencedor()
                print(CIANO + f"Placar da Fase: Você {self.pontos_jogador} x {self.pontos_computador} Computador")
            
            # Lógica de fim de fase / avanço
            print(AMARELO + f"\n--- Fim da Fase {self.fase_atual_indice + 1} ---")
            if self.pontos_jogador > self.pontos_computador:
                print(VERDE + "Parabéns! Você venceu esta fase e avança para a próxima!")
                self.fase_atual_indice += 1 # Avança para a próxima fase
                sleep(2)
            else:
                print(VERMELHO + "Você não conseguiu vencer esta fase. Fim de jogo!")
                break # O jogo termina se não passar da fase

        # Mensagem final do jogo
        if self.fase_atual_indice == len(self.fases):
            print(VERDE + "\n--- Parabéns! Você completou todas as fases do jogo! ---")
        
        self.exibir_placar_final_geral() # Criar um placar final que acumula os pontos totais (opcional)
        print(AMARELO + "Obrigado por jogar! Até a próxima!")



# --- Programa principal ---
if __name__ == "__main__":
    jogo = JogoDeAdivinhação(min_num=0, max_num=5) # Você pode ajustar os limites aqui
    jogo.jogar()