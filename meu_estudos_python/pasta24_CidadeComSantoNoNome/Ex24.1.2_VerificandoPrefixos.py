"""
Este código é um verificador de prefixos e que podemos implantar em futuros códigos de análise de dados 
"""

# Verificando com uma tupla de prefixos
arquivos = ["imagem.png", "documento.pdf", "texto.txt"]
for arquivo in arquivos:
    if arquivo.startswith((".png", ".jpg")):
        print(f"{arquivo} é um arquivo de imagem.")
    elif arquivo.startswith(".doc"):
        print(f"{arquivo} é um documento.")
    else:
        print(f"{arquivo} é outro tipo de arquivo.")