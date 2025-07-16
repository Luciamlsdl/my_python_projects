"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
se elas podem ou não formar um triângulo. 
"""

#Este programa esta em sua forma simples 

reta1 = float(input("Primeiro seguimento: "))
reta2 = float(input("Segundo seguimento: "))
reta3 = float(input("Terceiro seguimento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os seguimentos acima forma um triângulo!")
else:
    print("Os seguimentos acima não formam um triângulo!")
    