"""
Faça um algoritmo que leia o preço de um produto
e mostre o seu novo preço, com 5 % de desconto. 
"""
# ESte programa está na  sua forma de função.

def ler_valor_produto():
    print()
    while True:
        try:
            valor_produto = float(input("Digite o valor do produto R$: "))
            if valor_produto <= 0:
                print("O valor do produto não pode ser valor negativo")
            else:
                return valor_produto
        except ValueError:
            print("Por favor! Digite um valor valido!")


def  dar_desconto(valor_produto):
    novo_valor = valor_produto - (valor_produto * 5 / 100)
    return novo_valor


def mostrar_valor(novo_valor):
    print(f"Com desconto de 5% o novo valor do produto é R$:{novo_valor:.2f}.")
    print()



#Programa principal
while True:
    valor_produto = ler_valor_produto()
    if valor_produto: # Garantir que um valor válido foi retornado
        novo_valor = dar_desconto(valor_produto)
        mostrar_valor(novo_valor)
        break
