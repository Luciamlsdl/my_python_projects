"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado. 
"""
# Codigo feito pela Gemini IA

import os
from colorama import init, Fore, Style

# Inicializa o colorama para resetar as cores automaticamente após cada print
# Isso é útil para garantir que as cores não "vazem" para a linha de comando após a execução.
init(autoreset=True)

# Definição de constantes de cores e estilos para melhor legibilidade
VERDE = Fore.GREEN
AZUL = Fore.BLUE
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN
VERMELHO = Fore.RED
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL # Garante que o estilo volte ao normal, embora autoreset=True já ajude


def limpar_tela():
    """Limpa a tela do console para uma melhor experiência do usuário."""
    os.system('cls' if os.name == 'nt' else 'clear') # Descomente se quiser limpar a tela antes da apresentação


def apresentacao_do_codigo():
    """Exibe uma mensagem de apresentação para o usuário."""
    print(CIANO + "\n--- SISTEMA DE EMPRÉSTIMO BANCÁRIO ---".upper())


def ler_valor_numerico(mensagem: str, tipo: type, mensagem_erro: str) -> float | int:
    """
    Função genérica para ler e validar um valor numérico (float ou int).

    Args:
        mensagem (str): A mensagem a ser exibida para solicitar a entrada.
        tipo (type): O tipo de dado esperado (float ou int).
        mensagem_erro (str): A mensagem de erro para entrada inválida.

    Returns:
        float | int: O valor numérico válido inserido pelo usuário.
    """
    while True:
        try:
            valor = tipo(input(AMARELO + mensagem))
            if valor <= 0:
                print(VERMELHO + f"Desculpe: O valor não pode ser inferior ou igual a zero. Por favor, digite um valor válido.")
            else:
                return valor
        except ValueError:
            print(VERMELHO + f"Erro: {mensagem_erro} Por favor, digite um valor numérico válido!")


def calcula_valores(valor_casa: float, salario_comprador: float, anos_pagamento: int) -> tuple[float, float]:
    """
    Calcula a prestação mensal e o valor mínimo permitido (30% do salário).

    Args:
        valor_casa (float): O valor total da casa.
        salario_comprador (float): O salário mensal do comprador.
        anos_pagamento (int): A quantidade de anos para pagamento.

    Returns:
        tuple[float, float]: Uma tupla contendo (prestacao_mensal, limite_salario_30_porcento).
    """
    meses_pagamento = anos_pagamento * 12
    prestacao_mensal = valor_casa / meses_pagamento
    limite_salario_30_porcento = salario_comprador * 0.30
    return prestacao_mensal, limite_salario_30_porcento


def mostra_resultado(valor_casa: float, anos_parcela: int, prestacao: float, valor_minimo: float):
    """
    Exibe o resultado do empréstimo (aprovado ou negado).

    Args:
        valor_casa (float): O valor da casa.
        anos_parcela (int): Os anos para pagamento.
        prestacao (float): O valor da prestação mensal.
        valor_minimo (float): O limite de 30% do salário.
    """
    print(f'''
{CIANO}--- Detalhes da Simulação ---
Para comprar uma casa de R$:{valor_casa:.2f} em {anos_parcela} anos,
a prestação mensal será de R$:{prestacao:.2f}.
Seu limite de 30% do salário é de R$:{valor_minimo:.2f}.
''')

    if prestacao <= valor_minimo:
        print(VERDE + "🎉 Parabéns! Empréstimo aprovado!")
    else:
        print(VERMELHO + "😔 Empréstimo negado. A prestação excede 30% do seu salário.")

    print(CIANO + "---------------------------------------" + RESET) # Garante reset no final


def executar_programa():
    """Função principal que orquestra a execução do programa."""
    limpar_tela() # Limpa a tela antes de começar
    apresentacao_do_codigo()

    # Utilizando a função genérica para ler as entradas
    valor_casa = ler_valor_numerico("-->Qual é o valor da casa? R$: ", float, "Valor da casa inválido!")
    valor_salario = ler_valor_numerico("-->Qual é o seu salário? R$: ", float, "Valor do salário inválido!")
    anos_parcela = ler_valor_numerico("-->Em quantos anos você deseja pagar?: ", int, "Quantidade de anos inválida!")

    prestacao, valor_minimo = calcula_valores(valor_casa, valor_salario, anos_parcela)
    mostra_resultado(valor_casa, anos_parcela, prestacao, valor_minimo)


# Bloco principal para iniciar a execução do programa
if __name__ == "__main__":
    executar_programa()