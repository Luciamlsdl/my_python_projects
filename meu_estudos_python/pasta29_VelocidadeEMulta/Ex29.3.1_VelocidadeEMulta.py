"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por km acima do limite de velocidade.  
"""

# Este código foi refatorado pela IA Gemini 
# Depois de escrever o código eu a peso para ela me corrigir e me dar dicas

from time import sleep
from random import randint
from colorama import init, Fore

# Inicializa o colorama para resetar as cores automaticamente após cada print
init(autoreset=True)

# Definição de constantes de cores
VERDE = Fore.GREEN
AZUL = Fore.BLUE
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN
VERMELHO = Fore.RED
MAGENTA = Fore.MAGENTA

# --- Constantes do sistema de multas ---
LIMITE_VELOCIDADE_KMH = 80
VALOR_MULTA_POR_KM = 7.00 # Usando float para garantir precisão monetária

class MonitoramentoVelocidade:
    def __init__(self):
        # Atributos para contagem e soma de dados
        self.num_veiculos_processados = 0
        self.num_veiculos_multados = 0
        self.valor_total_multas_arrecadadas = 0.0 # Inicializa como float
        self.ultimas_multas_aplicadas = [] # Armazenará os valores das multas

    def apresentar_sistema(self):
        """Exibe a mensagem de boas-vindas do sistema."""
        print(AMARELO + "\n--- Monitoramento de Velocidade na Via ---".upper())

    def obter_quantidade_veiculos(self):
        """Solicita ao usuário a quantidade de veículos a serem monitorados."""
        while True:
            try:
                quantidade = int(input(MAGENTA + "\nQual a quantidade de veículos trafegando na via: "))
                if quantidade >= 0: # Garante que a quantidade não é negativa
                    self.num_veiculos_processados = quantidade
                    return
                else:
                    print(VERMELHO + "Por favor, digite um número não negativo para a quantidade de veículos.")
            except ValueError:
                print(VERMELHO + "Erro: Por favor, digite um número inteiro válido.")

    def simular_velocidade_veiculo(self):
        """Gera uma velocidade aleatória para um veículo."""
        # A velocidade pode estar entre 40 e 200 km/h
        return randint(40, 200)

    def calcular_multa(self, velocidade_atual):
        """
        Calcula o valor da multa se a velocidade exceder o limite.
        Retorna o valor da multa (float) ou 0.0 se não houver multa.
        """
        if velocidade_atual > LIMITE_VELOCIDADE_KMH:
            km_acima_do_limite = velocidade_atual - LIMITE_VELOCIDADE_KMH
            valor_multa = km_acima_do_limite * VALOR_MULTA_POR_KM
            return valor_multa
        return 0.0

    def processar_veiculo(self, velocidade_veiculo):
        """Processa um único veículo, calculando e exibindo a multa se necessário."""
        valor_da_multa = self.calcular_multa(velocidade_veiculo)

        if valor_da_multa > 0:
            print(VERMELHO + f"\n--> MULTADO! Velocidade excedida de {LIMITE_VELOCIDADE_KMH} km/h.")
            print(VERDE + f"--> Sua velocidade atual: {velocidade_veiculo} Km/h.")
            print(MAGENTA + f"--> Valor da multa: R$:{valor_da_multa:.2f}.")

            # Atualiza os contadores e acumuladores da classe
            self.num_veiculos_multados += 1
            self.valor_total_multas_arrecadadas += valor_da_multa
            self.ultimas_multas_aplicadas.append(valor_da_multa) # Armazena o valor da multa
        else:
            print(CIANO + f"\n--> Sua velocidade atual: {velocidade_veiculo} Km/h.")
            print(AZUL + "--> Tenha um bom dia! Dirija com segurança.")

    def exibir_dados_finais(self):
        """Exibe o resumo dos dados coletados durante o monitoramento."""
        print(AMARELO + "\n--- Dados Finais do Monitoramento ---".upper())
        print(AZUL + f"--> Total de veículos processados: {self.num_veiculos_processados}.")
        print(AZUL + f"--> Quantidade de veículos multados: {self.num_veiculos_multados}.")
        print(AZUL + f"--> Valor total arrecadado com multas: R$:{self.valor_total_multas_arrecadadas:.2f}.")
        print(AZUL + f"--> Quantidade de veículos sem multa: {self.num_veiculos_processados - self.num_veiculos_multados}.")

    def iniciar_sistema(self):
        """Coordena o fluxo principal do sistema de monitoramento."""
        self.apresentar_sistema()
        self.obter_quantidade_veiculos()

        for i in range(self.num_veiculos_processados):
            sleep(1) # Simula o tempo de um veículo passando
            velocidade_do_carro = self.simular_velocidade_veiculo()
            self.processar_veiculo(velocidade_do_carro)

        self.exibir_dados_finais()

# --- Programa Principal ---
if __name__ == "__main__":
    sistema = MonitoramentoVelocidade()
    sistema.iniciar_sistema()