import pandas as pd

def decora_print(mensagem: str):
    """ Decora os prints de tela no decorrer do código
    """
    print()
    print("#" * 100)
    print(mensagem)
    print("#" * 100)
    print()


def escolhe_colunas(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe apenas com as colunas que serão utilizadas
    """
    return df[colunas]


def agrupa_por(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas somados
    nesse agrupamento.
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado), "NO_MUNICIPIO" (Nome do Município), "TP_LOCALIZACAO" (Tipo de Localização da Escola), "TP_LOCALIZACAO_DIFERENCIADA" (Tipo de Localização Diferenciada da Escola) ou "TP_DEPENDÊNCIA" (Tipo de Dependência da Escola)')
    
    return df[[escolha_coluna] + colunas].groupby(escolha_coluna).agg(lambda x: sum(x))


def dados_descritivos(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """ Dados descritivos gerais para o conjunto de dados em questão.
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado) ou "NO_MUNICIPIO" (Nome do Município)')
    
    min = agrupa_por(df, escolha_coluna, colunas).min() # mínimo dos valores
    max = agrupa_por(df, escolha_coluna, colunas).max() # máximo dos valores
    mean = agrupa_por(df, escolha_coluna, colunas).mean() # media dos valores
    median = agrupa_por(df, escolha_coluna, colunas).median() # mediana dos valores
    std = agrupa_por(df, escolha_coluna, colunas).std() # desvio padrão dos valores
    
    dados = pd.concat([min, max, mean, median, std], axis=1).T # cria um dataframe dos dados estatísticos feitos acima
    dados.index = ['MINIMO', 'MAXIMO', 'MEDIA', 'MEDIANA', 'DESVIO PADRAO']
    return dados


def acima_media(df: pd. DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna os locais (em Regiões ou em Estados) que estão acima do valor médio em cada indicador.
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado) ou "NO_MUNICIPIO" (Nome do Município)')
    
    dados = agrupa_por(df, escolha_coluna, colunas)
    d = dados_descritivos(df, escolha_coluna, colunas) 
    
    for col in colunas:
        media = d.loc[d.index == "MEDIA"][col].iloc[0]
        print(f"{col}: {dados.loc[dados[col] > media].sort_values(col).index.to_list()}")


def dist_freq(df: pd.DataFrame, colunas: list):
    """Retorna a Distribuição de Frequências de todas as colunas dadas de um dataframe fornecido
    """
    
    for col in colunas:
        print(df[col].value_counts().sort_index())
        print()


def calcula_proximos(df: pd.DataFrame, escolha_coluna: str) -> list:
    pass # a fazer...