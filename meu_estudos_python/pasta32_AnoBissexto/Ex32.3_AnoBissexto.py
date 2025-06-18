"""
Faça um programa que leia um ano qualquer e mostre se ele e ano bissexto
"""

#Este programa está em sua forma de classe
#Mais com a importação da biblioteca datetime para analisar a data atual

from datetime import date


class AnalisadorDeAnoBissexto:
    def  __init__(self):
        self.ano = 0


    def apresentação(self):
        print("\nAnalisador de ano bissexto".upper())


    def ano_para_analise(self):
        while True:
            try:
                self.ano = int(input("Digite o ano para a analise ou 0 para o ano atual: "))
                return self.ano
            except ValueError:
                print("Por favor! Digite um ano válido")


    def analisa_ano(self):
        if self.ano == 0:
            self.ano = date.today().year
        if (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0):
            print(f"O ano de {self.ano} é um ano bissexto!")

        else:
            print(f"O ano de {self.ano} não é um ano bissexto!")


    def executador_de_programa(self):
        self.apresentação()
        while True:
            self.ano_para_analise()
            self.analisa_ano()
            while True:
                parar = str(input("Quer analisar outro ano (S=Sim ou N=Não): ")).strip().upper()
                if parar == "N":
                    print("Obrigado por utilizar nosso programa!")
                    return
                elif parar == "S":
                    break
                else:
                    print("Opção inválida! Use somente 'S' para sim ou 'N' para não!")


#Programa principal
if __name__ == "__main__":
    
    executador = AnalisadorDeAnoBissexto()
    executador.executador_de_programa()

        


