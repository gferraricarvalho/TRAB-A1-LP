from limpeza import funcoes as fl
import ler_arquivo as la
import os

# lendo a base de dados
df = la.ler_arquivo_csv("microdados_ed_basica_2021.csv")

# limpando a base de dados
df = fl.colunas_indesejadas(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colunas_nao_utilizadas.txt'), df)
df = fl.remove_duplicadas(df)
df = fl.remove_NaN(df)
df = fl.excluir_colunas_de_zeros(df)
for col in df.columns:
    if all(df[col].apply(lambda x: isinstance(x, int))):
        df = fl.excluir_outliers(df, col)

# salvando a base limpa
df.to_csv('dados_limpos.csv', sep=';')