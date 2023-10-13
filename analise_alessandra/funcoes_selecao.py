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
    df : Dataframe
        Dataframe com a soma da coluna.

    """
    df = dataframe.groupby(coluna_agrupamento)[coluna].sum()
    return df