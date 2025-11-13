"""
.Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar
e se é a hora exata de se alistar ou se já passou do tempo do alistamento.
.Seu programa também devera mostrar o tempo que falta ou que ja passou do prazo.    
"""

# Programa em sua forma classe

# Funções do código:
# Coleta = nome
# Coleta = data de nascimento
# Coleta = sexo
# Coleta = CPF
# Coleta = e-mail

# Validar as entrada
# Gerar os dados
# Criar um arquivo
# Enviar por e-mail


import re
import os
from datetime import date


class AlistamentoMilitar:
    def __init__(self):
        self.nome = ""
        self.data_nac = 0
        self.sexo = ""
        self.cpf = 0
        self.email = ""

# Inicializa do código----------------------------------------
    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")


    def tela_de_apresentacao(self):
        print("\n{:=^70}".format("Seja Bem vindo!".upper()))
        print("{:=^70}".format("Programa para analise de alistamento militar".upper()))

#--------------------------------------------------------------------------------------

# Ler e valida dados do usuário-------------------------------------------------

    def ler_nome(self):
        padrao_nome = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+([ '-][A-Za-zÀ-ÖØ-öø-ÿ]+)*$")

        while True:
            try:
                self.nome = str(input("Digite o seu nome inteiro: ")).strip().title()

                if not self.nome:
                    raise ValueError("O nome não pode star vazio. Tente novamente!")
                    

                if len(self.nome.split()) < 2:
                    raise ValueError("Digite seu nome completo (nome e sobrenome).")
                    

                if not padrao_nome.match(self.nome):
                    raise ValueError("O nome contem caracteres inválidos!")
                    
                return self.nome.title()
               
            except ValueError as erro:
                print(f"Erro: {erro}")


    def ler_data_nac(self):
        data_atual = date.today().year
        while True:
            try:
                entrada = input(f"Digite sua data de nascimento de 1900 a {data_atual}: ").strip()
                if not entrada:
                    raise ValueError("O campo não pode estar vazio!")
                
                ano = int(entrada)

                if not 1900 <= ano <= data_atual:
                    print(f"Por favor! A data de nascimento tem que estar no intervalo de 1900 a {data_atual}.")
                self.data_nac = ano
                return self.data_nac
             
            except ValueError:
                print("Por favor! Digite um valor válido para a data de nascimento!")


    def ler_sexo(self):
        while True:
            try: 
                entrada = str(input("Digite seu sexo (M/F): ")).strip().upper()

                if not entrada:
                    raise ValueError("O campo não pode estar vazio!")
                
                self.sexo = entrada[0]

                if self.sexo not in "MF":
                    raise ValueError("Por favor! Digite somente (M) para masculino ou (F) para feminino")
                
                else:
                    return self.sexo
                
            except ValueError as erro:
                print(f"Erro: {erro}")


    def ler_cpf(self):
        pass


    def ler_email(self):
        pass
#----------------------------------------------------------------------



    def carrasco(self):
        self.limpar_tela()
        self.tela_de_apresentacao()
        self.ler_nome()



if __name__ == "__main__":
    app = AlistamentoMilitar()
    app.carrasco()