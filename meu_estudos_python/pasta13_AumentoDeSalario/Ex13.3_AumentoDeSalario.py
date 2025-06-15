"""
.Faça um algoritmo que leia o salário de um funcionário e mostre
o seu novo salário com 15% de aumento.
"""
# Este programa está na sua forma de class.


class AumentoDeSalario:
    def __init__(self, nome_funcionário, salario_funcionário):
        self.nome_funcionário = nome_funcionário
        self.salario_funcionário = salario_funcionário



    def calcula_novo_salario(self, percentual):
        self.salario_funcionário += (self.salario_funcionário * percentual / 100)
        


    def __str__(self):
        return f"O novo salário de {self.nome_funcionário} é R$:{self.salario_funcionário:.2f}."



class GerenciadorDeFuncionário:
    @staticmethod
    def ler_nome_funcionário():
        print()
        while True:
            nome_funcionário = str(input("Escreva o nome do funcionário: ")).strip().capitalize()
            if nome_funcionário and not nome_funcionário.isnumeric():
                return nome_funcionário
            else:
                print("Por favor! Digite um nome válido para o funcionário.") 



    @staticmethod
    def ler_salario_funcionário(nome_funcionário):
        while True:
            try:
                salario_funcionário = float(input(f"Digite o valor do salário do funcionário {nome_funcionário} R$: "))
                if salario_funcionário > 0:
                    return salario_funcionário
                else:
                    print("O valor do salário do funcionário deve ser maior que zero!")
            except ValueError:
                print("Por favor! Digite um valor válido!")



    @staticmethod
    def mostra_valor(funcionário):
        print(funcionário)



# programa principal
if __name__ == "__main__":
    gerenciador = GerenciadorDeFuncionário()

    nome_funcionário = gerenciador.ler_nome_funcionário()
    salario_funcionário = gerenciador.ler_salario_funcionário(nome_funcionário)

    funcionário = AumentoDeSalario(nome_funcionário, salario_funcionário)
    funcionário.calcula_novo_salario(15)
    gerenciador.mostra_valor(funcionário)
