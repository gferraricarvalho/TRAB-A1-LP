import doctest as dt
import pandas as pd

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

    Exemplo
    -------
    >>> df = pd.DataFrame({"Numero": [13,22], "Nome": ["Lula", "Bolsonaro"]})
    >>> filter_columns(df, ["Numero"])
       Numero
    0      13
    1      22
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

    Exemplo
    -------
    >>> df = pd.DataFrame({"Aluno": ["Gui", "Ale"], "Faltas": [7,1]})
    >>> sum_columns(df)
    Aluno     GuiAle
    Faltas         8
    dtype: object
    """
    df_somado = dataframe.sum()
    return df_somado

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)