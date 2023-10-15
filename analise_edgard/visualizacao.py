import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import doctest as dt
import numpy as np
 
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(diretorio_raiz)

import ler_arquivo as la

def localizacao(nome_arquivo:str) -> pd.DataFrame:
    """
    Esta função é projetada para receber o nome de um arquivo com a extensão ".csv" e, em seguida,
    procurá-lo na pasta anterior àquela onde o código está sendo executado. 
    Após localizar o arquivo, a função o converte em um DataFrame e o retorna.
    """
  
     # encontra a base de dados
    try:
        caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',nome_arquivo)
        dados = la.ler_arquivo_csv(caminho_arquivo)
        dados = pd.DataFrame(dados)
        return dados
    
    except FileNotFoundError:
        raise FileNotFoundError("O arquivo não pôde ser encontrado.")
    

def organiza(parametro_ordem: str,dados: pd.DataFrame, colunas_usadas:str) -> pd.DataFrame:
    """
    Esta função desempenha um papel importante na preparação dos dados. Ela recebe um parâmetro de ordenação,
    que é uma coluna específica do DataFrame. Em seguida, ela classifica o DataFrame com base nesse parâmetro, 
    reorganizando as linhas de acordo com os valores na coluna especificada.

    Além disso, a função também realiza uma seleção das colunas que serão usadas nos cálculos subsequentes, 
    retornando um novo DataFrame contendo apenas as colunas relevantes. 

    Parâmetros
    ----------
    parametro_ordem -> str, é uma das colunas que pertence ao DataFrame fornecido

    dados -> DataFrame utilisado para a analise de dados

    colunas_usadas ->str, é uma lista com as colunas que vão ser usadas

    Returns
    -------
    dados_ag-> DataFrame com os dados reorganizados conforme os parâmetros

    Exemplo:
    >>> dados = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'], 'Idade': [25, 30, 28, 35, 22]})
    >>> organiza('Nome',dados,['Nome','Idade'])
        Nome  Idade
    0  Alice     25
    1    Bob     30
    2  Carol     28
    3  David     35
    4    Eve     22
"""

     #escolhendo as colunas que serão utilizadas
    dados_utilizados = dados[colunas_usadas]

    #organizando de acordo com o parametro fornecido pelo usuario
    dados_ag = dados_utilizados.groupby(parametro_ordem).sum().reset_index()
    
    return dados_ag


def visualizacao_RG(dados_uf: pd.DataFrame, coluna_desejada: str, eixo_y: str, eixo_x: pd.DataFrame,
                     titulo: str,nome_imag:str,frequencia: list):
    """
    Essa função desempenha um papel importante na geração e armazenamento de gráficos a partir de um DataFrame
    com dados específicos escolhidos pelo usuário. Ela aceita os seguintes parâmetros:

    1 - dados_uf: Um DataFrame contendo os dados escolhidos pelo usuário.

    2 - coluna_desejada: A coluna que será usada como o eixo x no gráfico.

    3 - eixo_y: Uma variável que descreve o que está sendo contado ou medido no eixo y do gráfico.
   
    4 - titulo: Um título personalizado para o gráfico.
 
    5 - nome_imagem: O nome do arquivo de imagem que será gerado.

    O principal objetivo dessa função é criar um gráfico a partir dos dados fornecidos e salvá-lo em uma pasta 
    chamada "imagem" com o nome especificado pelo usuário.

    """

    try:
        quantidade = dados_uf[coluna_desejada]/np.array(frequencia)
        fig, ax = plt.subplots()
        quantidade.plot(kind='bar', ax=ax)
        ax.set_ylabel(eixo_y)
        ax.set_title(titulo)
        ax.set_xticks(range(len(eixo_x)))
        ax.set_xticklabels(eixo_x, rotation=90)
        ax.axhline(y=quantidade.mean(), color='black', linestyle='solid', label='Média')
        plt.show()
    
        # Salva o gráfico como uma imagem
        if not os.path.exists('imagens'):
            os.makedirs('imagens')
        fig.savefig(f"imagens/{nome_imag}.png")
    except KeyError:
        raise ValueError(f"A coluna '{coluna_desejada}' não foi encontrada no DataFrame 'dados_uf'.")

def calcular_estatisticas(dados: pd.DataFrame):
    """
    Essa função calcula todas as estatísticas de um DataFrame

    Prâmetros
    ---------
    dados -> DataFrame com os dados usados

    Returns
    -------
    estatisticas -> É um conjunto de dados obtidos do DataFrame

    Exemplo:
    -------
    
    >>> dados = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'], 'Idade': [25, 30, 28, 35, 22]})
    >>> calcular_estatisticas(dados)
               Idade
    count   5.000000
    mean   28.000000
    std     4.949747
    min    22.000000
    25%    25.000000
    50%    28.000000
    75%    30.000000
    max    35.000000

    """

    # Calcule estatísticas descritivas
    estatisticas = dados.describe()
    return estatisticas

def encontrar_max(df: pd.DataFrame, coluna_max: str ,coluna_desejada: str):
    """
    Essa função tem a finalidade de buscar o valor máximo em uma coluna chamada coluna_max dentro de um DataFrame. 
    Após localizar esse valor máximo,a função retorna o valor encontrado na mesma linha, 
    mas na coluna especificada como coluna_desejada.

    Parâmetros
    ----------
    df -> DataFrame com os dados usados

    coluna_max -> str com o nome da coluna onde vai ser buscado o valor máximo

    coluna_desejada -> str com o nome da coluna na qul vai ser retornado a o valor ou str que está na mesma
    posição do valor encontrado na coluna_max

    Return
    ------
    max_procurado -> É uma lista comos elementos que estão nas mesmas linhas que os valores máximos encontrados,
      que estão na coluna_desejada

    exemplo:
    --------

    >>> dados = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'], 'Idade': [25, 30, 28, 35, 22]})
    >>> encontrar_max(dados, 'Idade', 'Nome')
    ['David']
    """
    max_valor = df[coluna_max].max()
    municipios_max = df[df[coluna_max] == max_valor][coluna_desejada].tolist()
    return municipios_max

def freq_contagem(df:pd.DataFrame,coluna:str):
    """
    Essa função caucula a a frequência de cada item da coluna fornecida no DataFrame

    Exemplo:

    >>> df = pd.DataFrame({'Fruta': ['maçã', 'Banana', 'maçã', 'laranja', 'Banana', 'maçã']})
    >>> freq_contagem(df,'Fruta')
    Fruta
    Banana     2
    laranja    1
    maçã       3
    Name: count, dtype: int64
    """
    try:
        freq = df[coluna].value_counts().sort_index()
        return freq
    except KeyError:
        raise ValueError(f"{coluna} não pertence a {df}")

if __name__ == "__main__":
    dt.testmod(verbose=True)


