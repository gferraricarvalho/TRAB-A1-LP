import sys
import os

diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)

import ler_arquivo as la
from limpeza import funcoes as fc
import pandas as pd
import matplotlib.pyplot as plt

 # encontra a base de dados
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "microdados_ed_basica_2021.csv")

# Lendo arquivo
dados = la.ler_arquivo_csv(caminho_arquivo)

#escolhendo as colunas que serão utilizadas
dados_utilizados = dados[['SG_UF', 'TP_CATEGORIA_ESCOLA_PRIVADA', 'IN_BIBLIOTECA',
   'IN_DORMITORIO_ALUNO', 'IN_DORMITORIO_PROFESSOR', 'IN_QUADRA_ESPORTES'
   ]]

#organizando por região
dados_regiao = dados.groupby('SG_UF').sum().reset_index()
regiao = dados_regiao['SG_UF']


while True:
    print("""
        1 = Quantidade de escolas privadas por região. \n
        2 = Quantidade de escolas com bibliotecas por região.\n
        3 = Quantidade de escolas com dormitórios para alunos, por região.\n
        4 = Quantidade de escolas com dormitórios para professores, por região.\n
        5 = Quantidade de escolas com quadras esportivas, por região.\n
""")
    escolha = input("qual doas graficos? \t")
    if escolha == '1':
        # Quantidade de escolas privadas por região
        quantidade = dados_regiao['TP_CATEGORIA_ESCOLA_PRIVADA']
        plt.bar(regiao,quantidade)
        plt.show()
        plt.xticks(rotation=90)
        
    elif escolha == '2':
        # Quantidade de escolas com bibliotecas por região
        quantidade = dados_regiao['IN_BIBLIOTECA']
        plt.bar(regiao,quantidade)
        plt.show()
        plt.xticks(rotation=90)

    elif escolha == '3':
        # Quantidade de escolas com dormitórios para alunos, por região
        quantidade = dados_regiao['IN_DORMITORIO_ALUNO']
        plt.bar(regiao,quantidade)
        plt.show()
        plt.xticks(rotation=90)

    elif escolha == '4':
        # Quantidade de escolas com dormitórios para professores, por região
        quantidade = dados_regiao['IN_DORMITORIO_PROFESSOR']
        plt.bar(regiao,quantidade)
        plt.show()
        plt.xticks(rotation=90)
        
    elif escolha == '5':
        # Quantidade de escolas com quadras esportivas, por região
        quantidade = dados_regiao['IN_QUADRA_ESPORTES']
        plt.bar(regiao,quantidade)
        plt.show()
        plt.xticks(rotation=90)
        
    else:
        break

















