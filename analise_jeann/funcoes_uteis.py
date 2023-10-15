import os
import pandas as pd
import matplotlib.pyplot as plt

def decora_print(mensagem: str):
    """ Decora os prints de tela no decorrer do código

    Parameters:
    -----------
    mensagem: Texto que será exibido na tela.
    """
    print()
    print("#" * 120)
    print(mensagem)
    print("#" * 120)
    print()


def escolhe_colunas(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe apenas com as colunas que serão utilizadas

    Parameters:
    -----------
    mensagem: Texto que será exibido na tela.
    """
    return df[colunas]


def agrupa_por_sum(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas somados
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado), "TP_LOCALIZACAO" (Tipo de Localização da Escola), "TP_LOCALIZACAO_DIFERENCIADA" (Tipo de Localização Diferenciada da Escola) ou "TP_DEPENDÊNCIA" (Tipo de Dependência da Escola)')
    
    return df[[escolha_coluna] + colunas].groupby(escolha_coluna).agg(lambda x: sum(x))


def agrupa_por_cont(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas contados
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado), "TP_LOCALIZACAO" (Tipo de Localização da Escola), "TP_LOCALIZACAO_DIFERENCIADA" (Tipo de Localização Diferenciada da Escola) ou "TP_DEPENDÊNCIA" (Tipo de Dependência da Escola)')
    
    return df[[escolha_coluna] + colunas].groupby(escolha_coluna).agg(lambda x: len(x))


def agrupa_por_proporcao(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas em proporção
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região),  "SG_UF" (Sigla do Estado), "TP_LOCALIZACAO" (Tipo de Localização da Escola), "TP_LOCALIZACAO_DIFERENCIADA" (Tipo de Localização Diferenciada da Escola) ou "TP_DEPENDÊNCIA" (Tipo de Dependência da Escola)')
    
    return agrupa_por_sum(df, escolha_coluna, colunas) / agrupa_por_cont(df, escolha_coluna, colunas)


def salva_dataset(df: pd.DataFrame, name: str):
    # fazer docstring e doctest
    if not os.path.exists('analise_jeann/datasets'):
        os.makedirs('analise_jeann/datasets')
    df.to_csv(f"analise_jeann/datasets/{name}.csv", sep=';')


def salva_imagens(fig, name: str):
    # fazer docstring e doctest
    if not os.path.exists('analise_jeann/imagens'):
        os.makedirs('analise_jeann/imagens')
    fig.savefig(f"analise_jeann/imagens/{name}.png")


def dados_descritivos(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """ Dados descritivos gerais para o conjunto de dados em questão.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região) ou "SG_UF" (Sigla do Estado)')
    
    min = agrupa_por_sum(df, escolha_coluna, colunas).min() # mínimo dos valores
    max = agrupa_por_sum(df, escolha_coluna, colunas).max() # máximo dos valores
    mean = agrupa_por_sum(df, escolha_coluna, colunas).mean() # media dos valores
    median = agrupa_por_sum(df, escolha_coluna, colunas).median() # mediana dos valores
    std = agrupa_por_sum(df, escolha_coluna, colunas).std() # desvio padrão dos valores
    
    dados = pd.concat([min, max, mean, median, std], axis=1).T # cria um dataframe dos dados estatísticos feitos acima
    dados.index = ['MINIMO', 'MAXIMO', 'MEDIA', 'MEDIANA', 'DESVIO PADRAO']
    return dados


def acima_media(df: pd. DataFrame, escolha_coluna: str, colunas: list):
    """Retorna os locais (em Regiões ou em Estados) que estão acima do valor médio em cada indicador.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região) ou "SG_UF" (Sigla do Estado)')
    
    dados = agrupa_por_sum(df, escolha_coluna, colunas)
    d = dados_descritivos(df, escolha_coluna, colunas) 
    
    for col in colunas:
        media = d.loc[d.index == "MEDIA"][col].iloc[0]
        print(f"{col}: {dados.loc[dados[col] > media].sort_values(col).index.to_list()}")
