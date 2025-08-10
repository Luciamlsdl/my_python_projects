"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado. 
"""

#Este código está em forma de classe (poo = Programação Orientada a Objeto)

import os
from colorama import init, Fore, Style

# Inicializa o colorama para resetar cores automaticamente
init(autoreset=True)

# Definição de constantes de cores
VERDE = Fore.GREEN
AZUL = Fore.BLUE
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN
VERMELHO = Fore.RED
RESET = Style.RESET_ALL

class EmprestimoBancario:
    """
    Classe responsável por simular um empréstimo bancário para compra de imóvel.
    """

    def __init__(self):
        """
        Inicializa os atributos principais do empréstimo.
        """
        self.valor_casa = 0.0
        self.valor_salario = 0.0
        self.anos_pagar = 0

    def limpar_tela(self):
        """
        Limpa a tela do terminal para melhor visualização.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def apresentacao_do_codigo(self):
        """
        Exibe a mensagem de boas-vindas ao usuário.
        """
        print(CIANO + "\n==== SISTEMA DE EMPRÉSTIMO BANCÁRIO ====\n")

    def ler_valor_numerico(self, mensagem: str, tipo: type, mensagem_erro: str):
        """
        Lê e valida um valor numérico digitado pelo usuário.

        Args:
            mensagem (str): Texto exibido ao solicitar entrada.
            tipo (type): Tipo de dado esperado (float ou int).
            mensagem_erro (str): Mensagem de erro personalizada.

        Returns:
            float | int: Valor numérico válido.
        """
        while True:
            try:
                valor = tipo(input(AMARELO + mensagem))
                if valor <= 0:
                    print(VERMELHO + "⚠️ O valor deve ser maior que zero.")
                else:
                    return valor
            except ValueError:
                print(VERMELHO + f"❌ Erro: {mensagem_erro}")

    def calcula_valores(self, valor_casa: float, valor_salario: float, anos_pagar: int):
        """
        Calcula a prestação mensal e o limite de 30% do salário.

        Args:
            valor_casa (float): Valor total do imóvel.
            valor_salario (float): Salário mensal do comprador.
            anos_pagar (int): Prazo de pagamento em anos.

        Returns:
            tuple: (prestacao_mensal, limite_salario)
        """
        meses = anos_pagar * 12
        prestacao = valor_casa / meses
        limite = valor_salario * 0.30
        return prestacao, limite

    def mostra_resultado(self, valor_casa, anos_pagar, prestacao, limite):
        """
        Exibe o resultado da simulação do empréstimo.

        Args:
            valor_casa (float): Valor do imóvel.
            anos_pagar (int): Prazo de pagamento.
            prestacao (float): Valor da prestação mensal.
            limite (float): Limite permitido (30% do salário).
        """
        print(f'''
                {AZUL}--- Detalhes da Simulação ---
                🏠 Valor da casa: R$ {valor_casa:.2f}
                📆 Prazo: {anos_pagar} anos ({anos_pagar * 12} meses)
                💰 Prestação mensal: R$ {prestacao:.2f}
                📉 Limite de 30% do salário: R$ {limite:.2f}
                ''')

        if prestacao <= limite:
            print(VERDE + "✅ Empréstimo aprovado! Parabéns pela conquista!")
        else:
            print(VERMELHO + "❌ Empréstimo negado. A prestação excede 30% do seu salário.")

        print(CIANO + "----------------------------------------" + RESET)

    def executar_programa(self):
        """
        Executa o fluxo completo do programa.
        """
        self.limpar_tela()
        self.apresentacao_do_codigo()

        # Coleta de dados do usuário
        self.valor_casa = self.ler_valor_numerico("Informe o valor da casa (R$): ", float, "Valor inválido.")
        self.valor_salario = self.ler_valor_numerico("Informe seu salário mensal (R$): ", float, "Salário inválido.")
        self.anos_pagar = self.ler_valor_numerico("Em quantos anos deseja pagar?: ", int, "Prazo inválido.")

        # Cálculo e exibição do resultado
        prestacao, limite = self.calcula_valores(self.valor_casa, self.valor_salario, self.anos_pagar)
        self.mostra_resultado(self.valor_casa, self.anos_pagar, prestacao, limite)

# 🔁 Execução do programa
if __name__ == "__main__":
    simulador = EmprestimoBancario()
    simulador.executar_programa()





































