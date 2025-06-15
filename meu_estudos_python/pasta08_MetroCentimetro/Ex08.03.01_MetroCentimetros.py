class ConversorDeMedidas:
    def __init__(self, metros):
        self.metros = metros

    def calcular_conversões(self):
        return {
            "quilômetros": self.metros / 1000,
            "hectômetros": self.metros / 100,
            "decâmetros": self.metros / 10,
            "decímetros": self.metros * 10,
            "centímetros": self.metros * 100,
            "milímetros": self.metros * 1000
        }

    def mostrar_conversões(self):
        conversões = self.calcular_conversões()
        for unidade, valor in conversões.items():
            print(f"Valor em {unidade.capitalize()}: {valor:.2f}")


# Programa principal
try:
    num = float(input("Digite o valor em metros para ser convertido: "))
    if num < 0:
        print("Por favor, insira um valor positivo!")
    else:
        conversor = ConversorDeMedidas(num)
        conversor.mostrar_conversões()
except ValueError:
    print("Erro: Por favor, insira um número válido!")
