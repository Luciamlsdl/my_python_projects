"""
Faça um programa em python que abra um o audio de um arquivo MP3.
"""

# Este código esta em sua forma simples usando a biblioteca pygame (para arquivos locais)

import pygame


def tocar_musica_pygame(caminho_arquivo):
    """Toca um arquivo de áudio usando a biblioteca pygame.mixer.

    Args:
        caminho_arquivo: O caminho completo para o arquivo de áudio.
    """

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()
        print("Música tocando.....")
    except pygame.error as e:
        print(f"Erro ao carregar ou tocar a música: {e}")


def pausar_musica_pygame():
    """Pausa a música que está tocando."""
    pygame.mixer.music.pause()
    print("Música pausada.")


def continuar_musica_pygame():
    """Continua a música pausada"""
    pygame.mixer.music.unpause()
    print("Música continuando.")


def parar_musica_pygame():
    """Para a música que esta tocando."""
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    print("Musica parada.")




# Programa principal
caminho_da_musica = '/home/lunix/Ambi_conda_python3/pasta21_Audio_MP3_Com_pygame/Nirvana - Inscesticide (1992) By Muro/07 - Son Of A Gun.mp3'
tocar_musica_pygame(caminho_da_musica)

input("Pressione Enter para pausar.....")
pausar_musica_pygame()

input("pressione Enter para continuar.....")
continuar_musica_pygame()

input("Pressione Enter para parar.....")
parar_musica_pygame()
