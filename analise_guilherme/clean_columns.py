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
    try: 
        if not isinstance(colunas, list):
            raise ValueError("O argumento 'colunas' deve ser uma lista de nomes de colunas.")
        
        elif not all(col in dataframe.columns for col in colunas):
            raise KeyError("Uma ou mais colunas não existem no dataframe.")
        
        df_filtrado = dataframe[colunas]
    except ValueError as e:
        print(f"Erro: {str(e)}")
        df_filtrado = None
    except KeyError as e:
        print(f"Erro: {str(e)}")
        df_filtrado = None
    except TypeError as e:
        print(f"Erro: O argumento 'dataframe' deve ser um DataFrame do pandas. Detalhes: {str(e)}")
        df_filtrado = None

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
    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("O argumento 'dataframe' deve ser um DataFrame do pandas.")
        
        df_somado = dataframe.sum()
        return df_somado
    except ValueError as ve:
        print(f"Erro de Valor: {str(ve)}")
        return None
    except TypeError as te:
        print(f"Erro de Tipo: {str(te)}")
        return None

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)