import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # possibilita ler arquivos/módulos um nível acima

import ler_arquivo as la
import matplotlib.pyplot as plt
import funcoes_uteis as fu
import vizualizacao as vz

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "microdados_ed_basica_2021.csv") # encontra a base de dados

df = la.ler_arquivo_csv(caminho_arquivo)

columns_local = ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']
columns_agua = ['IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE']
columns_energia = ['IN_ENERGIA_REDE_PUBLICA', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ENERGIA_INEXISTENTE']
columns_esgoto = ['IN_ESGOTO_REDE_PUBLICA', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA', 'IN_ESGOTO_INEXISTENTE']
columns_lixo = ['IN_LIXO_SERVICO_COLETA', 'IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESTINO_FINAL_PUBLICO', 'IN_LIXO_DESCARTA_OUTRA_AREA',
                'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM', 'IN_TRATAMENTO_LIXO_INEXISTENTE']

colunas = columns_agua + columns_energia + columns_esgoto + columns_lixo

df = fu.escolhe_colunas(df, columns_local + colunas)

# Análise Descritiva

## Dados (por região e por estado) de escolas acima da média em cada indicador
dados_reg = fu.dados_descritivos(df, 'NO_REGIAO', colunas)
dados_reg.to_csv()
fu.decora_print("Regiões acima da Média nos Indicadores")

dados_reg_acima_med = fu.acima_media(df, 'NO_REGIAO', colunas)

dados_est = fu.dados_descritivos(df, 'SG_UF', colunas)
dados_est.to_csv()
fu.decora_print("Estados acima da Média nos Indicadores")

dados_est_acima_med = fu.acima_media(df, 'SG_UF', colunas)


## Frequência da ocorrência de cada indicador na escolas
fu.decora_print("Frequência de cada Indicador nas Escolas")

fu.dist_freq(df, colunas)

## Vizualização Descritiva Simples e por Distribuição de Frequências por Região, Estado e Município

vz.viz_simples(df, 'NO_REGIAO', colunas)
vz.viz_simples(df, 'SG_UF', colunas)
vz.viz_dist_freq(df, 'NO_REGIAO', colunas)
vz.viz_dist_freq(df, 'SG_UF', colunas)
vz.viz_dist_freq(df, 'NO_MUNICIPIO', colunas)

# Análise Correlativa

## Correlação entre o tipo de localização e cada indicador

fu.decora_print("Correlação entre o Tipo de Localização e cada Indicador")

fu.agrupa_por(df, 'TP_LOCALIZACAO', colunas)

fu.decora_print("Correlação entre o Tipo de Localização Diferenciada e cada Indicador")

fu.agrupa_por(df, 'TP_LOCALIZACAO_DIFERENCIADA', colunas)

fu.decora_print("Correlação entre o Tipo de Dependência Escolar e cada Indicador")

fu.agrupa_por(df, 'TP_DEPENDENCIA', colunas)

## Vizualização Correlativa dos Tipos de Localização e Dependência Escolar para cada tipo Ecológico

vz.viz_correlativa(df, 'TP_LOCALIZACAO', columns_agua, columns_energia, columns_esgoto, columns_lixo)
vz.viz_correlativa(df, 'TP_LOCALIZACAO_DIFERENCIADA', columns_agua, columns_energia, columns_esgoto, columns_lixo)
vz.viz_correlativa(df, 'TP_DEPENDENCIA', columns_agua, columns_energia, columns_esgoto, columns_lixo)

# Análise Clusterizativa

## Calculo da proximidade de um Estado, Município ou Escola em relação à outros do país em cada indicador

# a fazer...

## Vizualização Clusterizada dos Estados, Municípios ou Escolas mais Próximos(as) para cada indicador 

# a fazer...