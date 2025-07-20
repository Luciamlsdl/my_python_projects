"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado. 
"""

# Programa em sua forma função

#Importação do modulo que da cores ao código
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


def apresentação_do_código():
    """
    Função que faz a apresentação do código ao usuário

    Args:
        Não possui argumentos
    """
    print(CIANO + "\n---Sistema de empréstimo bancário---".upper())


def ler_valor_da_casa():
    """
    Função que le o valor da casa

    Return:
        Que retorna o valor da casa
    """
    while True:
        try:
            casa = float(input(AMARELO +"\n-->Qual é o valor da casa? R$: "))
            if casa <= 0:
                print(VERMELHO +"Desculpe: O valor da casa não pode ser um valor inferior a 0")
            return casa
        except ValueError:
            print(VERMELHO +"Erro: Por favor! Digite um valor valido!")


def ler_salario():
    """
    Função que le o salário do usuário

    Return:
        Retorna o valor do salário do usuário 
    """
    while True:
        try:
            salario = float(input(AMARELO + "-->Qual é o valor do seu salário? R$: "))
            if salario <= 0:
                print(VERMELHO + "Desculpe: O seu salário não pode ser inferior a 0!")
            return salario
        except ValueError:
            print(VERMELHO + "Erro: Por favor! Digite um valor valido!")



def ler_anos_a_pagar():
    """
    Função que a quantidade de anos que o usuário deseja para a casa

    Return:
        Retorna o valor do salário do  usuário
    """
    while True:
        try:
            ano_a_pagar = int(input(AMARELO + "-->Em quantos anos você deseja pagar?: "))
            if ano_a_pagar <= 0:
                print(VERMELHO + "Desculpe: O valor anos não pode ser inferior a 0!")
            return ano_a_pagar
        except ValueError:
            print(VERMELHO + "Erro: Por favor! Digite um valor valido!")


def calcula_valores(val_casa, val_salario, val_anos):
    """
    Função que faz o calculo da prestação e valor minimo para a parcela da casa

    Args:
        val_casa (float) Valor da casa para a compra
        val_salario (float) Valor do salário do comprador
        val_anos (int) Quantidade de anos que sera a parcela

    Return:
        retorna o valor da prestação
        retorna o valor minimo a se pagar   
    """
    prestacao = val_casa / (val_anos * 12)
    valor_minimo = val_salario * 30 / 100
    return prestacao, valor_minimo


def mostra_resultado(valor_casa, anos_parcela, prestacao, valor_minimo):
    
    print(f'''
        Para comprar uma casa de R$:{valor_casa:.2f} em {anos_parcela} anos\n
        A prestação será de R$:{prestacao:.2f}
        ''')

    if prestacao <= valor_minimo:
        print(AZUL + "Empréstimo aprovado!")

    else:
        print(VERDE + "Empréstimo negado!")


def executador_de_programa():
    """
    Função que executa do código
    """
    apresentação_do_código()
    valor_casa = ler_valor_da_casa()
    valor_salario = ler_salario()
    anos_parcela = ler_anos_a_pagar()
    prestacao, valor_minimo = calcula_valores(valor_casa, valor_salario, anos_parcela)
    mostra_resultado(valor_casa, anos_parcela, prestacao, valor_minimo)


#Programa principal
executador_de_programa()