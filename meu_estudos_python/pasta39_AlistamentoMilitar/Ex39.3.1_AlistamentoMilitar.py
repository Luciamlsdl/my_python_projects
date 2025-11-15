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

# Inicializa do código limpando a tela----------------------------------------
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
                entrada = input("Digite o seu nome inteiro: ").strip()

                if not entrada:
                    raise ValueError("O nome não pode estar vazio. Tente novamente!")

                if len(self.nome.split()) < 2:
                    raise ValueError("Digite seu nome completo (nome e sobrenome).")

                if not padrao_nome.match(self.nome):
                    raise ValueError("O nome contem caracteres inválidos!")
                
                self.nome = str(entrada)    
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
        while True:
            
            entrada = input("Digite o seu cpf EX.(12345678912): ").strip()

            if not entrada:
                print("O campo não pode estar vazio!")
                continue

            if not entrada.isdigit():
                print("Erro: O CPF deve conter apenas números!")
                continue

            if len(entrada) != 11:
                print("Erro: O CPFdeve ter exatamente 11 dígitos!")
                continue

            if entrada == entrada[0] * 11:
                print("Erro: CPF inválido!")
                continue
            
            soma = sum(int(entrada[i]) * (10 -i) for i in range(9))
            digito1 = (soma * 10) % 11
            digito2 = 0 if digito1 == 10 else digito2

            soma = sum(int(entrada[i]) * (11 - i) for i in range(10))
            digito2 = (soma * 10) % 11
            digito2 = 0 if digito2 == 10 else digito2

            if not (int(entrada[9]) == digito1 and int(entrada[10]) == digito2):
                print("Erro: CPF inválido pelos dígitos verificadores!")
                continue
            
            self.cpf = int(entrada)
            return self.cpf
    

    def ler_email(self):
        pass
#----------------------------------------------------------------------



    def carrasco(self):
        self.limpar_tela()
        self.tela_de_apresentacao()
        self.ler_nome()
        self.ler_data_nac()
        self.ler_sexo()
        self.ler_cpf()
        self.ler_email()



if __name__ == "__main__":
    app = AlistamentoMilitar()
    app.carrasco()