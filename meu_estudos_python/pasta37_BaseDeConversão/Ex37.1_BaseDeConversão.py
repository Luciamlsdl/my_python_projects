"""
Escreva um número que lei um número inteiro qualquer e peça para o usuário
escolher sua base de conversão.
1 = Para Binário
2 = Para Octal
3 = Para Hexadecimal
"""

#Este programa esta em seu formato simples

numero = int(input("Digite um número inteiro: "))
print("""
Escolha uma das bases de conversão:
[1] Conversão para BINÁRIO
[2] Conversão para OCTAL
[3] Conversão para HEXADECIMAL
""")

opção = int(input("Digite sua escolha de Opção desejada: "))

if opção == 1:
    print(f"{numero} Convertido para BINÁRIO = {bin(numero)[2:]}")


elif opção == 2:
    print(f"{numero} Convertido para OCTAL = {oct(numero)[2:]}")

elif opção == 3:
    print(f"{numero} Convertido para HEXADECIMAL = {hex(numero)[2:]}")

else:
    print("Opção inválida")
    