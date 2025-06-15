"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.
"""

# Este programa está em sua forma mais simples

print("\nVamos analisar seu nome para ver se tem 'Silva' em seu nome!")
nome = str(input("Escreva o seu nome inteiro: ")).strip()
tem_silva = 'SILVA' in nome.upper().split()

if tem_silva == True:
    print("Voce tem silva no seu nome!")
else:
    print("Você não tem silva no nome!")

