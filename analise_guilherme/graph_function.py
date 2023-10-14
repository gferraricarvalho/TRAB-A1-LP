import matplotlib.pyplot as plt

def generate_graph_bar(figuresize, dataframe, x_lim, titulo, x_label, y_label, color_values, new_label, namefig):

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
