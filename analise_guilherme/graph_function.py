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
    # Gera a figura do gráfico 
    fig, ax = plt.subplots(figsize= figuresize)
    dataframe.plot( kind= "barh", xlim= x_lim)

    # Adiciona o título da figura, e os títulos dos eixos
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Adiciona os valores individuais em cada barra do gráfico
    for i, v in enumerate(dataframe):
        ax.text(v, i, str(v), color= color_values, va='center')

    # Coloca os novos nomes para as colunas
    ax.set_yticklabels(new_label)

    # Desloca a figura à direita para melhor visualização
    plt.subplots_adjust(left=0.2)

    #Plota e salva a figura no formato png
    plt.show()
    plt.savefig(namefig)
    return
