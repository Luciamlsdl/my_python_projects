import os
import shutil
import unicodedata

# Diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Temas e palavras-chave
TEMAS = {
    "fundamentos": ["conversao", "validacao", "string", "basico"],
    "automacoes": ["selenium", "automacao", "renomear", "arquivo"],
    "interativos": ["menu", "inquirer", "interativo", "senha"],
}

# Descrições para README
DESCRICOES = {
    "fundamentos": "Scripts básicos para aprender os fundamentos da linguagem Python, como conversões, validações e manipulação de strings.",
    "automacoes": "Automatizações usando bibliotecas como Selenium e manipulação de arquivos.",
    "interativos": "Scripts com interfaces interativas no terminal usando bibliotecas como InquirerPy.",
    "outros": "Scripts diversos que não se encaixam nas categorias principais.",
}

def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode()
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
        print(f"📦 Movendo {arquivo} → {tema}/{nome_normalizado}")
        shutil.move(os.path.join(BASE_DIR, arquivo), novo_caminho)

def gerar_readme_para_pasta(pasta):
    caminho = os.path.join(BASE_DIR, pasta)
    if not os.path.isdir(caminho):
        return

    arquivos = [f for f in os.listdir(caminho) if f.endswith(".py")]
    descricao = DESCRICOES.get(pasta, "Scripts relacionados ao tema " + pasta)

    conteudo = f"# 📁 {pasta.capitalize()}\n\n"
    conteudo += f"{descricao}\n\n"
    conteudo += "## 📜 Arquivos\n\n"

    for arquivo in arquivos:
        conteudo += f"- `{arquivo}`\n"

    with open(os.path.join(caminho, "README.md"), "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"📝 README gerado para: {pasta}/README.md")

def gerar_todos_readmes():
    for pasta in DESCRICOES.keys():
        gerar_readme_para_pasta(pasta)

if __name__ == "__main__":
    print("🚀 Iniciando organização do repositório...\n")
    organizar_arquivos()
    gerar_todos_readmes()
    print("\n✅ Tudo pronto! Seu repositório está organizado e documentado.")
