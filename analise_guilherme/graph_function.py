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
    fig, ax = plt.subplots(figsize= figuresize)
    dataframe.plot( kind= "barh", xlim= x_lim)
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    for i, v in enumerate(dataframe):
        ax.text(v, i, str(v), color= color_values, va='center')


    ax.set_yticklabels(new_label)

    plt.subplots_adjust(left=0.2)
    plt.show()
    plt.savefig(namefig)
    return
