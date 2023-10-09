import pandas as pd
import doctest as dt

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
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> colunas_indesejadas('doc_coluna.txt', df)
           B  C
        0  4  7
        1  5  8
        2  6  9


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
    '''colunas_indesejadas remove as colunas indesejadasdo DataFrame fornecido, informadas utilizando 
    o arquivo txt

    _extended_summary_

    :param arquivo_txt: esse arquivo possui o nome das linhas que deseja remover.
    :type arquivo_txt: arquivo de texto (.txt)
    :param dados: É o DataFrame que se deseja remover colunas.
    :type dados: DataFrame
    :return: retorna uma atualização do DataFrame fornecido, sem as colunas que deveriam ser retiradas
    :rtype: DataFrame

        Example:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> linhas_indesejadas('doc_linha.txt', df)
           A  B  C
        0  1  4  7
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
    
def linhas_duplicadas(dados):
    dados = dados.drop_duplicates()
    return dados



if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)

