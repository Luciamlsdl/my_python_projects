"""
.Escreva um programa que leia dois números inteiros e compare-os.
.Mostrando na tela uma mensagem:
-> O primeiro valor é o maior
-> O segundo valor é o maior
-> Não existe maior valor, os dois valores são iguais      
"""

#Código no seu formato classe

import os


class ComparDoisValores:
    def __init__(self):
        self.primeiro_valor = 0
        self.segundo_valor = 0


    def limpa_tela(self):
        os.system("cls" if os.name == "nt" else "clear")


    def apresentacao(self):
        print("{:=^70}".format("Programa de comparação entre dois valores"))


    def ler_primeiro_valor(self):
        while True:
            try:
                self.primeiro_valor = int(input("Digite o primeiro valor: "))
                return self.primeiro_valor
            except ValueError:
                print("Por favor! Digite um valor numérico válido!")


    def ler_segundo_valor(self):
        while True:
            try:
                self.segundo_valor = int(input("Digite o segundo valor: "))
                return self.segundo_valor
            except ValueError:
                print("Por favor! Digite um valor numérico válido!")
        


    def compar_valores(self):
        if self.primeiro_valor > self.segundo_valor:
            return f"O primeiro valor é o maior, número: {self.primeiro_valor}."
        
        elif self.segundo_valor > self.primeiro_valor:
            return f"O segundo valor é maior, número: {self.segundo_valor}. "

        else:
            return f"Os dois valores são iguais:\nnúmero-1 = {self.primeiro_valor}, número-2 = {self.segundo_valor}."
        

    def executor(self):
        self.limpa_tela()
        self.apresentacao()
        self.ler_primeiro_valor()
        self.ler_segundo_valor()
        print(self.compar_valores())


#Programa principal
if __name__ == "__main__":
    app = ComparDoisValores()
    app.executor()
