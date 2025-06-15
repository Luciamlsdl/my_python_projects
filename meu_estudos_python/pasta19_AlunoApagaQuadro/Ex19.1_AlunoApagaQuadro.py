"""
Uma professora quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ela, lendo os nomes deles e escrevendo o
nome do escolhido na tela.
"""

# Este programa está em sua forma mais simples usando a importação do biblioteca random

import random

lista_aluno = []

print()
for c in range(1, 6):
    nome = str(input(f"Digite o nome do {c}° aluno: ")).strip().capitalize()
    lista_aluno.append(nome)
        
    
print(lista_aluno)

escolhido = random.choice(lista_aluno)
print(f"\nO aluno escolhido para apagar o quadro é {escolhido}.")
