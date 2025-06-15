"""
Faça um programa em python que abra uma pasta de arquivo MP3.
"""

# Este código esta em sua forma melhorada usando a biblioteca playsound (para arquivos locais)

import os
from playsound import playsound
import time

def tocar_pasta_de_musicas(pasta):
    """Toca todos os arquivos .mp3 encontrados em uma pasta.

    Args:
        pasta: O caminho para a pasta contendo os arquivos de música.
    """
    try:
        arquivos_na_pasta = os.listdir(pasta)
        arquivo_de_musica = [arquivo for arquivo in arquivos_na_pasta if arquivo.endswith(".mp3")]

        if not arquivo_de_musica:
            print(f"Nenhum arquivo .mp3 encontrado na pasta: {pasta}")
            return
        
        print(f"Tocando musica da pasta: \n{pasta}")
        for musica in arquivo_de_musica:
            caminho_completo = os.path.join(pasta, musica)
            print(f"Tocando: {musica}")

            try:
                playsound(caminho_completo)
                time.sleep(1) # Pausa entre músicas
            except Exception as e:
                print(f"Erro ao tocar '{pasta}': {e}")


    except FileNotFoundError:
        print(f"ERRO: Pasta não encontrada em '{pasta}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



# Programa principal

pasta_das_musica = '/home/lunix/Ambi_conda_python3/pasta21_Audio_MP3_Com_playsound/Nirvana - Inscesticide (1992) By Muro'
tocar_pasta_de_musicas(pasta_das_musica)
print("Fim da reprodução da pasta.")


"""
Explicação do código:

import os: 
Importa o módulo os, que fornece funções para interagir com o sistema operacional, 
como listar arquivos em um diretório (os.listdir) e construir caminhos de arquivos (os.path.join).

from playsound import playsound: 
Importa a função playsound da biblioteca.

import time: 
Importa o módulo time, que usamos aqui para adicionar uma pequena pausa entre a reprodução de 
cada música (isso é opcional, mas pode ser útil).

tocar_pasta_de_musicas(pasta):
Recebe o pasta (o caminho para a pasta com as músicas) como argumento.

Usa os.listdir(pasta) para obter uma lista de todos os arquivos e subdiretórios dentro da pasta.

Cria uma nova lista chamada arquivos_de_musica usando uma list comprehension. 
Ela itera sobre arquivos_na_pasta e inclui apenas os arquivos cujo nome termina com .mp3. 
Você pode adicionar outras extensões (como .wav, .ogg) se quiser tocar outros formatos.

Verifica se foram encontrados arquivos de música na pasta. 
Se não, imprime uma mensagem e retorna.

Imprime uma mensagem indicando qual pasta está sendo tocada.

Inicia um loop for que itera sobre cada arquivo de música na lista arquivos_de_musica.

Dentro do loop:
caminho_completo = os.path.join(pasta, musica): 
Constrói o caminho completo para o arquivo de música, combinando o caminho da pasta com o nome do arquivo. 
Isso é importante para que playsound possa encontrar o arquivo corretamente.

Imprime o nome da música que está sendo tocada.

Tenta tocar a música usando playsound(caminho_completo).

time.sleep(1): Adiciona uma pausa de 1 segundo após a reprodução de cada música (você pode ajustar esse valor ou removê-lo).

Se ocorrer algum erro ao tocar a música, o bloco except captura a exceção e imprime uma mensagem de erro.

Se a pasta especificada não for encontrada (FileNotFoundError) ou se ocorrer outro erro geral, 
o bloco except correspondente captura a exceção e imprime uma mensagem.

Exemplo de uso: 
Define o caminho para a pasta de músicas (você precisará substituir isso pelo caminho real da sua pasta) e 
chama a função tocar_pasta_de_musicas com esse caminho.
"""