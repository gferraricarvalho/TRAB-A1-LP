import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # possibilita ler arquivos/módulos um nível acima

import ler_arquivo as la
from limpeza import funcoes as fl
import matplotlib.pyplot as plt
import funcoes_uteis as fu

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "microdados_ed_basica_2021.csv") # encontra a base de dados

df = la.ler_arquivo_csv(caminho_arquivo)

# colocar aqui as funções de limpeza...

columns_local = ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']
columns_agua = ['IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA',
                'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE']
columns_energia = ['IN_ENERGIA_REDE_PUBLICA', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ENERGIA_INEXISTENTE']
columns_esgoto = ['IN_ESGOTO_REDE_PUBLICA', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA', 'IN_ESGOTO_INEXISTENTE']
columns_lixo = ['IN_LIXO_SERVICO_COLETA', 'IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESTINO_FINAL_PUBLICO', 'IN_LIXO_DESCARTA_OUTRA_AREA',
                'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM', 'IN_TRATAMENTO_LIXO_INEXISTENTE']

colunas = columns_agua + columns_energia + columns_esgoto + columns_lixo

df = fu.atualiza_dataframe(df)

# Análise: a fazer...


