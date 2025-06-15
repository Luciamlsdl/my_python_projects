from random import randint
from time import sleep
from colorama import init, Fore

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
        
        # Pontos da fase atual (resetados a cada fase)
        self.pontos_jogador_fase = 0
        self.pontos_computador_fase = 0

        # Pontos totais do jogo (acumulados)
        self.pontos_jogador_total = 0
        self.pontos_computador_total = 0

        self.rodada_atual = 0
        # self.total_rodadas # Removido, pois cada fase tem suas próprias rodadas
        
        self.fases = [
            (0, 3),  # Fase 1
            (0, 5),  # Fase 2
            (0, 7),  # Fase 3
            (0, 9)   # Fase 4
        ]
        self.fase_atual_indice = 0
        self.rodadas_por_fase = 3 # Número fixo de rodadas por fase

    def apresentação(self):
        print()
        # Indentação corrigida aqui
        print(AMARELO + "-=-" * 13)
        print(CIANO + "seja bem vindo a o jogo de adivinhação".upper())
        print(AMARELO + "-=-" * 13)
        sleep(2)

    def iniciar_nova_fase(self):
        if self.fase_atual_indice < len(self.fases):
            self.NUM_MINIMO, self.NUM_MAXIMO = self.fases[self.fase_atual_indice]
            print(AMARELO + f"\n--- Entrando na Fase {self.fase_atual_indice + 1}! ---")
            print(AZUL + f"Agora vou pensar em um número entre {self.NUM_MINIMO} e {self.NUM_MAXIMO}.")
            
            # Resetar pontos da fase para a nova fase
            self.pontos_jogador_fase = 0
            self.pontos_computador_fase = 0
            self.rodada_atual = 0 # Resetar a contagem da rodada dentro da fase
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
            self.pontos_jogador_fase += 1
            self.pontos_jogador_total += 1 # Acumula pontos totais
        else:
            print(VERMELHO + f"Vitória do Computador! Eu pensei no número {self.computador}, não no {self.jogador}.")
            self.pontos_computador_fase += 1
            self.pontos_computador_total += 1 # Acumula pontos totais
        print()

    def exibir_placar_final_do_jogo(self): # Renomeado para maior clareza
        print(AMARELO + "\n--- Placar Final do Jogo ---")
        print(CIANO + f"Suas vitórias totais: {self.pontos_jogador_total}")
        print(CIANO + f"Vitórias totais do Computador: {self.pontos_computador_total}")

        if self.pontos_jogador_total > self.pontos_computador_total:
            print(VERDE + "🎉 Parabéns! Você é o grande campeão do jogo! 🎉")
        elif self.pontos_jogador_total < self.pontos_computador_total:
            print(VERMELHO + "🤖 O Computador foi o grande vencedor do jogo! 🤖")
        else:
            print(AZUL + "🤝 O jogo terminou empatado! 🤝")
        
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
                self.conviteDoComputador()
                self.escolhaDoJogador()
                self.tempoParaPensar()
                self.exibirVencedor()
                print(CIANO + f"Placar da Fase: Você {self.pontos_jogador_fase} x {self.pontos_computador_fase} Computador")
            
            # Lógica de fim de fase / avanço
            print(AMARELO + f"\n--- Fim da Fase {self.fase_atual_indice + 1} ---")
            if self.pontos_jogador_fase > self.pontos_computador_fase:
                print(VERDE + "🏆 Parabéns! Você venceu esta fase e avança para a próxima! 🏆")
                self.fase_atual_indice += 1 # Avança para a próxima fase
                sleep(2)
            else:
                print(VERMELHO + "😔 Você não conseguiu vencer esta fase. Fim de jogo! 😔")
                break # O jogo termina se não passar da fase

        # Mensagem final do jogo
        if self.fase_atual_indice == len(self.fases): # Se o loop terminou porque todas as fases foram completadas
            print(VERDE + "\n--- 🎉 Parabéns! Você completou todas as fases do jogo! 🎉 ---")
        
        self.exibir_placar_final_do_jogo() # Chama a função para mostrar o placar final geral

# --- Programa principal ---
if __name__ == "__main__":
    jogo = JogoDeAdivinhação() # Os limites iniciais agora são definidos pelas fases
    jogo.jogar()