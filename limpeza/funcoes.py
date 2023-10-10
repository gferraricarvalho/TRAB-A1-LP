import pandas as pd
import doctest as dt
from scipy import stats
import numpy as np

def colunas_indesejadas(arquivo_txt, dados):
    '''colunas_indesejadas remove as colunas indesejadasdo DataFrame fornecido, informadas utilizando 
    o arquivo txt

    _extended_summary_

    :param arquivo_txt: esse arquivo possui o nome das colunas que deseja remover.
    :type arquivo_txt: arquivo de texto (.txt)
    :param dados: É o DataFrame que se deseja remover colunas.
    :type dados: DataFrame
    :return: retorna uma atualização do DataFrame fornecido, sem as colunas que deveriam ser retiradas
    :rtype: DataFrame

        Example:
        1-
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> colunas_indesejadas('doc_coluna.txt', df)
           B  C
        0  4  7
        1  5  8
        2  6  9

        2- passando um txt vazio
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> colunas_indesejadas('doc_null.txt', df)
           A  B  C
        0  1  4  7
        1  2  5  8
        2  3  6  9


    '''
    with open(arquivo_txt, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        linhas = [linha.strip() for linha in linhas]
        for coluna in linhas:
            try:
                dados.drop(coluna, axis=1, inplace=True)
            except KeyError:
                print(f"{coluna} não encontrada!")
                continue
        return dados


def linhas_indesejadas(arquivo_txt, dados):
    '''linhas_indesejadas remove as linhas indesejadasdo DataFrame fornecido, informadas utilizando 
    o arquivo txt

    _extended_summary_

    :param arquivo_txt: esse arquivo possui o nome das linhas que deseja remover.
    :type arquivo_txt: arquivo de texto (.txt)
    :param dados: É o DataFrame que se deseja remover colunas.
    :type dados: DataFrame
    :return: retorna uma atualização do DataFrame fornecido, sem as colunas que deveriam ser retiradas
    :rtype: DataFrame

        Example:
        1-
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> linhas_indesejadas('doc_linha.txt', df)
           A  B  C
        0  1  4  7
        2  3  6  9

        2- passando um txt vazio
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> colunas_indesejadas('doc_null.txt', df)
           A  B  C
        0  1  4  7
        1  2  5  8
        2  3  6  9

    '''
    with open(arquivo_txt, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        linhas = [linha.strip() for linha in linhas]
        for linha in linhas:
            try:
                dados.drop(int(linha), axis=0, inplace=True)
            except KeyError:
                print(f"{linha} não encontrada!")
                continue
        return dados


def remove_duplicadas(dados):
    ''' Dropa linhas que estejam duplicadas no DataFrame.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3, 3], 'B': [4, 5, 6, 6], 'C': [7, 8, 9, 9]})
    >>> remove_duplicadas(df)
       A  B  C
    0  1  4  7
    1  2  5  8
    2  3  6  9
    '''
    dados = dados.drop_duplicates()
    return dados


def remove_NaN(dados):
    ''' Localiza colunas contendo excesso de valores vazios NaN's e as exclui do DataFrame.

    Example:
    >>> df = pd.DataFrame({'A': [1, np.nan, np.nan], 'B': [4, np.nan, 6], 'C': [7, 8, 9]})
    >>> remove_NaN(df)
       C
    0  7
    1  8
    2  9
    
    '''
    percentagem_nan = 0.8
    dados = dados.dropna(axis=1, thresh=dados.shape[0] * percentagem_nan)
    
    return dados


def padroniza_tipos(dados):
    ''' Localiza colunas com tipos mistos (mais de um tipo) - caracterizdas como tipo object - e padroniza, convertendo todos os valores nas colunas para string.
    
    Example:
    >>> df = pd.DataFrame({'A': [1, 'oi', 3], 'B': [4, 'hello', 'world'], 'C': [7, 8, 9]})
    >>> padroniza_tipos(df)
        A      B  C
    0   1      4  7
    1  oi  hello  8
    2   3  world  9
    '''
    colunas_object = dados.select_dtypes(include=['object']).columns
    dados[colunas_object] = dados[colunas_object].astype(str)
    
    return dados


def excluir_outliers(dataframe, coluna):
    """
    Função que exclui os outliers de uma coluna. Outliers são dados que se diferenciam muito do restante dos dados.
    Nesta função o padrão utilizado para detectar os outliers foi o zscore. Foi considerado outlier valores absolutos de zscore acima de 10.

    Parameters
    ----------
    dataframe : DataFrame
        Nome do dataframe onde está a coluna que você deseja fazer a remoção dos outliers.
    coluna : string
        Nome da coluna desejada.

    Returns
    -------
    df : DataFrame
        O retorno é um Dataframe com a coluna que você selecionou sem os outliers.

    """
    z_score = np.abs(stats.zscore(dataframe[coluna]))
    localizador = np.where(z_score>=10)
    df = dataframe.drop (localizador[0], inplace=True)
    
    return df

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)

