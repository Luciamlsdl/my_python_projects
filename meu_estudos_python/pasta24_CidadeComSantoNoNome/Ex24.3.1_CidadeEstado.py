"""Código para mostrar o estado em que se encontra uma cidade usando a API do IBGE"""

import requests
import unicodedata

# --- Funções Auxiliares (sem alterações, mantidas para contexto) ---
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


### Classe `LocalizadorGeograficoIBGE` (com melhorias no tratamento de dados)

class LocalizadorGeograficoIBGE:
    URL_BASE_LOCALIDADES = "https://servicodados.ibge.gov.br/api/v1/localidades"
    URL_BASE_POPULACAO = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2025/variaveis/934?localidades="

    def __init__(self):
        self.municipios_cache = {}
        self.estados_cache = {}
        print("Carregando dados iniciais do IBGE... Isso pode levar alguns segundos.")
        self._carregar_dados_iniciais()

    def _carregar_dados_iniciais(self):
        """
        Carrega todos os municípios e estados do IBGE para cache, otimizando buscas futuras.
        Adicionadas verificações para garantir que os dados JSON não são None ou vazios.
        """
        try:
            # 1. Carrega Estados
            response_estados = requests.get(f"{self.URL_BASE_LOCALIDADES}/estados")
            response_estados.raise_for_status()
            estados_data = response_estados.json()
            
            # --- Adição importante: Verificação antes de iterar ---
            if not estados_data: # Se a lista de estados for vazia ou None
                print("Aviso: A API de estados do IBGE retornou dados vazios.")
                return # Interrompe a carga se os dados base não vierem

            for estado in estados_data:
                # --- Adição importante: Verificação de chaves antes de acessar ---
                if 'nome' in estado and 'id' in estado and 'sigla' in estado:
                    self.estados_cache[estado['nome'].lower()] = {'id': estado['id'], 'sigla': estado['sigla']}
                    self.estados_cache[estado['sigla'].lower()] = {'id': estado['id'], 'nome': estado['nome']}
                else:
                    print(f"Aviso: Formato inesperado para um estado: {estado}")


            # 2. Carrega Municípios
            response_municipios = requests.get(f"{self.URL_BASE_LOCALIDADES}/municipios")
            response_municipios.raise_for_status()
            municipios_data = response_municipios.json()

            # --- Adição importante: Verificação antes de iterar ---
            if not municipios_data: # Se a lista de municípios for vazia ou None
                print("Aviso: A API de municípios do IBGE retornou dados vazios.")
                return # Interrompe a carga se os dados base não vierem

            for municipio in municipios_data:
                # --- Adição importante: Verificação de chaves antes de acessar ---
                # Acesso aninhado requer cuidado redobrado
                if ('nome' in municipio and 
                    'id' in municipio and 
                    'microrregiao' in municipio and 
                    'mesorregiao' in municipio['microrregiao'] and 
                    'UF' in municipio['microrregiao']['mesorregiao'] and 
                    'sigla' in municipio['microrregiao']['mesorregiao']['UF'] and
                    'id' in municipio['microrregiao']['mesorregiao']['UF']):

                    nome_municipio_lower = municipio['nome'].lower()
                    self.municipios_cache[nome_municipio_lower] = {
                        'id': municipio['id'],
                        'nome': municipio['nome'],
                        'estado_sigla': municipio['microrregiao']['mesorregiao']['UF']['sigla'],
                        'estado_id': municipio['microrregiao']['mesorregiao']['UF']['id']
                    }
                else:
                    print(f"Aviso: Formato inesperado para um município: {municipio}")
                    
            print("Dados do IBGE carregados com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao carregar dados do IBGE: {e}")
            print("Por favor, verifique sua conexão com a internet ou se a API do IBGE está disponível.")
        except Exception as e:
            print(f"Erro inesperado ao carregar dados do IBGE: {e}")
            print("Verifique a estrutura dos dados retornados pela API.")

    def obter_dados_cidade(self, nome_cidade):
        return self.municipios_cache.get(nome_cidade.lower())

    def obter_populacao(self, tipo_localidade, id_localidade):
        if tipo_localidade == 'municipio':
            url = f"{self.URL_BASE_POPULACAO}N6[{id_localidade}]"
        elif tipo_localidade == 'estado':
            url = f"{self.URL_BASE_POPULACAO}N3[{id_localidade}]"
        else:
            return None

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data and isinstance(data, list) and data[0]['resultados'] and data[0]['resultados'][0]['series'] and data[0]['resultados'][0]['series'][0]['serie']:
                populacao = list(data[0]['resultados'][0]['series'][0]['serie'].values())[0]
                return int(populacao)
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao obter população: {e}")
            return None
        except (IndexError, KeyError, TypeError) as e:
            print(f"Erro ao processar dados de população da API (estrutura inesperada): {e}")
            print(f"Dados recebidos (primeiros 100 caracteres): {str(data)[:100]}...") # Ajuda a depurar
            return None
        except Exception as e:
            print(f"Erro inesperado ao obter população: {e}")
            return None
        

# --- Programa Principal ---
def main():
    print("\nBem-vindo ao Localizador Geográfico de População do IBGE!")
    
    localizador = LocalizadorGeograficoIBGE() 

    # Se o cache de municípios estiver vazio após a tentativa de carga, o programa não funcionará.
    if not localizador.municipios_cache:
        print("\nNão foi possível carregar os dados das cidades. Encerrando o programa.")
        return

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
                
                populacao_mun = localizador.obter_populacao('municipio', dados_cidade['id'])
                if populacao_mun is not None:
                    print(f"População estimada da cidade: {populacao_mun:,d} habitantes.")
                else:
                    print("Não foi possível obter a população para esta cidade.")

                populacao_estado = localizador.obter_populacao('estado', dados_cidade['estado_id'])
                if populacao_estado is not None:
                    nome_estado_completo = None
                    for estado_info in localizador.estados_cache.values():
                        if estado_info.get('id') == dados_cidade['estado_id']:
                            nome_estado_completo = estado_info.get('nome')
                            break
                    
                    if nome_estado_completo:
                        print(f"População estimada do estado de {nome_estado_completo} ({dados_cidade['estado_sigla']}): {populacao_estado:,d} habitantes.")
                    else:
                        print(f"População estimada do estado de {dados_cidade['estado_sigla']}: {populacao_estado:,d} habitantes.")
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