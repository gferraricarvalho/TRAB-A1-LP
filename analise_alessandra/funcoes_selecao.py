def selecionar_colunas(dataframe, *nomes_colunas):
    df = dataframe[[*nomes_colunas]]
    return df

def trocar_valor (dataframe, coluna, valores):
    dataframe[coluna] = dataframe[coluna].map(valores)
    return dataframe

def somar_valores (dataframe, coluna):
    df = dataframe[coluna].sum()
    return df