from time import sleep

def ler_numero():
    """
    Lê um número inteiro do usuário entre 0 e 9999.

    Returns:
        int: O número inteiro digitado pelo usuário (se válido).
    """
    while True:
        try:
            numero = int(input("\nDigite um número de 0 a 9999 para ver seu dígitos: "))
            if 0 <= numero <= 9999:
                return numero
            else:
                print("O valor só pode ter 4 dígitos que é de 0 a 9999!")

        except ValueError:
            print("Por favor! Digite um valor válido para o número!")


def calcula_digito(valor_numero):
    """
    Calcula os dígitos de um número inteiro.

    Args:
        valor_numero (int): O número inteiro a ser analisado.

    Returns:
        dict: Um dicionário contendo os dígitos unidade, dezena, centena e milhar.
    """
    valor_dígitos = {
                        "unidade": valor_numero // 1 % 10,
                        "dezena": valor_numero // 10 % 10,
                        "centena": valor_numero // 100 % 10,
                        "milhar": valor_numero // 1000 % 10
                    }
    return valor_dígitos


def mostrar_resultado(resultado, valor_numero):
    """
    Exibe os dígitos de um número formatado na tela.

    Args:
        resultado (dict): Um dicionário contendo os dígitos.
        valor_numero (int): O número original analisado.
    """
    sleep(2)
    print(f"\nO resultado da analise de dígitos do número {valor_numero}:")
    sleep(1)
    print(f"Unidade = {resultado['unidade']}")
    sleep(1)
    print(f"Dezena = {resultado['dezena']}")
    sleep(1)
    print(f"Centena = {resultado['centena']}")
    sleep(1)
    print(f"Milhar = {resultado['milhar']}")
    sleep(1)


# Programa principal
while True:
    valor_numero = ler_numero()
    resultado = calcula_digito(valor_numero)
    mostrar_resultado(resultado, valor_numero)

    pare = str(input("\nDigite S = sim para continuar e N = não para parar: ")).strip().upper()[0]
    if pare == "N":
        break
    elif pare != "S":
        print("Digite somente S ou N!")