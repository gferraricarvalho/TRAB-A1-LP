import matplotlib.pyplot as plt

def grafico_de_linha_6_var (var1, var2, var3, var4, var5, var6, label1, label2, label3, label4, label5, label6, cor1, cor2, 
                      cor3, cor4, cor5, cor6, lim_inf_y, lim_sup_y, titulo, x_label, y_label):
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

    return plt.savefig("grafico_Ale.png")