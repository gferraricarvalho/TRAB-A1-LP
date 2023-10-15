import sys
import os
import funcoes_grafico as fg
import funcoes_selecao as fs

# possibilita ler arquivos/módulos um nível acima
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
import ler_arquivo as la

# encontra a base de dados
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "dados_limpos.csv")

df_0 = la.ler_arquivo_csv(caminho_arquivo)

#selecionando as colunas utilizadas para a análise
df = fs.selecionar_colunas(df_0, "TP_DEPENDENCIA", "QT_MAT_BAS_ND", "QT_MAT_BAS_BRANCA", "QT_MAT_BAS_PRETA", "QT_MAT_BAS_PARDA", "QT_MAT_BAS_AMARELA", "QT_MAT_BAS_INDIGENA")

#alterando os valores, segundo dados fornecidos pela base de dados
df = fs.trocar_valor(df, "TP_DEPENDENCIA", {1:"Federal", 2 : "Municipal", 3: "Estadual", 4:"Privada"})

#contando o número de matriculas por raça
nao_declarada = (fs.somar_valores_agrupado(df, "QT_MAT_BAS_ND", "TP_DEPENDENCIA"))/1000000
branca = (fs.somar_valores_agrupado(df, "QT_MAT_BAS_BRANCA", "TP_DEPENDENCIA"))/1000000
preta = (fs.somar_valores_agrupado(df, "QT_MAT_BAS_PRETA", "TP_DEPENDENCIA"))/1000000
parda = (fs.somar_valores_agrupado(df,"QT_MAT_BAS_PARDA", "TP_DEPENDENCIA"))/1000000
amarela = (fs.somar_valores_agrupado(df, "QT_MAT_BAS_AMARELA", "TP_DEPENDENCIA"))/1000000
indigena = (fs.somar_valores_agrupado(df, "QT_MAT_BAS_INDIGENA", "TP_DEPENDENCIA"))/1000000

#plotando o gráfico
grafico = fg.grafico_de_linha_6_var(nao_declarada, branca, preta, parda, amarela, indigena, "Não declarada", "Branca", 
                                    "Preta", "Parda", "Amarela", "Indígena", "#A569BD", "#F4D03F", "#3498DB", "#E74C3C", 
                                    "#58D68D", "#7F8C8D", 0, 10, "Número de matrículas na educação básica, por tipo de escola",
                                    "Tipo de escola", "Número de matriculas (em milhões)", "grafico_Ale.png")

#print dos dados, para análise
print ("Matrículas de pessoas da raça Não declarada: ", nao_declarada, "Matrículas de pessoas da raça Branca: ", branca,
       "Matrículas de pessoas da raça Preta: ", preta, "Matrículas de pessoas da raça Parda: ", parda, 
       "Matrículas de pessoas da raça Amarela: ", amarela, "Matrículas de pessoas da raça Indígena: ", indigena, sep="\n\n")