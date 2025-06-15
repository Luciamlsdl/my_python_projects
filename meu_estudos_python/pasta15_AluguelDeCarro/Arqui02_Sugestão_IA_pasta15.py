from InquirerPy import prompt
from colorama import init, Fore, Style

# Definição de cores como constantes
VERDE = Fore.GREEN
VERMELHO = Fore.RED
AZUL_CLARO = Fore.LIGHTBLUE_EX
CIANO = Fore.CYAN
AMARELO_CLARO = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

def nome_loja():
    """Retorna o nome da loja."""
    return "ALUGANDO SONHOS"

def coletar_nome_cliente():
    """Solicita e retorna o nome do cliente, validando a entrada."""
    while True:
        try:
            nome = input(AZUL_CLARO + "Qual é o  nome do cliente?: " + RESET).strip().capitalize()
            if nome and not nome.isnumeric():
                return nome
        except ValueError:
            print(VERMELHO + "Por favor! Digite um nome válido." + RESET)

def escolher_marca_modelo():
    """Permite ao usuário escolher a marca e o modelo do carro."""
    marcas_modelos = {
        "Chevrolet": ["Tracker", "Ônix", "Cruze", "S10", "Equinox"],
        "Fiat": ["Argo", "Cronos", "Toro", "Pulse", "Fiorino"],
        "Ford": ["Ranger", "EcoSport", "Mustang", "Ford Ka", "Bronco Sport"],
        "Honda": ["Honda Civic", "Honda Accord", "Honda HR-V", "Honda CR-V", "Honda Fit"],
        "Hyundai": ["HB20", "Creta", "Tucson", "Santa Fe", "Elantra"],
        "Volkswagen": ["Gol", "Polo", "Virtus", "T-Cross", "Amarok"],
    }

    pergunta_marca = [
        {
            "type": "list",
            "message": "Escolha o modelo do carro:",
            "choices": list(marcas_modelos.keys()),
            "name": "marca",
        }
    ]

    resposta_marca = prompt(pergunta_marca)
    marca_selecionada = resposta_marca["marca"]

    pergunta_modelo = [
        {
            "type": "list",
            "message": f"Escolha a marca do carro {marca_selecionada}:",
            "choices": marcas_modelos[marca_selecionada],
            "name": "modelo",
        }
    ]

    resposta_modelo = prompt(pergunta_modelo)
    modelo_selecionado = resposta_modelo["modelo"]

    return marca_selecionada, modelo_selecionado

def valor_aluguel(dia, km):
    """Calcula o valor total do aluguel.

    Args:
        dia (int): Número de dias de aluguel.
        km (int): Número de quilômetros rodados.

    Returns:
        float: O valor total do aluguel.
    """
    valor_dia = 60
    valor_km = 0.15
    valor_total = (dia * valor_dia) + (km * valor_km)
    return valor_total

def ler_dias_km():
    """Solicita e retorna o número de dias e quilômetros, validando a entrada."""
    while True:
        try:
            dias = int(input(VERDE + "Quantos dias alugado?: "))
            km = int(input(VERDE + "Quantos quilômetros rodados?: " + RESET))
            return dias, km
        except ValueError:
            print(VERMELHO + "Por favor! Digite um número inteiro para dias e quilômetros." + RESET)

def mostra_nome_loja(loja):
    """Exibe o nome da loja formatado."""
    print(CIANO + f"\n{loja:=^40}\n" + RESET)

def mostrar_nome_cliente(nome):
    """Exibe uma mensagem de boas-vindas ao cliente."""
    print(CIANO + f"Seja bem vindo cliente {nome}." + RESET)
    print()

def mostrar_valor_aluguel(modelo, valor):
    """Exibe o modelo do carro alugado e o valor total do aluguel."""
    print(AMARELO_CLARO + f"\nCarro alugado {modelo[0]} modelo {modelo[1]}.\nFica no total de R$:{valor:.2f}.\n" + RESET)

# Programa principal
if __name__ == "__main__":
    init(autoreset=True)  # Inicializa colorama

    while True:
        nome_da_loja = nome_loja()
        mostra_nome_loja(nome_da_loja)

        nome_cliente = coletar_nome_cliente()
        mostrar_nome_cliente(nome_cliente)

        modelo_escolhido = escolher_marca_modelo()
        dias_aluguel, km_rodados = ler_dias_km()
        valor_total = valor_aluguel(dias_aluguel, km_rodados)
        mostrar_valor_aluguel(modelo_escolhido, valor_total)

        parar = input(Fore.BLUE + "Cadastrar novo cliente? (s/n): " + RESET).strip().lower()
        if parar == "n":
            break
        elif parar != "s":
            print(VERMELHO + "Por favor! Digite 's' para sim ou 'n' para não." + RESET)