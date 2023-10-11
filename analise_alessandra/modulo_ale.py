import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # possibilita ler arquivos/módulos um nível acima
import ler_arquivo as la

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "microdados_ed_basica_2021.csv") # encontra a base de dados

df_0 = la.ler_arquivo_csv(caminho_arquivo)

df = df_0[["TP_DEPENDENCIA", "QT_MAT_BAS_ND", "QT_MAT_BAS_BRANCA", "QT_MAT_BAS_PRETA", "QT_MAT_BAS_PARDA", "QT_MAT_BAS_AMARELA", "QT_MAT_BAS_INDIGENA"]]

tipo_agrupado = df.groupby("TP_DEPENDENCIA")

nao_declarada = tipo_agrupado["QT_MAT_BAS_ND"].sum()
branca = tipo_agrupado["QT_MAT_BAS_BRANCA"].sum()
preta = tipo_agrupado["QT_MAT_BAS_PRETA"].sum()
parda = tipo_agrupado["QT_MAT_BAS_PARDA"].sum()
amarela = tipo_agrupado["QT_MAT_BAS_AMARELA"].sum()
indigena = tipo_agrupado["QT_MAT_BAS_INDIGENA"].sum()


print ("Não declarada: ", nao_declarada, "Branca: ", branca, "Preta: ", preta, "Parda: ", parda, "Amarela: ", amarela, "Indígena: ", indigena, sep="\n\n")

plt.plot(nao_declarada, label="Não declarada")
plt.plot(branca, label="Branca")
plt.plot(preta, label="Preta")
plt.plot(parda, label="Parda")
plt.plot(amarela, label="Amarela")
plt.plot(indigena, label="Indígena")
plt.ylim(0,10000000)
plt.title("matriculas por tipo de escola")
plt.xlabel("tipo de escola")
plt.ylabel("Nº de matriculas")
plt.legend()
plt.show()