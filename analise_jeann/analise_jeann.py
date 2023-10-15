import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # possibilita ler arquivos/módulos um nível acima

import ler_arquivo as la
import matplotlib.pyplot as plt
import funcoes_uteis as fu
import vizualizacao as vz

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "dados_limpos.csv") # encontra a base de dados

df = la.ler_arquivo_csv(caminho_arquivo)

columns_local = ['NO_REGIAO', 'SG_UF', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA']
columns_agua = ['IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE']
columns_energia = ['IN_ENERGIA_REDE_PUBLICA', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ENERGIA_INEXISTENTE']
columns_esgoto = ['IN_ESGOTO_REDE_PUBLICA', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA', 'IN_ESGOTO_INEXISTENTE']
columns_lixo = ['IN_LIXO_SERVICO_COLETA', 'IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESTINO_FINAL_PUBLICO', 'IN_LIXO_DESCARTA_OUTRA_AREA',
                'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM', 'IN_TRATAMENTO_LIXO_INEXISTENTE']

colunas = columns_agua + columns_energia + columns_esgoto + columns_lixo

df = fu.escolhe_colunas(df, columns_local + colunas)
fu.salva_dataset(df, 'dados_utilizados')

# Análise Descritiva

## Dados estatísticos das variáveis (por região e por estado)
dados_reg = fu.dados_descritivos(df, 'NO_REGIAO', colunas)
fu.salva_dataset(dados_reg, 'dados_reg')
dados_est = fu.dados_descritivos(df, 'SG_UF', colunas)
fu.salva_dataset(dados_est, 'dados_est')

## Dados (por região e por estado) da quantidade de escolas acima da média em abastecimento por água potável
## IN_AGUA_POTAVEL

fu.decora_print("Regiões acima da Média em abastecimento por água potável")
fu.acima_media(df, 'NO_REGIAO', ['IN_AGUA_POTAVEL'])
fu.decora_print("Estados acima da Média em abastecimento por água potável")
fu.acima_media(df, 'SG_UF', ['IN_AGUA_POTAVEL'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_AGUA_POTAVEL'], 1, 1, '11')
vz.viz_simples(df, 'SG_UF', ['IN_AGUA_POTAVEL'], 1, 1, '12')

## Dados (por região e por estado) da quantidade de escolas acima da média em abastecimento por água, energia, esgoto de rede pública e destino do lixo por poder público
## IN_AGUA_REDE_PUBLICA, IN_ENERGIA_REDE_PUBLICA, IN_ESGOTO_REDE_PUBLICA, IN_LIXO_DESTINO_FINAL_PUBLICO

fu.decora_print("Regiões acima da Média em abastecimento por água, energia e esgoto de rede pública e destino do lixo por poder público")
fu.acima_media(df, 'NO_REGIAO', ['IN_AGUA_REDE_PUBLICA', 'IN_ENERGIA_REDE_PUBLICA', 'IN_ESGOTO_REDE_PUBLICA', 'IN_LIXO_DESTINO_FINAL_PUBLICO'])
fu.decora_print("Estados acima da Média em abastecimento por água, energia e esgoto de rede pública e destino do lixo por poder público")
fu.acima_media(df, 'SG_UF', ['IN_AGUA_REDE_PUBLICA', 'IN_ENERGIA_REDE_PUBLICA', 'IN_ESGOTO_REDE_PUBLICA', 'IN_LIXO_DESTINO_FINAL_PUBLICO'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_AGUA_REDE_PUBLICA', 'IN_ENERGIA_REDE_PUBLICA', 'IN_ESGOTO_REDE_PUBLICA', 'IN_LIXO_DESTINO_FINAL_PUBLICO'], 2, 2, '21')
vz.viz_simples(df, 'SG_UF', ['IN_AGUA_REDE_PUBLICA', 'IN_ENERGIA_REDE_PUBLICA', 'IN_ESGOTO_REDE_PUBLICA', 'IN_LIXO_DESTINO_FINAL_PUBLICO'], 2, 2, '22')

## Dados (por região e por estado) da quantidade de escolas acima da média sem abastecimento por água, energia, esgoto e tratamento de lixo
## IN_AGUA_INEXISTENTE, IN_ENERGIA_INEXISTENTE, IN_ESGOTO_INEXISTENTE, IN_TRATAMENTO_LIXO_INEXISTENTE

fu.decora_print("Regiões acima da Média em abastecimento sem abastecimento por água, energia, esgoto e tratamento de lixo")
fu.acima_media(df, 'NO_REGIAO', ['IN_AGUA_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_TRATAMENTO_LIXO_INEXISTENTE'])
fu.decora_print("Estados acima da Média em abastecimento por água, energia, esgoto e tratamento de lixo")
fu.acima_media(df, 'SG_UF', ['IN_AGUA_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_TRATAMENTO_LIXO_INEXISTENTE'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_AGUA_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_TRATAMENTO_LIXO_INEXISTENTE'], 2, 2, '31')
vz.viz_simples(df, 'SG_UF', ['IN_AGUA_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_TRATAMENTO_LIXO_INEXISTENTE'], 2, 2, '32')

## Dados (por região e por estado) da quantidade de escolas acima da média em meios alternativos de abastecimento de água, energia e esgoto
## IN_AGUA_POCO_ARTESIANO, IN_AGUA_CACIMBA, IN_AGUA_FONTE_RIO, IN_ENERGIA_GERADOR_FOSSIL, IN_ENERGIA_RENOVAVEL, IN_ESGOTO_FOSSA_SEPTICA, IN_ESGOTO_FOSSA_COMUM, IN_ESGOTO_FOSSA

fu.decora_print("Regiões acima da Média em meios alternativos de abastecimento de água, energia e esgoto")
fu.acima_media(df, 'NO_REGIAO', ['IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA'])
fu.decora_print("Estados acima da Média em abastecimento por água potável")
fu.acima_media(df, 'SG_UF', ['IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA'], 2, 4, '41')
vz.viz_simples(df, 'SG_UF', ['IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA'], 2, 4, '42')

## Dados (por região e por estado) da quantidade de escolas que realizam serviço de coleta de lixo ou tratam o lixo
## IN_LIXO_SERVICO_COLETA, IN_TRATAMENTO_LIXO_SEPARACAO, IN_TRATAMENTO_LIXO_REUTILIZA, IN_TRATAMENTO_LIXO_RECICLAGEM

fu.decora_print("Regiões acima da Média que realizam serviço de coleta de lixo ou tratam o lixo")
fu.acima_media(df, 'NO_REGIAO', ['IN_LIXO_SERVICO_COLETA', 'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM'])
fu.decora_print("Estados acima da Média que realizam serviço de coleta de lixo ou tratam o lixo")
fu.acima_media(df, 'SG_UF', ['IN_LIXO_SERVICO_COLETA', 'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_LIXO_SERVICO_COLETA', 'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM'], 2, 2, '51')
vz.viz_simples(df, 'SG_UF', ['IN_LIXO_SERVICO_COLETA', 'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM'], 2, 2, '52')

## Dados (por região e por estado) da quantidade de escolas que realizam meios alternativos para o destino do lixo
## IN_LIXO_QUEIMA, IN_LIXO_ENTERRA, IN_LIXO_DESCARTA_OUTRA_AREA

fu.decora_print("Regiões acima da Média que realizam meios alternativos para o destino do lixo")
fu.acima_media(df, 'NO_REGIAO', ['IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESCARTA_OUTRA_AREA'])
fu.decora_print("Estados acima da Média que realizam meios alternativos para o destino do lixo")
fu.acima_media(df, 'SG_UF', ['IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESCARTA_OUTRA_AREA'])
vz.viz_simples(df, 'NO_REGIAO', ['IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESCARTA_OUTRA_AREA'], 1, 3, '61')
vz.viz_simples(df, 'SG_UF', ['IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESCARTA_OUTRA_AREA'], 1, 3, '62')


# Análise Correlativa

## Dados 
corr_loc = fu.agrupa_por_proporcao(df, 'TP_LOCALIZACAO', colunas)
fu.salva_dataset(corr_loc, 'corr_loc')
corr_loc_dif = fu.agrupa_por_proporcao(df, 'TP_LOCALIZACAO_DIFERENCIADA', colunas)
fu.salva_dataset(corr_loc_dif, 'corr_loc_dif')
corr_dep = fu.agrupa_por_proporcao(df, 'TP_DEPENDENCIA', colunas)
fu.salva_dataset(corr_dep, 'corr_dep')


## Dados da correlação entre a quantidade de escolas para cada indicador e o Tipo de Localização e Dependência Escolar

fu.decora_print("Correlação entre o Tipo de Localização e o abastecimento por água potável")
print(corr_loc)

fu.decora_print("Correlação entre o Tipo de Localização Diferenciada e o abastecimento por água potável")
print(corr_loc_dif)

fu.decora_print("Correlação entre o Tipo de Dependência e o abastecimento por água potável")
print(corr_dep)

## Salvando o plot dos dados para Tipo de Localização

vz.viz_correlativa(df, 'TP_LOCALIZACAO', columns_agua, columns_energia, columns_esgoto, columns_lixo, '71')

## Salvando o plot dos dados para Tipo de Localização Diferenciada

vz.viz_correlativa(df, 'TP_LOCALIZACAO_DIFERENCIADA', columns_agua, columns_energia, columns_esgoto, columns_lixo, '72')

## Salvando o plot dos dados para Tipo de Dependência

vz.viz_correlativa(df, 'TP_DEPENDENCIA', columns_agua, columns_energia, columns_esgoto, columns_lixo, '73')
