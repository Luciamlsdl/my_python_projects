"""
Ordem de apresentação de trabalho de alunos.
Faça um programa que leia o nome de seus alunos e mostre a ordem sorteada. 
"""

# Este programa está em sua forma mais simples mais usando a biblioteca random com a função shuffle

from random import shuffle

lista = []

print('\033[4;32mOrdem de apresentação de trabalho\033[m')

for x in range(1, 5):
    nomes = str(input(f'\033[33mNome do {x}º aluno: ')).strip().capitalize()
    lista.append(nomes)
shuffle(lista)

print(f'A ordem de apresentação é\n'
      f'{lista}')