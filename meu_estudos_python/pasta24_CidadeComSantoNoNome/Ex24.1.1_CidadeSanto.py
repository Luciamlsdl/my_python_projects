"""
Crie um programa que leia  o nome de uma cidade e diga se ela começa pu não com o nome "Santo".
"""

# Este programa está em sua forma mais simples mais com uma nova função

print("\nVerificando se sua cidade começa com o nome santo")
cidade = input("Escreva o nome de sua cidade: ").strip().split()
if cidade[0].upper().startswith('SANTO'):
    print("Sua cidade começa com o nome santo!")
else:
    print("Sua cidade não começa com o nome santo!")


# temos a explicação desta função startswith()
"""
A função startswith() é um método de string que verifica se uma string começa com uma determinada substring (uma sequência de caracteres). 
Ela retorna um valor booleano:

True: se a string original começar com a substring especificada.
False: caso contrário.
Sintaxe:

A sintaxe básica da função é:

string.startswith(prefixo, inicio, fim)
Onde:

string: 
A string na qual você quer fazer a verificação.

prefixo:
A substring que você quer verificar se está no início da string. 
Este argumento é obrigatório. Pode ser uma string ou uma tupla de strings.

inicio (opcional): 
Um inteiro que especifica a posição inicial dentro da string a partir da qual a verificação deve começar. 

O padrão é 0 (o início da string).
fim (opcional): 
Um inteiro que especifica a posição final dentro da string onde a verificação deve parar. A substring verificada será da posição inicio até fim (exclusive).
Exemplos para entender melhor:

texto = "Olá, mundo!"

print(texto.startswith("Olá"))   # Saída: True
print(texto.startswith("Mundo")) # Saída: False
print(texto.startswith("olá"))   # Saída: False (case-sensitive)

# Verificando a partir de um índice específico
print(texto.startswith("mundo", 5)) # Saída: True (começa no índice 5)

# Verificando até um índice específico
print(texto.startswith("Olá", 0, 3)) # Saída: True (verifica "Olá")
print(texto.startswith("lá", 1, 3))  # Saída: True (verifica "lá")

# Verificando com uma tupla de prefixos
arquivos = ["imagem.png", "documento.pdf", "texto.txt"]
for arquivo in arquivos:
    if arquivo.startswith((".png", ".jpg")):
        print(f"{arquivo} é um arquivo de imagem.")
    elif arquivo.startswith(".doc"):
        print(f"{arquivo} é um documento.")
    else:
        print(f"{arquivo} é outro tipo de arquivo.")


Em quais momentos a função startswith() pode ser aplicada?

A função startswith() 
É extremamente útil em diversas situações onde você precisa verificar o início de uma string:

Análise de arquivos: 
Verificar a extensão de um arquivo para determinar seu tipo (como nos exemplos com .png, .jpg, .pdf).

Processamento de texto:
Verificar se uma linha de texto começa com um determinado comando ou marcador (por exemplo, em arquivos de log, arquivos de configuração).

Identificar títulos ou cabeçalhos em documentos.
Analisar URLs para verificar o protocolo (http://, https://, ftp://).

Validação de entrada de dados:
Verificar se um código postal começa com um determinado prefixo.
Verificar se um número de telefone segue um padrão inicial específico.

Implementação de funcionalidades de autocompletar: 
Sugerir palavras ou frases que começam com o que o usuário digitou.

Parsing de dados: 
Analisar linhas de dados onde o início da linha indica o tipo de informação contida.
"""