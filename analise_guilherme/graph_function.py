import matplotlib.pyplot as plt

def generate_graph_bar(figuresize, dataframe, x_lim, titulo, x_label, y_label, color_values, new_label, namefig):
    """
    Função para gerar o gráfico de barras.

    Parameters
    ----------
    figuresize : tuple
        Tamanho da figura que será gerada.
    dataframe : dataframe
        Dataframe de dados original.
    x_lim : tuple
        Valores que definem os intervalos do eixo X.
    titulo : string
        Título da figura gerada.
    x_label : string
        Título do eixo X.
    y_label : string
        Título do eixo Y.
    color_values : string
        Define a cor dos valores individuais de cada coluna.
    new_label : list
        Novos nomes das colunas.
    namefig : string
        Nome da figura.

    Returns
    -------
    Apenas exibe o gráfico, e salva em png.

    """
    # Mapeamento de cores para categorias
    color_map = {'IN_ACESSIBILIDADE_CORRIMAO': "green", 'IN_ACESSIBILIDADE_ELEVADOR': "green",	
                 'IN_ACESSIBILIDADE_VAO_LIVRE': "green", 'IN_ACESSIBILIDADE_RAMPAS': "green",	
                 'IN_ACESSIBILIDADE_SINAL_VISUAL': "yellow", 'IN_ACESSIBILIDADE_SINAL_SONORO': "blue",
                 'IN_ACESSIBILIDADE_PISOS_TATEIS': "blue", 'IN_ACESSIBILIDADE_SINAL_TATIL': "blue", 
                 'IN_ACESSIBILIDADE_INEXISTENTE':"red"}

    # Define uma lista de cores com base nas categorias
    colors = [color_map[column] for column in dataframe.index]

    # Gera a figura do gráfico 
    fig, ax = plt.subplots(figsize= figuresize)
    dataframe.plot(kind="barh", xlim=x_lim, color=colors, legend=False, ax=ax)

    # Adiciona o título da figura, e os títulos dos eixos
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Adiciona os valores individuais em cada barra do gráfico
    for i, v in enumerate(dataframe):
        ax.text(v, i, str(v), color= color_values, va='center')

    rotulo_legenda = {"Deficiência Física": "green", "Deficiência Visual":"blue", "Deficiência Auditiva":"yellow","Sem Adaptação ou\n Acessibilidade":"red"}

    # Cria uma legenda personalizada
    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=rotulo_legenda[cor]) for cor in rotulo_legenda]
    plt.legend(legend_handles, rotulo_legenda, title='Legendas', loc='upper right')

    # Coloca os novos nomes para as colunas
    ax.set_yticklabels(new_label)

    # Desloca a figura à direita para melhor visualização
    plt.subplots_adjust(left=0.2)

    #Plota e salva a figura no formato png
    plt.show()
    fig.savefig(namefig)
    return
