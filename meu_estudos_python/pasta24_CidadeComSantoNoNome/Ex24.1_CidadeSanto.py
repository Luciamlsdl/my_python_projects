"""
Crie um programa que leia  o nome de uma cidade e diga se ela começa pu não com o nome "Santo".
"""

# Este programa está em sua forma mais simples

print("\nVerificando se sua cidade começa com o nome santo")
cidade = str(input("Escreva o nome de sua cidade: ")).strip().split()
cit = cidade[0].upper()== 'SANTO'
if cit == True:
    print("Sua cidade começa com o nome santo!")
else:
    print("Sua cidade não começa com o nome santo!")

