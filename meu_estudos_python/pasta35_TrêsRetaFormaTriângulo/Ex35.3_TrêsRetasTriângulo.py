"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
se elas podem ou não formar um triângulo. 
"""

#Este programa esta em sua forma de classe ou poo (Programação Orientada a Objeto)

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        """
        Inicializar um objeto Triângulo com os comprimentos dos lados.

        Args:
            lado1 (float): Comprimento do primeiro lado.
            lado2 (float): Comprimento do segundo lado.
            lado3 (float): Comprimento do terceiro lado.
        """

        # Atribui os comprimentos aos atributos da instância
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def e_valido(self):
        """
        Verifica se os lados do triângulo podem formar um triângulo válido.

        Returns:
            bool: True se os lados formarem um triângulo, False caso contrário.
        """

        # Verifica se  todos os lados são positivos
        if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
            print("Erro: Os comprimentos dos lados devem ser maiores que zeo.")
            return False

        # Aplica a desigualdade triangular
        if (self.lado1 < self.lado2 + self.lado3 and
            self.lado2 < self.lado1 + self.lado3 and
            self.lado3 < self.lado1 + self.lado2):
            return True
        else:
            return False
        

    def __str__(self):
        """
        Retorna uma representação em string do objeto triangulo.
        Útil para printar o objeto diretamente.
        """

        return f"Triângulos com lados: {self.lado1}, {self.lado2}, {self.lado3}"
    

# --- Programa Principal (Usando a Classe) ---
print("\n--- Verificador de Triângulos (Orientado a Objetos) ---".upper())

try:
    l1 = float(input("Digite o comprimento do primeiro lado: "))
    l2 = float(input("Digite o comprimento do segundo lado: "))
    l3 = float(input("Digite o comprimento do terceiro lado: "))

    # Cria uma instância da classe Triangulo
    meu_triangulo = Triangulo(l1, l2, l3)

    # Usa o método e_valido() do objeto
    if meu_triangulo.e_valido():
        print(f"{meu_triangulo} \n- É POSSÍVEL formar um triângulo!")
    else:
        print(f"{meu_triangulo} \n- NÃO é possível formar um triângulo.")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")