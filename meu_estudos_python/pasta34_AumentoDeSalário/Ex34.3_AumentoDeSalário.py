"""
Escreva um programa que leia o salário de um funcionário e calcule o seu aumento.
Para salário superior a R$:1250.00 calcule um aumento de 10%.
Para salário inferior o igual o aumento é de 15%.
"""

#Este código está em formato de classe 

class AumentoDeSalário:
    def __init__(self):
        self.salario = 0.0
        self.novo_salario = 0.0

    
    def apresentação(self):
        print("\n---Programa para calcular aumento de salário---".upper())


    def ler_salario(self):
        while True:
            try:
                self.salario = float(input("\nDigite o valor do salário do funcionário R$: "))
                if self.salario > 0:
                    return
                else:
                    print("-->Salário não pode ser um valor menor que 0!")
            except ValueError:
                print("--->Por favor! Digite um valor válido para salário!")


    def aumento_de_salario(self):
        if self.salario <= 1250:
            self.novo_salario = self.salario + (self.salario * 15/ 100)
        else:
            self.novo_salario = self.salario + (self.salario * 10 / 100)

        return 
    

    def mostrar_aumento(self):
        print(f"Para o salário de R$:{self.salario:.2f}.\n"
              f"O seu novo salário é de R$:{self.novo_salario:.2f}.")
        

    def executador_de_programa(self):
        self.apresentação()
        self.ler_salario()
        self.aumento_de_salario()
        self.mostrar_aumento()



#Programa principal
executar = AumentoDeSalário()
executar.executador_de_programa()