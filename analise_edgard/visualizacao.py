import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)

import ler_arquivo as la
from limpeza import funcoes as fc

def localizacao(nome_arquivo:str) -> pd.DataFrame:

     # encontra a base de dados
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',nome_arquivo)
    dados = la.ler_arquivo_csv(caminho_arquivo)
    dados = pd.DataFrame(dados)
    return dados

def organiza(parametro_ordem: str,dados: pd.DataFrame, colunas_usadas:str) -> pd.DataFrame:

     #escolhendo as colunas que serão utilizadas
    dados_utilizados = dados[colunas_usadas]

    #organizando por Sigla da Unidade da Federação
    dados_uf = dados_utilizados.groupby(parametro_ordem).sum().reset_index()
    
    return dados_uf


def visualização_RG(dados_uf: pd.DataFrame, coluna_desejada: str, eixo_y: str, eixo_x: pd.DataFrame, titulo: str,nome_imag:str):

    quantidade = dados_uf[coluna_desejada]
    fig, ax = plt.subplots()
    quantidade.plot(kind='bar', ax=ax)
    ax.set_ylabel(eixo_y)
    ax.set_title(titulo)
    ax.set_xticks(range(len(eixo_x)))
    ax.set_xticklabels(eixo_x, rotation=90)
    ax.axhline(y=quantidade.mean(), color='black', linestyle='solid', label='Média')
    plt.show()
    
    # Salva o gráfico como uma imagem
    if not os.path.exists('imagens'):
        os.makedirs('imagens')
    fig.savefig(f"imagens/{nome_imag}.png")

def calcular_estatisticas(dados):
    # Calcule estatísticas descritivas
    estatisticas = dados.describe()
    return estatisticas


