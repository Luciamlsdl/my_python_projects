"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
"""
# Este programa está na sua forma de classe

from time import sleep

class Números_Dígitos:
    def __init__(self, numero):
        self.numero = numero
        self.valor_dígitos = 0
        



    def calcula_dígitos(self):
        self.valor_dígitos = {
                        "unidade": self.numero // 1 % 10,
                        "dezena": self.numero // 10 % 10,
                        "centena": self.numero // 100 % 10,
                        "milhar": self.numero // 1000 % 10
                    }
        return self.valor_dígitos



    def mostrar_resultado(self):
        sleep(2)
        print(f"\nO resultado da analise de dígitos do número {self.numero}:")
        sleep(1)
        print(f"Unidade = {self.valor_dígitos["unidade"]}")
        sleep(1)
        print(f"Dezena = {self.valor_dígitos["dezena"]}")
        sleep(1)
        print(f"Centena = {self.valor_dígitos["centena"]}")
        sleep(1)
        print(f"Milhar = {self.valor_dígitos["milhar"]}")
        sleep(1)



class EntradaDeNumero:
    @staticmethod
    def ler_numero():
        while True:
            try:
                numero = int(input("\nDigite um número de 0 a 9999 para ver seu dígitos: "))
                if numero >= 0 and numero <= 9999:
                    return numero
                else:    
                    print("O valor só pode ter 4 dígitos que é de 0 a 9999!")
                
            except ValueError:
                print("Por favor! Digite um valor válido para o número!")    



if __name__ == "__main__":
    while True:
        numero = EntradaDeNumero.ler_numero()

        resultado = Números_Dígitos(numero)
        resultado.calcula_dígitos()
        resultado.mostrar_resultado()


        pare = str(input("\nDigite S = sim para continuar e N = não para parar: ")).strip().upper()[0]
        if pare == "N":
            break
        elif pare == "S":
            continue
        else:
            print("Digite somente S para sim ou N para não!")