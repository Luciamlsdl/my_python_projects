"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""

# Este programa vai estar na sua forma de classe


class Tabuada:
    """
    Classe para calcular a tabuada de um número inteiro.
    """
    def __init__(self, numero):
        self.numero = numero

    
    def calcular_tabuada(self):
        """
        Método para calcular e exibir a tabuada do número armazenado na instância.
        """
        print(f"\nTabuada do {self.numero}:")
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} x {i} = {resultado}")

    
class ler_valor:
    """
    Classe para ler um número inteiro do usuário.
    """
    @staticmethod
    def ler_valor():
        """
        Método para ler um número inteiro do usuário.
        """
        try:
            numero = int(input("Digite um número inteiro para ver sua tabuada: "))
        except ValueError:
            print("ERRO: Digite um valor válido!")
            return None
        return numero
    
    @staticmethod
    def main():
    
        numero = ler_valor.ler_valor()
        if numero is not None:
            tabuada = Tabuada(numero)
            tabuada.calcular_tabuada()


if __name__ == "__main__":
    while True:
        ler_valor.main()
        
        continuar = input("Deseja calcular a tabuada de outro número? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar o programa!")
            break
                




