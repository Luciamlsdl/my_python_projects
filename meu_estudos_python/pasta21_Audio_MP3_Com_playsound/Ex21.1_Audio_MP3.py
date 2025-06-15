"""
Faça um programa em python que abra um o audio de um arquivo MP3.
"""

# Este código esta em sua forma simples usando a biblioteca playsound (para arquivos locais)

from playsound import playsound

def tocar_musica(caminho_arquivo):
    """Toca um arquivo de áudio usando a biblioteca playsound.

    Args:
    caminho_arquivo: O caminho completo para o arquivo de áudio (ex: 'musica.mp3').
    """
     
    try:
        playsound(caminho_arquivo)
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado em '{caminho_arquivo}'")
    except Exception as e:
        print(f"Ocorreu um erro ao tocar a música: {e}" )

# Programa principal

caminho_da_musica = '/home/lunix/Ambi_conda_python3/pasta21_Audio_MP3_Com_playsound/Nirvana - Inscesticide (1992) By Muro/07 - Son Of A Gun.mp3'

tocar_musica(caminho_da_musica)
print("Música tocando.....")
