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
    try:
        df = dataframe[[*nomes_colunas]]
    except:
        print("Verifique se o nome do DataFrame ou da coluna está escrito da forma correta.") 
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
    #mapeia os valores indicados no dicionario e faz a troca atribuindo os novos valores no mesmo DataFrame
    try:
        dataframe[coluna] = dataframe[coluna].map(valores)
    except: 
        print("Verifique se os nomes estão corretos e o dicionário está abrangendo todas as possibilidades.")
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
    #primeiro faz o agrupamento, para depois selecionara a coluna e fazer a soma
    try:
        df = dataframe.groupby(coluna_agrupamento)[coluna].sum()
    except:
        print("Verifique se os nomes estão corretos.")
    return df

if __name__ == "__main__":
    dt.testmod()
    dt.testmod(verbose=True)