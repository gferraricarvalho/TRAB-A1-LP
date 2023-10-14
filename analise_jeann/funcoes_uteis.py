import pandas as pd

def atualiza_dataframe(df: pd.DataFrame, colunas: list):
    """Retorna um dataframe apenas com as colunas que serão utilizadas.
    """

    return df[colunas]

def agrupa_por(df: pd.DataFrame, escolha_coluna: str, tipo_colunas: list) -> pd.DataFrame:
    """Retorna um dataframe com os indíces agrupados por uma coluna base e os valores numéricos das colunas informativas somados
    nesse agrupamento.
    """

    return df[[escolha_coluna] + tipo_colunas].groupby(tipo_colunas).agg(lambda x: sum(x))