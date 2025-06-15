"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma de classe.
# E este programa já está atualizado para fazer pesquisa na web com a biblioteca requests

import requests
from InquirerPy import prompt

class ConversorDeMoedasAPI:
    def __init__(self, valor, moeda_destino):
        self.valor = valor
        self.moeda_destino = moeda_destino
        self.url = f"https://economia.awesomeapi.com.br/json/last/{self.moeda_destino}BRL"
        self.taxa_cambio = 0


    def obter_taxa_cambio(self):
        try:
            resposta = requests.get(self.url)
            dados = resposta.json()
            if f"{self.moeda_destino}BRL" in dados:
                self.taxa_cambio = float(dados[f"{self.moeda_destino}BRL"]["bid"])
            else:
                print("Erro: Moeda não encontrada!")
                self.taxa_cambio = 0
        except Exception as e:
            print("Erro ao buscar taxas de câmbio:", e)
            self.taxa_cambio = 0
        return self.taxa_cambio
    

    def converter(self):
        if self.taxa_cambio:
            valor_convertido = self.valor * self.taxa_cambio
            print(f"Com {self.valor:.2f} em reais, você pode comprar {valor_convertido:.2f} {self.moeda_destino}.")
        else:
            print("Não foi possível realizar a conversão.")


if __name__ == "__main__":
    valor = float(input("Digite o valor em reais: R$: "))
    if valor <= 0:
        print("O valor em reais deve ser maior que zero.")
        exit()

    pergunta = [{
        "type": "list",
        "message": "Para qual moeda você deseja converter?",
        "choices": ["Dollar", "Euro"],
        "name": "moeda",
    }]

    resp = prompt(pergunta)
    moeda_map = {"Dollar": "USD", "Euro": "EUR"}
    moeda_destino = moeda_map[resp["moeda"]]

    conversor = ConversorDeMoedasAPI(valor, moeda_destino)
    conversor.obter_taxa_cambio()
    conversor.converter()