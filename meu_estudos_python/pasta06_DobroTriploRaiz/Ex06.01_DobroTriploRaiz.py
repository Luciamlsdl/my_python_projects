"""
Crie um algorítimo que lei um número e mostre o seu
dobro, triplo e raiz quadrada
"""

num = int(input("Digite um número para ver seu Dobro, triplo e Raiz quadrada: "))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

print(f"O dobro de {num} é igual a {dobro}")
print(f"O triplo de {num} é igual a {triplo}")
print(f"A raiz quadrada de {num} e igual a {raiz}")

