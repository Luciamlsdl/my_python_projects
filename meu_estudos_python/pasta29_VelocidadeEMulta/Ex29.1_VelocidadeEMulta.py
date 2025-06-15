"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por km acima do limite de velocidade.  
"""

#Este código esta em sua forma simples 


print("\nMonitoramento de velocidade")
velocidade = float(input("Qual é a velocidade do carro?: "))
if velocidade > 80:
    print("Multado! Velocidade excedida de 80km/h")
    multa = (velocidade - 80) * 7
    print(f"A multa será de R$:{multa:.2f}")
else:
    print("Tenha um bom dia! E dirija com segurança!")
    