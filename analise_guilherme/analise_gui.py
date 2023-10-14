import sys
import os
import matplotlib.pyplot as plt
import clean_columns as cc
import graph_function as gf

# possibilita ler arquivos/módulos um nível acima
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
import ler_arquivo as la

# encontra a base de dados
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "microdados_ed_basica_2021.csv")

df_original = la.ler_arquivo_csv(caminho_arquivo)

colunas_filtradas = ['IN_ACESSIBILIDADE_CORRIMAO', 'IN_ACESSIBILIDADE_ELEVADOR',	'IN_ACESSIBILIDADE_VAO_LIVRE', 	'IN_ACESSIBILIDADE_RAMPAS',	'IN_ACESSIBILIDADE_SINAL_VISUAL',
                     'IN_ACESSIBILIDADE_SINAL_SONORO',	'IN_ACESSIBILIDADE_PISOS_TATEIS', 'IN_ACESSIBILIDADE_SINAL_TATIL', 'IN_ACESSIBILIDADE_INEXISTENTE']

df_filtrado = cc.filter_columns(df_original, colunas_filtradas)

novo_rotulo = ['Corrimão', 'Elevador', 'Vão Livre', 'Rampas', 'Sinal Visual', 'Sinal Sonoro', 'Pisos Táteis', 'Sinal Tátil', 'Inexistente']

df_acessibilidade = cc.sum_columns(df_filtrado)

grafico = gf.generate_graph_bar((10,6), df_acessibilidade, (0,100000), "Acessibilidade (221140 Escolas Analisadas)", "N° de Escolas", "Tipo de Acessibilidade", "black", novo_rotulo, "acessibilidade.png")
