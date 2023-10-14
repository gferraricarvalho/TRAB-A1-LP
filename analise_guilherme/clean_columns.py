def filter_columns(dataframe, colunas):
    """
    A função filtra as colunas de um dataframe, 
    mantendo apenas as selecionadas pelo usuário.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe original para filtrar as colunas.
    colunas : list
        Lista com as colunas que deseja manter no dataframe.

    Returns
    -------
    df_filtrado : dataframe
        Dataframe filtrado com as colunas selecionadas.

    """
    df_filtrado = dataframe[colunas]
    return df_filtrado

def sum_columns(dataframe):
    """
    Somas as colunas do dataframe.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe escolhido para somar colunas.

    Returns
    -------
    df_somado : dataframe
        Dataframe que exibe a soma das colunas.

    """
    df_somado = dataframe.sum()
    return df_somado