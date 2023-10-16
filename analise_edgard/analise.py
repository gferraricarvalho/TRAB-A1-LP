import visualizacao as vz

def analise():
    '''
    Após executar esse arquivo ele chama todas as funções disponíveis no arquivo visualizacao.py em uma função que 
    retorna um dicionário automatizando o processo da analise de dados específicamente para essa análise, faz o print desse 
    dicionário.

    Return 
    ------  
    estatisticas -> dict com todas as estatísticas dos estados 'SP','MG' e 'PA'.
    '''

    colunas = ['SG_UF','NO_MUNICIPIO','IN_BANHEIRO_PNE', 'IN_BIBLIOTECA',
        'IN_DORMITORIO_ALUNO','IN_REFEITORIO', 'IN_QUADRA_ESPORTES'
        ]
    #localizando a base de dados
    df = vz.localizacao('dados_limpos.csv')

    #frequencia com que cada estado aparece
    freq = vz.freq_contagem(df,'SG_UF').sort_index()

    #organizando o Dataframe por Estado
    df_modificado = vz.organiza('SG_UF',df,colunas)

    #Aqui chamamos a função vz.visualização_RG para plotar todos os gráficos que serão usados
    vz.visualizacao_RG(df_modificado,'IN_BIBLIOTECA','escolas com bibliotecas',df_modificado['SG_UF'],'Escolas com bibliotecas por Unidade da Federação','imagem_1',freq)
    vz.visualizacao_RG(df_modificado,'IN_BANHEIRO_PNE','quantidade de banheiros adaptados',df_modificado['SG_UF'],'quantidade de escolas com banheiros adaptados','imagem_2',freq)
    vz.visualizacao_RG(df_modificado,'IN_DORMITORIO_ALUNO','dormitórios para alunos',df_modificado['SG_UF'],'Escolas dormitórios para alunos por Unidade da Federação','imagem_3',freq)
    vz.visualizacao_RG(df_modificado,'IN_REFEITORIO','refeitorias em escolas',df_modificado['SG_UF'],'Escolas com refeitórios','imagem_4',freq)
    vz.visualizacao_RG(df_modificado,'IN_QUADRA_ESPORTES','quadras esportivas',df_modificado['SG_UF'],'Escolas com quadras esportivas por Unidade da Federação','imagem_5',freq)


    #separando o dataframe por unidade de federação, 
    # apenas aquelas que tiveram um grande resultado em relação as demais em cada um dos graficos
    df_ac = df.loc[df['SG_UF'] == 'AC'] #Menor proporção entre quantidade de escolas totais e escolas com bibliotecas
    df_am = df.loc[df['SG_UF'] == 'AM'] #Menor proporção entre quantidade de escolas totais e escolas com banheiros adaptados 
    df_sp = df.loc[df['SG_UF'] == 'SP'] #Menor proporção entre quantidade de escolas totais e escolas com dormitórios para alunos
    df_ma = df.loc[df['SG_UF'] == 'MA'] #Menor proporção entre quantidade de escolas totais e escolas com refeitórios e quadras esportivas

    #organizando cada um deles por municipio
    df_ac = vz.organiza('NO_MUNICIPIO',df_ac,colunas)
    df_am = vz.organiza('NO_MUNICIPIO',df_am,colunas)
    df_sp = vz.organiza('NO_MUNICIPIO',df_sp,colunas)
    df_ma = vz.organiza('NO_MUNICIPIO',df_ma,colunas)

    # Criar um dicionário para armazenar as estatísticas de diferentes estados
    estatisticas = {}

    # Calcular as estatísticas para São Paulo e armazená-las no dicionário
    estatisticas['SP'] = {
        'estatisticas': vz.calcular_estatisticas(df_sp),
        'max_banheiro': vz.encontrar_max(df_sp, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_sp, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_sp, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_sp, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_refeitório': vz.encontrar_max(df_sp, 'IN_REFEITORIO','NO_MUNICIPIO')
    }

    # Calcular as estatísticas para Minas Gerais e armazená-las no dicionário
    estatisticas['MA'] = {
        'estatisticas': vz.calcular_estatisticas(df_ma),
        'max_banheiro': vz.encontrar_max(df_ma, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_ma, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_ma, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_ma, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_refeitório': vz.encontrar_max(df_ma, 'IN_REFEITORIO','NO_MUNICIPIO')
    }
    estatisticas['AM'] = {
        'estatisticas': vz.calcular_estatisticas(df_ma),
        'max_banheiro': vz.encontrar_max(df_am, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_am, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_am, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_am, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_refeitório': vz.encontrar_max(df_am, 'IN_REFEITORIO','NO_MUNICIPIO')
    }
    estatisticas['AC'] = {
        'estatisticas': vz.calcular_estatisticas(df_ac),
        'max_banheiro': vz.encontrar_max(df_ac, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_ac, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_ac, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_ac, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_refeitório': vz.encontrar_max(df_ac, 'IN_REFEITORIO','NO_MUNICIPIO')
    }

    print(estatisticas['MA'])
    print(100*"#")
    print(estatisticas['AM'])
    print(100*"#")
    print(estatisticas['AC'])
    print(100*"#") 

    return estatisticas

if __name__ == "__main__":
    analise()









