"""
Crie um programa que mostre quanto dinheiro você tem na carteira
e mostre quantos dollars da para comprar (Podendo fazer com outras moedas também)
"""
# Este programa está na sua forma de classe.
# E este programa já está atualizado para fazer pesquisa na web com a biblioteca selenium


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ConversorDeMoedaSelenium:
    def __init__(self, valor, moeda_destino):
        self.valor = valor
        self.moeda_destino = moeda_destino
        self.driver = webdriver.Chrome()


    def buscar_taxa(self):
        try:
            self.driver.get("https://www.google.com/")
            time.sleep(2)
            
            #Procurando a taxa de câmbio no google
            barra_pesquisa = self.driver.find_element(By.NAME, "q")
            barra_pesquisa.send_keys(f"{self.moeda_destino} para BRL")
            barra_pesquisa.send_keys(Keys.RETURN)
            time.sleep(2)

            #Procurando o valor  do cambio
            taxa = self.driver.find_element(By. XPATH, "//*[contains(text(),'1')]").text
            taxa_cambio = float(taxa.split()[3])
            return taxa_cambio

        except Exception as e:
            print("Erro ao buscar taxa de câmbio:", e)
            return 0
        finally:
            self.driver.quit()



    def converter(self):
        taxa_cambio = self.buscar_taxa()
        if taxa_cambio:
            valor_convertido = self.valor / taxa_cambio
            print(f"Com R$:{self.valor:.2f} em reais.\nVocê pode comprar {valor_convertido:.2f} {self.moeda_destino}")
        else:
            print("Não foi possível realizar a conversão")



# Programa principal
if __name__ == "__main__":
    valor = float(input("Digite o valor em reais: R$: "))
    moeda_destino = input("Digite o código da moeda de destino (ex: USD, EUR): ").upper()

    conversor = ConversorDeMoedaSelenium(valor, moeda_destino)
    conversor.converter()