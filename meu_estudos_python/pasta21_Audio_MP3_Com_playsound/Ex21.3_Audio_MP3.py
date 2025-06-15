"""
Faça um programa em python que abra uma pasta de arquivo MP3.
"""

# Este código esta em sua forma melhorada usando a biblioteca playsound (para arquivos locais)

import os
from playsound import playsound
from InquirerPy import inquirer

def escolher_e_tocar_musica(pasta):
    """Lista os arquivos .mp3 em uma pasta e permite ao usuário escolher um para tocar.
    """

    try:
        arquivos_na_pasta = os.listdir(pasta)
        arquivos_de_musica = sorted([arquivo for arquivo in arquivos_na_pasta if arquivo.endswith(".mp3")])

        if not arquivos_de_musica:
            print(f"Nenhum arquivo .mp3 encontrado na pasta: {pasta}")
            return

        escolha = inquirer.select(
            message="\nSelecione uma música para tocar:",
            choices=arquivos_de_musica,
        ).execute()

        if escolha:
            caminho_completo = os.path.join(pasta, escolha)
            print(f"Tocando: {escolha}")
            try:
                playsound(caminho_completo)
            except Exception as e:
                print(f"Erro ao tocar '{escolha}': {e}")

    except FileNotFoundError:
        print(f"Erro: Pasta não encontrada em '{pasta}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



# Programa principal:
pasta_das_musicas = '/home/lunix/Ambi_conda_python3/pasta21_Audio_MP3_Com_playsound/Nirvana - Inscesticide (1992) By Muro' 
escolher_e_tocar_musica(pasta_das_musicas)
print("Fim da execução.")
