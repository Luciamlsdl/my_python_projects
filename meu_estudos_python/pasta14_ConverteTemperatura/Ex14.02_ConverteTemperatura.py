"""
Escreva um programa que converta uma temperatura digitada em
graus célsius e converta em graus fahrenheit
"""

# Este programa está em sua forma de função

from InquirerPy import prompt

def ler_temperatura():
    while True:
        try:
            temperatura = float(input("\nDigite a temperatura a ser convertida Tº: "))
            return temperatura
        except ValueError:
            print("Por favor! Digite um valor válido!")


def escolher_temperatura(temp):
    conversor = [{
        "type": "list",
        "message": "Você quer converter para Fº fahrenheit ou Cº célsius?",
        "choices": ["Fahrenheit", "Célsius"],
        "name": "temperatura",
    }] 


    resultado = prompt(conversor)
    unidade_destino = resultado["temperatura"]

    if unidade_destino == "Fahrenheit":
        valor = ((9 * temp) / 5) + 32
        return valor,  unidade_destino
    
    elif unidade_destino == "Célsius":
        valor = 5 * ((temp - 32) / 9)
        return valor, unidade_destino


def mostrar_valor_convertido(valor_convertido, unidade_destino):
    print(f"O valor convertido para {unidade_destino} é = {valor_convertido:.2f}")


def deseja_continuar():
    while True:
        continuar = input("\nDeseja realizar outra conversão? (s/n): ").strip().lower()[0]
        if continuar and continuar in ['s', 'n']:
            return continuar[0]
        else:
            print("Entrada inválida! Por favor, digite 's' para sim ou 'n' para não.")



# Programa principal
while True:
    temperatura = ler_temperatura()
    valor_convertido, unidade_destino = escolher_temperatura(temperatura)
    mostrar_valor_convertido(valor_convertido, unidade_destino)

    continuar = deseja_continuar()
    if continuar == 'n':
        print("\nObrigado por usar o programa! Até logo!")
        break
