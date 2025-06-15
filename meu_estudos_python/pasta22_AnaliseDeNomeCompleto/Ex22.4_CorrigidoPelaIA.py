from time import sleep
import unicodedata
from colorama import init, Fore, Style

Verde = Fore.GREEN
Vermelho = Fore.RED
Azul = Fore.BLUE
Amarelo = Fore.LIGHTYELLOW_EX
Ciano = Fore.CYAN
Reset = Style.RESET_ALL

init(autoreset=True)

class AnaliseDeNome:
    def __init__(self, nome):
        self.nome = nome
        self.decorador = f"{Vermelho}-{Reset}" * 60

    def exibir_decorador(self):
        print(self.decorador)

    def nome_maiúsculo(self):
        self.exibir_decorador()
        print(f"{Amarelo}O seu nome em letras maiúsculas:{Reset}.")
        print(f"{Verde}{self.nome.upper()}{Reset}.")
        self.exibir_decorador()
        sleep(1)  # Reduzi o tempo para não ser tão longo em testes
        print()

    def nome_minúsculo(self):
        self.exibir_decorador()
        print(f"{Amarelo}O seu nome em letras minúsculas:{Reset}")
        print(f"{Verde}{self.nome.lower()}{Reset}")
        self.exibir_decorador()
        sleep(1)
        print()

    def quantidade_de_letras(self):
        self.exibir_decorador()
        print(f"{Amarelo}O seu nome tem ao todo {len(self.nome) - self.nome.count(' ')} letras.{Reset}")
        self.exibir_decorador()
        sleep(1)
        print()

    def quantidade_letras_primeiro_nome(self):
        self.exibir_decorador()
        primeiro_nome_fim = self.nome.find(' ')
        if primeiro_nome_fim != -1:
            print(f"{Amarelo}O seu primeiro nome tem ao todo {primeiro_nome_fim} letras.{Reset}")
        else:
            print(f"{Amarelo}O seu nome tem apenas um nome.{Reset}")
        self.exibir_decorador()
        print()

class AnalisaEntradaDeNome:
    @staticmethod
    def valida_nome(nome):
        if not nome.strip():
            return False, f"{Vermelho}A entrada de nome não pode estar em branco!{Reset}"

        for caractere in nome:
            categoria = unicodedata.category(caractere)
            if not (categoria.startswith('L') or caractere.isspace() or caractere == '-' or caractere == "'"):
                return False, f"{Vermelho}O nome deve conter apenas letras, espaços, hífens e apóstrofos!{Reset}"
            if caractere.isspace() and nome.count('  ') > 0:
                return False, f"{Vermelho}O nome não deve conter múltiplos espaços consecutivos!{Reset}"
        return True, None

    @staticmethod
    def ler_nome():
        while True:
            nome = str(input(f"{Azul}\n--> Escreva seu nome completo: {Reset}")).strip().capitalize()
            print()
            sleep(1)
            valido, mensagem_erro = AnalisaEntradaDeNome.valida_nome(nome)

            if not valido:
                print(f"{mensagem_erro}")
                continue
            else:
                return nome

class Apresentação:
    @staticmethod
    def apresentar_boas_vindas():
        print(Ciano + "\n{:*^70}".format(" Seja bem-vindo ao analisador de nome! ".upper()) + Reset)
        sleep(2)
        print()

# Programa principal
if __name__ == "__main__":
    Apresentação.apresentar_boas_vindas()
    while True:
        valor_nome = AnalisaEntradaDeNome.ler_nome()
        analise = AnaliseDeNome(valor_nome)
        analise.nome_maiúsculo()
        analise.nome_minúsculo()
        analise.quantidade_de_letras()
        analise.quantidade_letras_primeiro_nome()

        while True:
            parar = str(input(f"{Ciano}Quer analisar outro nome (S = Sim ou N = Não): {Reset}")).strip().upper()[0]
            if parar == "N":
                break
            elif parar == "S":
                break
            else:
                print(f"{Vermelho}Opção inválida. Digite 'S' para Sim ou 'N' para Não.{Reset}")
        if parar == "N":
            break