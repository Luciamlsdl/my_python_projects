"""
Escreva um programa que pergunte a quantidade de km percorrido por um carro
e a quantidades de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$:60 por dia e R$:0.15 por km rodado.
"""

# Este programa  está na  sua forma de classe

from InquirerPy import prompt


class AluguelDeCarro:
    def __init__(self, nome, dia, km, marca, modelo):
        self.nome = nome
        self.dia = dia
        self.km = km
        self.marca = marca
        self.modelo = modelo
        self.valor_total = 0


    def calcula_valor(self):
        valor_dia = 60
        valor_km = 0.15

        valor_total_dia = self.dia * valor_dia
        valor_total_km = self.km * valor_km

        self.valor_total = valor_total_dia + valor_total_km
        return self.valor_total
    

    def mostrar_valor(self):
        print(f"\nCliente {self.nome}, Aqui está seus dados de aluguel.")
        print(f"Marca do carro alugado {self.marca}.")
        print(f"Modelo do carro alugado {self.modelo}.")
        print(f"O valor total do aluguel é de R$:{self.valor_total:.2f}.")
        print()

       

class GerenciadorDeDados:
    @staticmethod    
    def ler_nome_cliente():
        while True:
            try:
                nome_cliente = str(input("\nEscreva o nome do cliente: ")).strip().capitalize()
                if nome_cliente and not nome_cliente.isnumeric():
                    return nome_cliente
                else:
                    print("Digite um nome válido para o cliente!")
            except ValueError:
                print("Por favor! Digite um valor válido!")


    @staticmethod
    def ler_dias_alugado():
        while True:
            try:
                dias_alugados = int(input("Quantos dias sera alugados o carro?: "))
                if dias_alugados > 1:
                    return dias_alugados
                else:
                    print("O valor de dias alugados não pode ser menor que um!")
            except ValueError:
                print("Por favor! Digite um valor válido!")


    @staticmethod
    def ler_quilometragem():
        while True:
            try:
                km_aluguel = int(input("Quantos quilômetros o carro vai rodar?: "))
                if km_aluguel > 1:
                    return km_aluguel
                else:
                    print("O valor de quilômetros rodados não pode ser menor que um!")
            except ValueError:
                print("Por favor! Digite um valor válido!")


    @staticmethod
    def escolher_marca_modelo():
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



#  Programa principal
while True:
    gerenciador = GerenciadorDeDados()
    nome = gerenciador.ler_nome_cliente()
    dia = gerenciador.ler_dias_alugado()
    km = gerenciador.ler_quilometragem()
    marca, modelo = gerenciador.escolher_marca_modelo()

    aluguel = AluguelDeCarro(nome, dia, km, marca, modelo)
    aluguel.calcula_valor()
    aluguel.mostrar_valor()

    while True:
        try:
            parar = str(input("Quer cadastrar novo cliente? (s/n): ")).strip().lower()[0]  
            if parar == 'n':
                break
        except ValueError:
            print("Por favor! Digite um valor válido entre 's' para continuar e 'n' para parar!")
