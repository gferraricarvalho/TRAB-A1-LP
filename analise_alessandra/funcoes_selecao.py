import doctest as dt
import pandas as pd
def selecionar_colunas(dataframe, *nomes_colunas):
    """
    A função selecionar colunas é utilizada para selecionar colunas específicas de um Dataframe.

    Parameters
    ----------
    dataframe : DataFrame
        Dataframe onde estão as colunas que serão excluidas.
    *nomes_colunas : string
        Nome das colunas que serão excluidas do DataFrame.

    Returns
    -------
    df : DataFrame
        DataFrame sem as colunas indicadas.
        
    Exemplo
    -------
    >>> df = pd.DataFrame({"nome":["Alessandra", "Guilherme"], "Idade": [20,21]})
    >>> selecionar_colunas(df, "nome")
             nome
    0  Alessandra
    1   Guilherme

    """
    df = dataframe[[*nomes_colunas]]
    return df

def trocar_valor (dataframe, coluna, valores):
    """
    Função para alterar valores de uma coluna em um DataFrame.

    Parameters
    ----------
    dataframe : Dataframe
        Dataframe onde estão as colunas que serão alteradas.
    coluna : string
        Nome da coluna que será alterada.
    valores : Dicionário
        Dicionário onde a chave é o valor atual da célula e o valor é o novo valor que será inserido.

    Returns
    -------
    dataframe : Dataframe
        Dataframe com os valores alterados.

    Exemplo
    -------
    >>> df = pd.DataFrame({"nome":["Alessandra", "Guilherme"], "Idade": [20,21]})
    >>> trocar_valor(df, "Idade", {20:"Vinte", 21: "Vinte e um"})
             nome       Idade
    0  Alessandra       Vinte
    1   Guilherme  Vinte e um

    """
    dataframe[coluna] = dataframe[coluna].map(valores)
    return dataframe

def somar_valores_agrupado (dataframe, coluna, coluna_agrupamento):
    """
    Soma os valores de uma coluna em um dataframe

    Parameters
    ----------
    dataframe : Dataframe
        Dataframe onde está a coluna onde os valores serão somados.
    coluna : string
        Nome da coluna que será somada.
    coluna_agrupamento : string
        Nome da coluna pela qual a soma será agrupada.

    Returns
    -------
    df : Series
        Serie com a soma da coluna, onde o índice é o agrupamento.
        
    Exemplo
    -------
    >>> df = pd.DataFrame({"Idade":[20,21,20,21], "Itens comprados":[3,5,7,2]})
    >>> somar_valores_agrupado (df, "Itens comprados", "Idade")
    Idade
    20    10
    21     7
    Name: Itens comprados, dtype: int64

    """
    df = dataframe.groupby(coluna_agrupamento)[coluna].sum()
    return df

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)