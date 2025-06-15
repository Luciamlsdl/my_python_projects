"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A" (ou "a") na frase
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
"""

# Este código está em sua forma mais simples

frase = str(input("\nEscreva uma frase qualquer para ser analisada: ")).strip()
frase_x = frase.upper()
print(f"Aletra A aparece {frase_x.count('A')} vezes na frase.")
print(f"A primeira letra A está na posição {(frase_x.find('A') + 1)}")
print(f"A ultima  letra A aparece na posição {(frase_x.rfind('A') + 1)}")
