"""
Escreva um programa que converta uma temperatura digitada em
graus célsius e converta em graus fahrenheit
"""

# Este programa está em sua forma de classe


from InquirerPy import prompt

class ConversorDeTemperatura:
    def __init__(self, valor_temperatura):
        self.valor_temperatura = valor_temperatura


    def converter(self):
        pergunta = [
            {
                "type": "list",
                "message": "você quer converter para Fahrenheit ou Célsius?",
                "choices": ["Fahrenheit", "Célsius"],
                "name": "temperatura",
            }
        ]

        resposta = prompt(pergunta)
        unidade_destino = resposta["temperatura"]

        if unidade_destino == "Fahrenheit":
            valor = ((9 * self.valor_temperatura) / 5) + 32

        elif unidade_destino == "Célsius":
            valor = 5 * ((self.valor_temperatura - 32) / 9)

        else:
            valor = None

        return valor, unidade_destino
        

class GerenciadorDeConversor:
    @staticmethod
    def ler_temperatura():
        while True:
            try:
                temperatura = float(input("\nDigite a temperatura a ser convertida: °"))
                return temperatura
            except ValueError:
                print("Por favor! Digite uma valor valido!")

    
    @staticmethod
    def mostrar_valor_convertido(valor_convertido, unidade_destino):
        print(f"O valor convertido para {unidade_destino} é = {valor_convertido:.4f}")



    @staticmethod
    def deseja_continuar():
        while True:
            continuar = input("\nDeseja realizar outra conversão? (s/n): ").strip().lower()
            if continuar and continuar in ['s', 'n']:
                return continuar
            else:
                print("Entrada inválida! Por favor, digite 's' para sim ou 'n' para não!")

    
# Programa principal
if __name__ == "__main__":
    while True:
        temperatura = GerenciadorDeConversor.ler_temperatura()
        conversor = ConversorDeTemperatura(temperatura)

        valor_convertido, unidade_destino = conversor.converter()
        GerenciadorDeConversor.mostrar_valor_convertido(valor_convertido, unidade_destino)

        continuar = GerenciadorDeConversor.deseja_continuar()
        if continuar == 'n':
            print("\nObrigado por usar o programa! Até logo!")
            break