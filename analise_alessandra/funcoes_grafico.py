import matplotlib.pyplot as plt
import numpy as np

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

    figura = plt.figure()
    #O bloco abaixo plota as 6 variáveis em um único gráfico
    barWidht=0.13

    p1 = np.arange(len(var1))
    p2 = [x + barWidht for x in p1]
    p3 = [x + barWidht for x in p2]
    p4 = [x + barWidht for x in p3]
    p5 = [x + barWidht for x in p4]
    p6 = [x + barWidht for x in p5]

    plt.bar(p1, var1, label=label1, color=cor1, width=barWidht)
    plt.bar(p2, var2, label=label2, color=cor2, width=barWidht)
    plt.bar(p3, var3, label=label3, color=cor3, width=barWidht)
    plt.bar(p4, var4, label=label4, color=cor4, width=barWidht)
    plt.bar(p5, var5, label=label5, color=cor5, width=barWidht)
    plt.bar(p6, var6, label=label6, color=cor6, width=barWidht)
    plt.ylim(bottom=lim_inf_y, top=lim_sup_y)
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.xticks([p + barWidht for p in range(len(var1))], ["Estadual", "Federal", "Municipal", "Privada"])
    plt.ylabel(y_label)
    #adiciona legenda ao gráfico, pois são várias variáveis
    plt.legend()
    #mostra a figura
    plt.show()
    #salva a figura
    figura.savefig(nome_figura)

    return