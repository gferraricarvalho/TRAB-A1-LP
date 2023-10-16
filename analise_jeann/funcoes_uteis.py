import os
import doctest as dt
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
    df: DataFrame
    colunas: colunas que serão utilizadas

    Example:
    -----------
    >>> escolhe_colunas(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}), ["A", "B"])
       A  B
    0  1  4
    1  2  5
    2  3  6

    """

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")

    return df[colunas]


def agrupa_por_sum(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas somados
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)

    Example:
    -----------
    >>> agrupa_por_sum(pd.DataFrame({"A": [1, 1, 2], "B": [4, 5, 6], "C": [7, 8, 9]}), "A", ["B", "C"])
       B   C
    A       
    1  9  15
    2  6   9
    """

    if escolha_coluna not in df.columns:
        raise ValueError("A coluna base escolhida não se encontra como uma das colunas do dataframe.")

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")

    return df[[escolha_coluna] + colunas].groupby(escolha_coluna).agg(lambda x: sum(x))


def agrupa_por_cont(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas contados
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)

    Example:
    -----------
    >>> agrupa_por_cont(pd.DataFrame({"A": [1, 1, 2], "B": [4, 5, 6], "C": [7, 8, 9]}), "A", ["B", "C"])
       B  C
    A      
    1  2  2
    2  1  1
    """

    if escolha_coluna not in df.columns:
        raise ValueError("A coluna base escolhida não se encontra como uma das colunas do dataframe.")

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")

    return df[[escolha_coluna] + colunas].groupby(escolha_coluna).agg(lambda x: len(x))


def agrupa_por_proporcao(df: pd.DataFrame, escolha_coluna: str, colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas em proporção
    nesse agrupamento.

    Parameters:
    -----------
    df: dataframe.
    escolha_colunas: coluna base.
    colunas: lista de colunas padrão (indicadores ecológicos)

    Example:
    -----------
    >>> agrupa_por_proporcao(pd.DataFrame({"A": [1, 1, 2], "B": [4, 5, 6], "C": [7, 8, 9]}), "A", ["B", "C"])
         B    C
    A          
    1  4.5  7.5
    2  6.0  9.0

    """

    if escolha_coluna not in df.columns:
        raise ValueError("A coluna base escolhida não se encontra como uma das colunas do dataframe.")

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")

    return agrupa_por_sum(df, escolha_coluna, colunas) / agrupa_por_cont(df, escolha_coluna, colunas)


def salva_dataset(df: pd.DataFrame, name: str):
    # fazer docstring e doctest
    if not os.path.exists('analise_jeann/datasets'):
        os.makedirs('analise_jeann/datasets')
    df.to_csv(f"analise_jeann/datasets/{name}.csv", sep=';')
    df.to_markdown(f"analise_jeann/datasets/{name}.md")


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

    Example:
    -----------
    >>> dados_descritivos(pd.DataFrame({"A": [1, 1, 2], "B": [4, 5, 6], "C": [7, 8, 9]}), "A", ["B", "C"])
                         B          C
    MINIMO         6.00000   9.000000
    MAXIMO         9.00000  15.000000
    MEDIA          7.50000  12.000000
    MEDIANA        7.50000  12.000000
    DESVIO PADRAO  2.12132   4.242641
    """

    if escolha_coluna not in df.columns:
        raise ValueError("A coluna base escolhida não se encontra como uma das colunas do dataframe.")

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")

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

    if len([col for col in colunas if col in df.columns]) != len(colunas):
        raise ValueError("Alguma(s) das colunas fornecidas não estão no dataframe")
    
    dados = agrupa_por_sum(df, escolha_coluna, colunas)
    d = dados_descritivos(df, escolha_coluna, colunas) 
    
    for col in colunas:
        media = d.loc[d.index == "MEDIA"][col].iloc[0]
        print(f"{col}: {dados.loc[dados[col] > media].sort_values(col).index.to_list()}")


if __name__ == '__main__':
    dt.testmod(verbose=True)
