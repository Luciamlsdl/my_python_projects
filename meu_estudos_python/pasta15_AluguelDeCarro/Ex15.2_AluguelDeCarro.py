"""
Escreva um programa que pergunte a quantidade de km percorrido por um carro
e a quantidades de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$:60 por dia e R$:0.15 por km rodado.
"""

# Este programa  está na  sua forma de função

from InquirerPy import prompt
from colorama import init, Fore, Back, Style


def nome_loja():
    loja = "ALUGANDO SONHOS"
    return loja


def coletar_nome_cliente():
    while True:
        try:
            nome = str(input(Fore.LIGHTBLUE_EX +"Qual é o  nome do cliente?: " + Style.RESET_ALL)).strip().capitalize()
            if nome and not nome.isnumeric():
                return nome
        except ValueError:
            print(Fore.RED + "por favor! Digite um nome válido." + Style.RESET_ALL)
            

def escolher_marca_modelo():
    marca = [
        {
            "type": "list",
            "message": "Escolhe qual é modelo do carro?",
            "choices": ["Chevrolet", "Fiat", "Ford", "Honda", "Hyundai", "Volkswagen"],
            "name": "tipo",
        }

    ]
    

    resposta = prompt(marca)
    lista_marca = resposta["tipo"]


    if lista_marca == "Chevrolet":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["Tracker", "Ônix ","Cruze", "S10", "Equinox"],
                "name": "modelo",
            }
        ]
        

    elif lista_marca == "Fiat":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["Argo", "Cronos", "Toro", "Pulse", "Fiorino"],
                "name": "modelo", 
            }
        ]


    elif lista_marca == "Ford":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["Ranger", "EcoSport", "Mustang", "Ford Ka", "Bronco Sport"],
                "name": "modelo", 
            }
        ]


    elif lista_marca == "Honda":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["Honda Civic", "Honda Accord", "Honda HR-V", "Honda CR-V", "Honda Fit"],
                "name": "modelo", 
            }
        ]


    elif lista_marca == "Hyundai":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["HB20", "Creta", "Tucson", "Santa Fe", "Elantra"],
                "name": "modelo", 
            }
        ]


    elif lista_marca == "Volkswagen":
        modelo = [
            {
                "type": "list",
                "message": "Escolher qual é o marca do carro?",
                "choices": ["Gol", "Polo", "Virtus", "T-Cross", "Amarok"],
                "name": "modelo", 
            }
        ]

    nova_resposta = prompt(modelo)
    valor_modelo = nova_resposta["modelo"]


    return lista_marca, valor_modelo
   


def valor_aluguel(dia, km):
    valor_dia = 60
    valor_km = 0.15

    valor_total_dias = dia * valor_dia
    valor_total_km = km * valor_km

    valor_total = valor_total_dias + valor_total_km
    return valor_total


def ler_dias_km():
    while True:
        try:
            dias = int(input(Fore.GREEN + "Quantos dias alugado?: "))
            km = int(input("Quantos quilômetros rodados?: " + Style.RESET_ALL))    
            return dias, km
        except ValueError:
            print("Por favor! Digite um valor válido!")


def mostra_nome_loja(loja):
    print(Fore.CYAN + f"\n{loja:=^40}\n"+ Style.RESET_ALL)


def mostrar_nome_cliente(nome):
    print(Fore.CYAN+f"Seja bem vindo cliente {nome}."+Style.RESET_ALL)
    print()


def mostrar_valor_aluguel(modelo, valor):
    print(Fore.LIGHTYELLOW_EX+f"\nCarro alugado {modelo[0]} modelo {modelo[1]}.\nFica no total de R$:{valor}.\n"+Style.RESET_ALL)


# Programa principal
while True:
    nome = nome_loja()
    mostra_nome_loja(nome) 

    nome_client = coletar_nome_cliente()
    mostrar_nome_cliente(nome_client)


    modelo = escolher_marca_modelo()
    dias, km = ler_dias_km()
    valor = valor_aluguel(dias, km)
    mostrar_valor_aluguel(modelo, valor)

    try:
        parar = str(input(Fore.BLUE+"Cadastrar novo cliente? (s/n): "+Style.RESET_ALL)).strip().lower()
        if parar == "n":
            break
    except ValueError:
        print(Fore.RED+"Pro favor! Digite um valor válido!"+Style.RESET_ALL)