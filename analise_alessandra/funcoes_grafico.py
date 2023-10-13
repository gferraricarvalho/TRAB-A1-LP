import matplotlib.pyplot as plt

def grafico_de_linha_6_var (var1, var2, var3, var4, var5, var6, label1, label2, label3, label4, label5, label6, cor1, cor2, 
                      cor3, cor4, cor5, cor6, lim_inf_y, lim_sup_y, titulo, x_label, y_label, nome_figura):
    """
    Função para gerar e salvar um gráfico de linha com 6 variáveis.

    Parameters
    ----------
    var1 : Series
        Variável 1 que será plotada.
    var2 : Series
        Variável 2 que será plotada.
    var3 : Series
        Variável 3 que será plotada.
    var4 : Series
        Variável 4 que será plotada.
    var5 : Series
        Variável 5 que será plotada.
    var6 : Series
        Variável 6 que será plotada.
    label1 : string
        Descrição da 1 variável, que será escrito na legenda da figura.
    label2 : string
        Descrição da 2 variável, que será escrito na legenda da figura.
    label3 : string
        Descrição da 3 variável, que será escrito na legenda da figura.
    label4 : string
        Descrição da 4 variável, que será escrito na legenda da figura.
    label5 : string
        Descrição da 5 variável, que será escrito na legenda da figura.
    label6 : string
        Descrição da 6 variável, que será escrito na legenda da figura.
    cor1 : string
        Cor da linha da 1 variável, preferência por código hexadecimal. 
    cor2 : string
        Cor da linha da 2 variável, preferência por código hexadecimal. 
    cor3 : string
        Cor da linha da 3 variável, preferência por código hexadecimal. 
    cor4 : string
        Cor da linha da 4 variável, preferência por código hexadecimal. 
    cor5 : string
        Cor da linha da 5 variável, preferência por código hexadecimal. 
    cor6 : string
        Cor da linha da 6 variável, preferência por código hexadecimal. 
    lim_inf_y : float
        Limite inferior do eixo y.
    lim_sup_y : float
        Limite superior do eixo y.
    titulo : string
        Título do gráfico.
    x_label : string
        Nome do eixo x.
    y_label : string
        Nome do eixo y.
    nome_figura : string
        Nome que a figura será salva

    Returns
    -------
    Somente executa a função, mostra o gráfico e salva com o nome indicado.

    """
    plt.plot(var1, label=label1, color=cor1)
    plt.plot(var2, label=label2, color=cor2)
    plt.plot(var3, label=label3, color=cor3)
    plt.plot(var4, label=label4, color=cor4)
    plt.plot(var5, label=label5, color=cor5)
    plt.plot(var6, label=label6, color=cor6)
    plt.ylim(bottom=lim_inf_y, top=lim_sup_y)
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()
    plt.savefig(nome_figura)

    return 