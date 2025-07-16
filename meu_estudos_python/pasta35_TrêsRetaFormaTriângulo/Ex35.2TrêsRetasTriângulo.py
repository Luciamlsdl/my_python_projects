"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
se elas podem ou não formar um triângulo. 
"""

#Este programa esta em sua forma de função

def pode_formar_triangulo(r1, r2, r3):
    """
    Verifica se três comprimento de retas podem formar um triângulo.

    Args:
        r1 (float): Comprimento da primeira reta.
        r2 (float): Comprimento da segunda reta.
        r3 (float): Comprimento da terceira reta.

    Returns:
        bool: True se puderem forma um triângulo, False caso contrário.
    """
    # Verifica se todos os comprimentos são positivos 
    if r1 <= 0 or r2 <= 0 or r3 <= 0:
        print("Erro: Os comprimentos das retas devem ser maiores que zero.")
        return False
    
    # A]plica a desigualdade triangular
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        return True
    else:
        return False
    

    
# --- Programa principal ---
print("\n--- Verificador de TriÂngulo ---")

try:
    reta1 = float(input("Digite o comprimento da primeira reta: "))
    reta2 = float(input("Digite o comprimento da segunda reta: "))
    reta3 = float(input("Digite o comprimento da terceira reta: "))

    if pode_formar_triangulo(reta1, reta2, reta3):
        print(f"Com os comprimentos {reta1}, {reta2}, {reta3}, É POSSÍVEL formar um triângulo!")
    else:
        print(f"Com os comprimentos {reta1}, {reta2}, {reta3}, NÃO É possível formar um triângulo!")

except ValueError:
    print("Entra inválida. Por favor, digite apenas números.")


# Fala a verdade que código bonitinho hahahaha
# Código bem vi****dinho
