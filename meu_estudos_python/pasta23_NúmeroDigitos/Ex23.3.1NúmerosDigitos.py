"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
"""
# Este programa está na sua forma de classe com nova função e melhorias
# divmod() .Essa função retorna o quociente e o resto de uma divisão em uma única operação.

from time import sleep

class Números_Dígitos:
    """
    Classe responsável por analisar um número inteiro de 0 a 9999
    e extrair seus dígitos (unidade, dezena, centena e milhar).
    """
    def __init__(self, numero):
        """
        Inicializa a classe com o número a ser analisado.

        Args:
            numero (int): O número inteiro (0 a 9999).
        """
        self.numero = numero
        self.valor_dígitos = {}

    def calcula_dígitos(self):
        """
        Calcula os dígitos do número e os armazena no dicionário valor_dígitos.

        Returns:
            dict: Um dicionário contendo os dígitos do número
                  com as chaves 'unidade', 'dezena', 'centena' e 'milhar'.
        """
        numero = self.numero
        self.valor_dígitos = {}

        numero, self.valor_dígitos["unidade"] = divmod(numero, 10)
        numero, self.valor_dígitos["dezena"] = divmod(numero, 10)
        numero, self.valor_dígitos["centena"] = divmod(numero, 10)
        numero, self.valor_dígitos["milhar"] = divmod(numero, 10)

        return self.valor_dígitos

    def mostrar_resultado(self):
        """
        Exibe os dígitos do número analisado na tela.
        """
        sleep(2)
        print(f"\nO resultado da análise de dígitos do número {self.numero}:")
        sleep(1)
        print(f"Unidade = {self.valor_dígitos['unidade']}")
        sleep(1)
        if self.numero >= 10:
            print(f"Dezena = {self.valor_dígitos['dezena']}")
            sleep(1)
        if self.numero >= 100:
            print(f"Centena = {self.valor_dígitos['centena']}")
            sleep(1)
        if self.numero >= 1000:
            print(f"Milhar = {self.valor_dígitos['milhar']}")
            sleep(1)


class EntradaDeNumero:
    """
    Classe responsável por obter a entrada do número do usuário,
    garantindo que esteja dentro do intervalo válido (0 a 9999).
    """
    @staticmethod
    def ler_numero():
        """
        Solicita ao usuário que digite um número entre 0 e 9999.
        Repete a solicitação até que um valor válido seja inserido.

        Returns:
            int: O número inteiro digitado pelo usuário.
        """
        while True:
            try:
                numero = int(input("\nDigite um número de 0 a 9999 para ver seus dígitos: "))
                if 0 <= numero <= 9999:
                    return numero
                else:
                    print("O valor só pode ter 4 dígitos, de 0 a 9999!")

            except ValueError:
                print("Por favor, digite um valor inteiro válido para o número!")


if __name__ == "__main__":
    while True:
        numero = EntradaDeNumero.ler_numero()

        resultado = Números_Dígitos(numero)
        resultado.calcula_dígitos()
        resultado.mostrar_resultado()

        continuar = input("\nDeseja continuar? (S/N): ").strip().upper()
        if continuar != "S":
            break
