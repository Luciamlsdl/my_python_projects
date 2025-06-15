"""
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
# /1000  /100  /10   1   *10   *100    *1000
# km     hm    dam   m   dm    cm      mm


num = float(input("Digite um valor em metro para ser convertido em milímetros: "))

# Conversões
km = num / 1000  # Quilômetros
hm = num / 100   # Hectômetros
dam = num / 10   # Decâmetros
dm = num * 10    # Decímetros
cm = num * 100   # Centímetros
mm = num * 1000  # Milímetros


print(f"O valor {num} metros convertido para km = {km}.")
print(f"O valor {num} metros convertido para hm = {hm}.")
print(f"O valor {num} metros convertido para dam = {dam}.")
print(f"O valor {num} metros convertido para dm = {dm}.")
print(f"O valor {num} metros convertido para cm = {cm}.")
print(f"O valor {num} metros convertido para mm = {mm}.")


