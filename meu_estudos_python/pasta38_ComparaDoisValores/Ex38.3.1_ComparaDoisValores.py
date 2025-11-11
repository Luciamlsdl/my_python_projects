"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato classe


"""
Programa: Comparação entre dois valores inteiros
Autor: Luciano Soares
Descrição:
    Lê dois números inteiros e mostra qual é o maior,
    ou se ambos são iguais.
"""

import os

class CompararDoisValores:
    def __init__(self):
        self.primeiro_valor = 0
        self.segundo_valor = 0

    def limpa_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def apresentacao(self):
        print("{:*^70}".format(" Programa de Comparação entre Dois Valores "))

    def ler_valor(self, mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("Por favor! Digite um valor numérico válido!")

    def compar_valores(self):
        if self.primeiro_valor > self.segundo_valor:
            return f"\nO primeiro valor ({self.primeiro_valor}) é o maior."
        elif self.segundo_valor > self.primeiro_valor:
            return f"\nO segundo valor ({self.segundo_valor}) é o maior."
        else:
            return f"\nOs dois valores são iguais: {self.primeiro_valor} = {self.segundo_valor}."

    def executor(self):
        self.limpa_tela()
        self.apresentacao()
        self.primeiro_valor = self.ler_valor("Digite o primeiro valor: ")
        self.segundo_valor = self.ler_valor("Digite o segundo valor: ")
        print(self.compar_valores())


# Programa principal
if __name__ == "__main__":
    app = CompararDoisValores()
    app.executor()
