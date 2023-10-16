import funcoes_uteis as fu
import pandas as pd
import matplotlib.pyplot as plt

def viz_simples(df: pd.DataFrame, escolha_coluna: str, colunas: list, quant_graf_lin: int, quant_graf_col: int, name: str):
    """Vizualização Simplificada (por Região ou Estado) da quantidade do indicador ecológico fornecido em um (ou vários) gráfico(s) de barras verticais.

    Parameters:
    -----------
    df: DataFrame
    colunas: colunas 
    quant_graf_lin: quantidade de subplots de gráficos por linha
    quant_graf_col: quantidade de subplots de gráficos por colunas 
    name: nome da imagem que será salvado (sem o .png)
    """
    
    if escolha_coluna not in ['NO_REGIAO', 'SG_UF']:
        raise ValueError('A escolha_coluna deve ser "NO_REGIAO" (Nome da Região) ou "SG_UF" (Sigla do Estado)')
    
    if quant_graf_lin * quant_graf_col != len(colunas):
        raise ValueError('A quantidade de linhas (quant_graf_lin) e a quantidade de colunas (quant_graf_col) devem satisfazer uma quantidade total de suplots igual ao número de colunas fornecidas')

    df = fu.agrupa_por_sum(df, escolha_coluna, colunas)

    fig, ax = plt.subplots(quant_graf_lin, quant_graf_col, figsize=(20, 10))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    
    if quant_graf_lin == quant_graf_col == 1:
        media = df[colunas[0]].mean()
        ax.bar(df.index, df[colunas[0]])
        ax.set_title(f"{colunas[0]}", fontsize=15)
        if escolha_coluna == 'SG_UF':
            ax.tick_params(axis='x', labelrotation=90) # detalhes de formatação
        if escolha_coluna == 'NO_REGIAO':
            ax.tick_params(axis='x', labelrotation=60)
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=15)
        ax.axhline(media, color='red', linestyle='-', label='Média')

    elif quant_graf_lin == 1:
        for j in range(0, quant_graf_col):
            media = df[colunas[j]].mean()
            ax[j].bar(df.index, df[colunas[j]])
            ax[j].set_title(f"{colunas[j]}", fontsize=15)
            if escolha_coluna == 'SG_UF':
                ax[j].tick_params(axis='x', labelrotation=90) # detalhes de formatação
            if escolha_coluna == 'NO_REGIAO':
                ax[j].tick_params(axis='x', labelrotation=60)
            ax[j].tick_params(axis='x', labelsize=10)
            ax[j].tick_params(axis='y', labelsize=12)
            ax[j].axhline(media, color='red', linestyle='-', label='Média')
    else:
        cont = 0
        for i in range(0, quant_graf_lin):
            for j in range(0, quant_graf_col):
                media = df[colunas[cont]].mean()
                ax[i, j].bar(df.index, df[colunas[cont]])
                ax[i, j].set_title(f"{colunas[cont]}", fontsize=15)
                if escolha_coluna == 'SG_UF':
                    ax[i, j].tick_params(axis='x', labelrotation=90) # detalhes de formatação
                if escolha_coluna == 'NO_REGIAO':
                    ax[i, j].tick_params(axis='x', labelrotation=60)
                ax[i, j].tick_params(axis='x', labelsize=10)
                ax[i, j].tick_params(axis='y', labelsize=12)
                ax[i, j].axhline(media, color='red', linestyle='-', label='Média')
                cont += 1

    fu.salva_imagens(fig, name)


def viz_correlativa(df: pd.DataFrame, escolha_coluna: str, colunas_agua: list, colunas_energia: list, colunas_esgoto: list, colunas_lixo: list, name: str):
    """Vizualização da Correlação do Tipo de Localização, Tipo de Localização Diferenciada ou Tipo de Dependência com a
    quantidade de cada indicador ecológico utilizado (Água, Energia, Esgoto ou Tratamento de Lixo) em um (ou vários) gráfico(s)
    de barras verticais empilhadas.

    Parameters:
    -----------
    df: DataFrame
    escolha_coluna: coluna base (TP_LOCALIZACAO, TP_LOCALIZACAO_DIFERENCIADA ou TP_DEPENDENCIA)
    colunas_agua: colunas de agua
    colunas_energia: colunas de energia
    colunas_esgoto: colunas de esgoto
    colunas_lixo: colunas de lixo
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
    fig.subplots_adjust(hspace=0.5)
    
    df_corr_agua = fu.agrupa_por_proporcao(df, escolha_coluna, colunas_agua) # proporcao da quantidade de escolas no quesito agua
    df_corr_agua.index = idx
    df_corr_agua.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[0,0])
    ax[0, 0].tick_params(axis='x', labelrotation=0)
    ax[0, 0].legend(loc='upper left', fontsize='xx-small')
    
    df_corr_energia = fu.agrupa_por_proporcao(df, escolha_coluna, colunas_energia) # proporcao da quantidade de escolas no quesito energia
    df_corr_energia.index = idx
    df_corr_energia.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[0,1])
    ax[0, 1].tick_params(axis='x', labelrotation=0)
    ax[0, 1].legend(loc='upper left', fontsize='xx-small')
    
    df_corr_esgoto = fu.agrupa_por_proporcao(df, escolha_coluna, colunas_esgoto) # proporcao da quantidade de escolas no quesito esgoto
    df_corr_esgoto.index = idx
    df_corr_esgoto.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[1,0])
    ax[1, 0].tick_params(axis='x', labelrotation=0)
    ax[1, 0].legend(loc='upper left', fontsize='xx-small')
    
    df_corr_lixo = fu.agrupa_por_proporcao(df, escolha_coluna, colunas_lixo) # proporcao da quantidade de escolas no quesito lixo
    df_corr_lixo.index = idx
    df_corr_lixo.plot(kind='bar', stacked=True, figsize=(12, 10), ax=ax[1,1])
    ax[1, 1].tick_params(axis='x', labelrotation=0)
    ax[1, 1].legend(loc='upper left', fontsize='xx-small')

    fu.salva_imagens(fig, name)
