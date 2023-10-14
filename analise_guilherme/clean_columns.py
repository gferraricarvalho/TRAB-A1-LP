def filter_columns(dataframe, colunas):
    df_filtrado = dataframe[colunas]
    return df_filtrado

def sum_columns(dataframe):
    df_somado = dataframe.sum()
    return df_somado