import requests
import unicodedata

# --- Funções Auxiliares ---
def valida_nome_cidade(nome):
    """
    Valida se o nome da cidade é válido (não vazio e contém apenas letras e espaços).
    Retorna True e None se válido, False e uma mensagem de erro caso contrário.
    """
    if not nome.strip():
        return False, "A entrada do nome da cidade não pode estar em branco!"

    for caractere in nome:
        if not (unicodedata.category(caractere).startswith('L') or caractere.isspace()):
            return False, "O nome da cidade deve conter apenas letras e espaços!"
        
    return True, None

def ler_nome_cidade():
    """
    Solicita ao usuário que digite o nome da cidade e valida a entrada.
    Continua pedindo até que uma entrada válida seja fornecida.
    """
    while True:
        nome_cidade_input = input("Escreva o nome completo de sua cidade: ").strip()
        valido, mensagem_erro = valida_nome_cidade(nome_cidade_input)

        if not valido:
            print(mensagem_erro)
            continue
        else:
            return nome_cidade_input




# Classe LocalizadorGeograficoIBGE
class LocalizadorGeograficoIBGE:
    # URLs base para as APIs do IBGE
    URL_BASE_LOCALIDADES = "https://servicodados.ibge.gov.br/api/v1/localidades" 
    # Tabela 6579: População residente - Censo Demográfico. Ano 2022. Variável 934: População residente.
    # N6: Município, N3: UF (Estado)
    URL_BASE_POPULACAO = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2022/variaveis/934?localidades="

    def __init__(self):
        self.municipios_cache = {} # Armazena {nome_cidade_lower: {id, nome, estado_sigla, estado_id}}
        self.estados_cache = {}    # Armazena {nome_estado_lower: {id, sigla}, sigla_lower: {id, nome}}
        print("Carregando dados iniciais do IBGE... Isso pode levar alguns segundos.")
        self._carregar_dados_iniciais()

    def _carregar_dados_iniciais(self):
        """
        Carrega todos os municípios e estados do IBGE para cache, otimizando buscas futuras.
        """
        try:
            # 1. Carrega Estados
            response_estados = requests.get(f"{self.URL_BASE_LOCALIDADES}/estados")
            response_estados.raise_for_status() # Levanta um erro para status de resposta HTTP ruins (4xx ou 5xx)
            estados_data = response_estados.json()
            for estado in estados_data:
                self.estados_cache[estado['nome'].lower()] = {'id': estado['id'], 'sigla': estado['sigla']}
                self.estados_cache[estado['sigla'].lower()] = {'id': estado['id'], 'nome': estado['nome']}

            # 2. Carrega Municípios
            response_municipios = requests.get(f"{self.URL_BASE_LOCALIDADES}/municipios")
            response_municipios.raise_for_status()
            municipios_data = response_municipios.json()
            for municipio in municipios_data:
                nome_municipio_lower = municipio['nome'].lower()
                self.municipios_cache[nome_municipio_lower] = {
                    'id': municipio['id'],
                    'nome': municipio['nome'], # Nome original da cidade
                    'estado_sigla': municipio['microrregiao']['mesorregiao']['UF']['sigla'],
                    'estado_id': municipio['microrregiao']['mesorregiao']['UF']['id']
                }
            print("Dados do IBGE carregados com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao carregar dados do IBGE: {e}")
            print("O programa pode não funcionar corretamente sem os dados.")
        except Exception as e:
            print(f"Erro inesperado ao carregar dados do IBGE: {e}")

    def obter_dados_cidade(self, nome_cidade):
        """
        Retorna um dicionário com nome, ID, sigla do estado e ID do estado para uma cidade,
        ou None se a cidade não for encontrada no cache.
        """
        return self.municipios_cache.get(nome_cidade.lower())

    def obter_populacao(self, tipo_localidade, id_localidade):
        """
        Obtém a população de um município (N6) ou estado (N3) dado seu ID do IBGE.
        Retorna a população como inteiro ou None em caso de erro/não encontrado.
        """
        if tipo_localidade == 'municipio':
            url = f"{self.URL_BASE_POPULACAO}N6[{id_localidade}]"
        elif tipo_localidade == 'estado':
            url = f"{self.URL_BASE_POPULACAO}N3[{id_localidade}]"
        else:
            return None # Tipo de localidade inválido

        try:
            response = requests.get(url)
            response.raise_for_status() # Lança exceção para erros HTTP
            data = response.json()
            
            # Navega na estrutura JSON da resposta da API de população
            if data and data[0]['resultados'] and data[0]['resultados'][0]['series'] and data[0]['resultados'][0]['series'][0]['serie']:
                # A chave do dicionário representa o ano, o valor a população. Pega o primeiro valor encontrado.
                populacao = list(data[0]['resultados'][0]['series'][0]['serie'].values())[0]
                return int(populacao) # Converte para inteiro
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao obter população: {e}")
            return None
        except (IndexError, KeyError, TypeError) as e: # Lida com erros de estrutura JSON inesperada
            print(f"Erro ao processar dados de população da API: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao obter população: {e}")
            return None
        

# --- Programa Principal ---
def main():
    print("\nBem-vindo ao Localizador Geográfico de População do IBGE!")
    
    # Inicializa o localizador. Ele carrega os dados do IBGE uma vez.
    localizador = LocalizadorGeograficoIBGE() 

    while True:
        print("\nEscolha uma opção:")
        print("1. Descobrir estado e população de uma cidade e seu estado")
        print("2. Sair")

        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == '1':
            nome_cidade_input = ler_nome_cidade()
            dados_cidade = localizador.obter_dados_cidade(nome_cidade_input)
            
            if dados_cidade:
                print(f"\n--- Dados para '{dados_cidade['nome']}' ---")
                print(f"Estado: {dados_cidade['estado_sigla']}")
                
                # Obtendo população da cidade
                populacao_mun = localizador.obter_populacao('municipio', dados_cidade['id'])
                if populacao_mun is not None:
                    print(f"População estimada da cidade: {populacao_mun:,d} habitantes.")
                else:
                    print("Não foi possível obter a população para esta cidade.")

                # Obtendo população do estado
                populacao_estado = localizador.obter_populacao('estado', dados_cidade['estado_id'])
                if populacao_estado is not None:
                    # Buscando o nome completo do estado para exibição
                    nome_estado_completo = None
                    for estado_info in localizador.estados_cache.values():
                        if estado_info.get('id') == dados_cidade['estado_id']:
                            nome_estado_completo = estado_info.get('nome')
                            break
                    
                    if nome_estado_completo:
                        print(f"População estimada do estado de {nome_estado_completo} ({dados_cidade['estado_sigla']}): {populacao_estado:,d} habitantes.")
                    else:
                        print(f"População estimada do estado de {dados_cidade['estado_sigla']}: {populacao_estado:,d} habitantes.") #Fallback
                else:
                    print(f"Não foi possível obter a população para o estado de {dados_cidade['estado_sigla']}.")
            else:
                print(f"Desculpe, não encontramos a cidade '{nome_cidade_input}' em nossos dados do IBGE.")
        elif opcao == '2':
            print("Obrigado por usar o Localizador Geográfico do IBGE. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, digite '1' ou '2'.")

if __name__ == "__main__":
    main()