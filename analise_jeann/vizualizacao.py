import funcoes_uteis as fu
import pandas as pd
import matplotlib.pyplot as plt

def viz_simples(df: pd.DataFrame, escolha_coluna: str, colunas: list, dado_especifico=""):
    """Vizualização Simplificada (por Região ou Estado) da quantidade de cada indicador ecológico utilizado (Água, Energia, Esgoto ou Tratamento
    de Lixo) em um (ou vários) gráfico(s) de barras verticais.
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região) ou "SG_UF" (Sigla do Estado)')

    if dado_especifico not in [""] + colunas:
        raise ValueError(f'O dado_específico deve ser vazio (nenhum valor atribuído ou string vazia) ou deve ser alguma das colunas: {colunas}')
    
    df_tend = fu.agrupa_por(df, escolha_coluna, colunas)

    if dado_especifico == "":
        fig, ax = plt.subplots(4, 6, figsize=(20, 10))
        fig.subplots_adjust(hspace=0.5)
        
        cont = 0
        for i in range(0, 4):
            for j in range(0, 6):
                media = df_tend[colunas[cont]].mean()
                ax[i, j].bar(df_tend.index, df_tend[colunas[cont]])
                ax[i, j].set_title(f"{colunas[cont]}", fontsize=7)
                if escolha_coluna == 'SG_UF':
                    ax[i, j].tick_params(axis='x', labelrotation=90)
                ax[i, j].tick_params(axis='x', labelsize=4)
                ax[i, j].tick_params(axis='y', labelsize=5)
                ax[i, j].axhline(media, color='red', linestyle='-', label='Média')
                cont += 1
    
        plt.show()

    else:
        media = df_tend[dado_especifico].mean()
        plt.bar(df_tend.index, df_tend[dado_especifico])
        plt.title(f"{dado_especifico}")
        if escolha_coluna == 'SG_UF':
            plt.xticks(rotation=90)
        plt.axhline(media, color='red', linestyle='-', label='Média')
        plt.show()


def viz_dist_freq(df: pd.DataFrame, escolha_coluna: str, colunas: list, dado_especifico=""):
    """Vizualização da Distribuição de Frequências (por Região, Estado ou Município) da quantidade de cada indicador ecológico
    utilizado (Água, Energia, Esgoto ou Tratamento de Lixo) em um (ou vários) gráfico(s) de barras verticais.
    """

    if escolha_coluna not in ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região), "SG_UF" (Sigla do Estado) ou "NO_MUNICIPIO" (Nome do Município)')

    if dado_especifico not in [""] + colunas:
        raise ValueError(f'O dado_específico deve ser vazio (nenhum valor atribuído ou string vazia) ou deve ser alguma das colunas: {colunas}')
        
    df_freq = fu.agrupa_por(df, escolha_coluna, colunas)
    
    if dado_especifico == "":
        fig, ax = plt.subplots(4, 6, figsize=(40, 20))
        fig.subplots_adjust(hspace=0.5, wspace=0.5)
        
        cont = 0
        for i in range(0, 4):
            for j in range(0, 6):
                ax[i, j].hist(df_freq[colunas[cont]], bins=10, edgecolor='k')
                ax[i, j].set_title(f"{colunas[cont]}", fontsize=7)
                ax[i, j].set_xlabel("Quantidade", fontsize=7)
                ax[i, j].set_ylabel("Frequência", fontsize=7)
                ax[i, j].tick_params(axis='x', labelsize=4)
                ax[i, j].tick_params(axis='y', labelsize=4)
                cont += 1
    
        plt.show()

    else:
        df_freq = df_freq[dado_especifico].value_counts().sort_index()
        plt.hist(df_freq, bins=10, edgecolor='k')
        plt.xlabel("Quantidade")
        plt.ylabel("Frequência")
        plt.title(f"{dado_especifico}")
        plt.show()


def viz_correlativa(df: pd.DataFrame, escolha_coluna: str, colunas_agua: list, colunas_energia: list, colunas_esgoto: list, colunas_lixo: list):
    """Vizualização da Correlação do Tipo de Localização, Tipo de Localização Diferenciada ou Tipo de Dependência com a
    quantidade de cada indicador ecológico utilizado (Água, Energia, Esgoto ou Tratamento de Lixo) em um (ou vários) gráfico(s)
    de barras verticais empilhadas.
    """
    
    if escolha_coluna not in ['TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']:
        raise ValueError('A escolha_coluna deve ser "TP_LOCALIZACAO" (Tipo de Localização da Escola), "TP_LOCALIZACAO_DIFERENCIADA" (Tipo de Localização Diferenciada da Escola) ou "TP_DEPENDÊNCIA" (Tipo de Dependência da Escola)')

    if escolha_coluna == "TP_LOCALIZACAO":
        idx = {1: 'Urbana', 2: 'Rural'}
    elif escolha_coluna == "TP_LOCALIZACAO_DIFERENCIADA":
        idx = {0: 'Área não\nDiferenciada', 1: 'Assentamento', 2: 'Terra Indígena', 3: 'Remanescente\nde Quilombos'}
    elif escolha_coluna == "TP_DEPENDENCIA":
        idx = {1: "Federal", 2: "Estadual", 3: "Municipal", 4: "Privada"}
    
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))
    
    df_corr_agua = df[[escolha_coluna] + colunas_agua].groupby(escolha_coluna).agg(lambda x: sum(x))
    df_corr_agua = df_corr_agua.rename(index = idx)
    df_corr_agua.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[0,0])
    ax[0, 0].tick_params(axis='x', labelrotation=0)
    ax[0, 0].legend(loc='upper left', fontsize='small')
    
    df_corr_energia = df[[escolha_coluna] + colunas_energia].groupby(escolha_coluna).agg(lambda x: sum(x))
    df_corr_energia = df_corr_energia.rename(index = idx)
    df_corr_energia.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[0,1])
    ax[0, 1].tick_params(axis='x', labelrotation=0)
    ax[0, 1].legend(loc='upper left', fontsize='small')
    
    df_corr_esgoto = df[[escolha_coluna] + colunas_esgoto].groupby(escolha_coluna).agg(lambda x: sum(x))
    df_corr_esgoto = df_corr_esgoto.rename(index = idx)
    df_corr_esgoto.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[1,0])
    ax[1, 0].tick_params(axis='x', labelrotation=0)
    ax[1, 0].legend(loc='upper left', fontsize='small')
    
    df_corr_lixo = df[[escolha_coluna] + colunas_lixo].groupby(escolha_coluna).agg(lambda x: sum(x))
    df_corr_lixo = df_corr_lixo.rename(index = idx)
    df_corr_lixo.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[1,1])
    ax[1, 1].tick_params(axis='x', labelrotation=0)
    ax[1, 1].legend(loc='upper left', fontsize='small')

    plt.show()


def viz_clusterizada(df: pd.DataFrame, escolha_coluna: str, colunas: list):
    pass # a fazer...