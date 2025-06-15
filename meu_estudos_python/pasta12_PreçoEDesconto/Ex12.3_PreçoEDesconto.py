"""
Faça um algoritmo que leia o preço de um produto
e mostre o seu novo preço, com 5 % de desconto. 
"""
# ESte programa está na  sua forma de função.


class Produto:
    def __init__(self, valor):
        self.valor = valor


    def dar_desconto(self, percentual):
        self.valor -= (self.valor * percentual / 100)

    
    def __str__(self):
        return f"O valor do produto com desconto é R$:{self.valor:.2f}."


class GerenciadorDeProduto:
    @staticmethod
    def ler_valor_produto():
        while True:
            try:
                valor = float(input("Digite o valor do produto R$: "))
                if valor > 0:
                    return Produto(valor)
                else:
                    print("O valor do produto deve ser maior do que zero.")
            except ValueError:
                print("Por favor! Insira um valor válido.")

    @staticmethod
    def mostra_valor(produto):
        print(produto)


#Programa principal
if __name__ == "__main__":
    gerenciador = GerenciadorDeProduto()
    produto = gerenciador.ler_valor_produto()
    produto.dar_desconto(5) # Aplicando o desconto de 5%
    gerenciador.mostra_valor(produto)
    