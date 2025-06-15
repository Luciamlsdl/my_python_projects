class AumentoDeSalario:
    def __init__(self, nome_funcionário, salario_funcionário):
        self.nome_funcionário = nome_funcionário
        self.salario_funcionário = salario_funcionário

    def calcula_novo_salario(self, percentual=15):
        # Realiza o cálculo com o aumento
        self.salario_funcionário += (self.salario_funcionário * percentual / 100)

    def __str__(self):
        return f"O novo salário de {self.nome_funcionário} é R$:{self.salario_funcionário:.2f}."


class GerenciadorDeFuncionário:
    def __init__(self):
        self.funcionários = []

    def adicionar_funcionário(self, nome, salario):
        novo_funcionário = AumentoDeSalario(nome, salario)
        self.funcionários.append(novo_funcionário)
        return novo_funcionário

    @staticmethod
    def entrada_valida(mensagem, tipo):
        # Método genérico para validar entradas
        while True:
            try:
                entrada = tipo(input(mensagem))
                if tipo == float and entrada <= 0:
                    print("O valor deve ser maior que zero!")
                else:
                    return entrada
            except ValueError:
                print("Por favor, insira um valor válido.")

    def processar_funcionário(self):
        nome = self.entrada_valida("Digite o nome do funcionário: ", str).capitalize()
        salario = self.entrada_valida(f"Digite o salário de {nome} (R$): ", float)
        funcionário = self.adicionar_funcionário(nome, salario)
        return funcionário

    def mostrar_funcionários(self):
        print("\nLista de Funcionários:")
        for func in self.funcionários:
            print(func)


# Programa Principal
if __name__ == "__main__":
    gerenciador = GerenciadorDeFuncionário()

    while True:
        funcionário = gerenciador.processar_funcionário()
        funcionário.calcula_novo_salario()  # Adiciona o aumento de 15%
        gerenciador.mostrar_funcionários()

        continuar = input("\nDeseja adicionar outro funcionário? (s/n): ").strip().lower()
        if continuar != 's':
            print("Fim do programa. Até mais!")
            break
