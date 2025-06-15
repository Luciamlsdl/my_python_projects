# Verificando tipos básicos
numero_inteiro = 10
numero_decimal = 3.14
texto = "Olá"
lista = [1, 2, 3]
booleano = True

print(isinstance(numero_inteiro, int))     # Saída: True
print(isinstance(numero_decimal, float))   # Saída: True
print(isinstance(texto, str))             # Saída: True
print(isinstance(lista, list))           # Saída: True
print(isinstance(booleano, bool))         # Saída: True

# Verificando herança (instâncias de subclasses também são instâncias da superclasse)
class Animal:
    pass

class Cachorro(Animal):
    pass

meu_cachorro = Cachorro()

print(isinstance(meu_cachorro, Cachorro)) # Saída: True
print(isinstance(meu_cachorro, Animal))   # Saída: True (um cachorro É um animal)

# Verificando contra uma tupla de tipos
numero = 5
print(isinstance(numero, (int, float)))  # Saída: True (numero é um int)

valor = "abc"
print(isinstance(valor, (int, float)))   # Saída: False (valor não é int nem float)

# Verificando contra tipos definidos pelo usuário
class MinhaClasse:
    pass

objeto_minha_classe = MinhaClasse()
print(isinstance(objeto_minha_classe, MinhaClasse)) # Saída: True