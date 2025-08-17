import os
import shutil
import unicodedata

# Diretório base (ajuste se necessário)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapeamento de temas por palavras-chave
TEMAS = {
    "fundamentos": ["conversao", "validacao", "string", "basico"],
    "automacoes": ["selenium", "automacao", "renomear", "arquivo"],
    "interativos": ["menu", "inquirer", "interativo", "senha"],
}

def normalizar_nome(nome):
    # Remove acentos
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode()
    # Substitui espaços por underscore e deixa tudo minúsculo
    nome = nome.replace(" ", "_").lower()
    return nome

def identificar_tema(nome_arquivo):
    nome_lower = nome_arquivo.lower()
    for tema, palavras in TEMAS.items():
        if any(palavra in nome_lower for palavra in palavras):
            return tema
    return "outros"

def organizar_arquivos():
    arquivos = [f for f in os.listdir(BASE_DIR) if f.endswith(".py") and os.path.isfile(f)]
    for arquivo in arquivos:
        nome_normalizado = normalizar_nome(arquivo)
        tema = identificar_tema(nome_normalizado)
        destino = os.path.join(BASE_DIR, tema)
        os.makedirs(destino, exist_ok=True)
        novo_caminho = os.path.join(destino, nome_normalizado)
        print(f"Movendo {arquivo} → {tema}/{nome_normalizado}")
        shutil.move(os.path.join(BASE_DIR, arquivo), novo_caminho)

if __name__ == "__main__":
    organizar_arquivos()
    print("\n✅ Organização e renomeação concluídas!")
