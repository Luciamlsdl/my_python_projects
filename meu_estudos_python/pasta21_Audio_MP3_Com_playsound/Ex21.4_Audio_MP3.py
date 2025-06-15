"""
Faça um programa em python que abra uma pasta de arquivo MP3.
"""

# Este código esta em sua forma melhorada usando a biblioteca playsound (para arquivos locais)

import os
import random
from playsound import playsound
from InquirerPy import inquirer

def tocar_musica(caminho_completo):
    """Toca um arquivo de música."""
    try:
        print(f"Tocando: {os.path.basename(caminho_completo)}")
        playsound(caminho_completo)
    except Exception as e:
        print(f"Erro ao tocar '{os.path.basename(caminho_completo)}': {e}")

def escolher_e_tocar_musica(pasta):
    """Lista as músicas e permite escolher tocar, adicionar à fila ou aleatório."""
    try:
        arquivos_na_pasta = sorted([f for f in os.listdir(pasta) if f.endswith(".mp3")])
        if not arquivos_na_pasta:
            print(f"Nenhum arquivo .mp3 encontrado em: {pasta}")
            return

        fila_de_reproducao = []

        while True:
            opcoes = ["Tocar agora", "Adicionar à fila", "Tocar aleatório", "Ver fila", "Sair"]
            if fila_de_reproducao:
                opcoes.insert(opcoes.index("Sair"), "Tocar fila")


            acao = inquirer.select(
                message="O que você gostaria de fazer?",
                choices=opcoes,
            ).execute()

            if acao == "Sair":
                break



            elif acao == "Tocar agora":
                escolha = inquirer.select(
                    message="Selecione uma música para tocar:",
                    choices=arquivos_na_pasta,
                ).execute()
                if escolha:
                    tocar_musica(os.path.join(pasta, escolha))



            elif acao == "Adicionar à fila":
                escolha = inquirer.select(
                    message="Selecione uma música para adicionar à fila:",
                    choices=arquivos_na_pasta,
                ).execute()
                if escolha:
                    fila_de_reproducao.append(os.path.join(pasta, escolha))
                    print(f"'{escolha}' adicionada à fila.")



            elif acao == "Tocar fila":
                if fila_de_reproducao:
                    print("Tocando a fila:")
                    for musica_na_fila in list(fila_de_reproducao): # Usar list() para evitar erros de modificação durante a iteração
                        tocar_musica(musica_na_fila)
                        fila_de_reproducao.pop(0) # Remove da fila após tocar
                    print("Fila de reprodução terminada.")
                else:
                    print("A fila de reprodução está vazia.")



            elif acao == "Tocar aleatório":
                if arquivos_na_pasta:
                    musica_aleatoria = random.choice(arquivos_na_pasta)
                    tocar_musica(os.path.join(pasta, musica_aleatoria))
                else:
                    print("Nenhuma música para tocar aleatoriamente.")



            elif acao == "Ver fila":
                if fila_de_reproducao:
                    print("Fila de reprodução:")
                    for i, musica in enumerate(fila_de_reproducao):
                        print(f"{i+1}. {os.path.basename(musica)}")
                else:
                    print("A fila de reprodução está vazia.")



    except FileNotFoundError:
        print(f"Erro: Pasta não encontrada.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



# Programa principal
pasta_das_musicas = '/home/lunix/Ambi_conda_python3/pasta21_Audio_MP3_Com_playsound/Nirvana - Inscesticide (1992) By Muro' 
escolher_e_tocar_musica(pasta_das_musicas)
print("Programa encerrado.")