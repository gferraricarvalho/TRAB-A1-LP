import visualizacao as vz

def analise_completa():
    """
    Essa função é chamada pela main.py e após isso chama todas as funções disponíveis no arquivo visualizacao.py
    automatizando o processo da analise de dados, essa função não recebe nenhumparâmetro por conta que é feita 
    específicamente para essa analise

    Return
    ------
    estatisticas -> dict com todas as estatísticas dos estados 'SP','MG' e 'PA'
    """

    #localizando a base de dados
    colunas = ['SG_UF','NO_MUNICIPIO','IN_BANHEIRO_PNE', 'IN_BIBLIOTECA',
        'IN_DORMITORIO_ALUNO', 'IN_DORMITORIO_PROFESSOR', 'IN_QUADRA_ESPORTES'
        ]
    df = vz.localizacao('microdados_ed_basica_2021.csv')
  
    df_modificado = vz.organiza('SG_UF',df,colunas)

    """Aqui chamamos a função vz.visualização_RG para plotar todos os gráficos que serão usados"""
    vz.visualização_RG(df_modificado,'IN_BIBLIOTECA','escolas com bibliotecas',df_modificado['SG_UF'],'Escolas com bibliotecas por Unidade da Federação','imagem_1')
    vz.visualização_RG(df_modificado,'IN_BANHEIRO_PNE','quantidade de banheiros adaptados',df_modificado['SG_UF'],'quantidade de escolas com banheiros adaptados','imagem_2')
    vz.visualização_RG(df_modificado,'IN_DORMITORIO_ALUNO','dormitórios para alunos',df_modificado['SG_UF'],'Escolas dormitórios para alunos por Unidade da Federação','imagem_3')
    vz.visualização_RG(df_modificado,'IN_DORMITORIO_PROFESSOR','dormitórios para professores',df_modificado['SG_UF'],'Escolas com dormitórios para professores por Unidade da Federação','imagem_4')
    vz.visualização_RG(df_modificado,'IN_QUADRA_ESPORTES','quadras esportivas',df_modificado['SG_UF'],'Escolas com quadras esportivas por Unidade da Federação','imagem_5')

    """separando o dataframe por unidade de federação, 
        apenas aquelas que tiveram um grande resultado em relação as demais em cada um dos graficos"""
    df_sp = df.loc[df['SG_UF'] == 'SP'] #Destaque em banheiros adaptados e quadras esportivas
    df_mg = df.loc[df['SG_UF'] == 'MG'] #Destaque em bibliotecas e dormitorios para alunos
    df_pa = df.loc[df['SG_UF'] == 'PA'] #Destaque em dormitorios para professores

    #organizando cada um deles por municipio
    df_sp = vz.organiza('NO_MUNICIPIO',df_sp,colunas)
    df_mg = vz.organiza('NO_MUNICIPIO',df_mg,colunas)
    df_pa = vz.organiza('NO_MUNICIPIO',df_pa,colunas)

    # Criar um dicionário para armazenar as estatísticas de diferentes estados
    estatisticas = {}
 
    # Calcular as estatísticas para São Paulo e armazená-las no dicionário
    estatisticas['SP'] = {
        'estatisticas': vz.calcular_estatisticas(df_sp),
        'max_banheiro': vz.encontrar_max(df_sp, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_sp, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_sp, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_sp, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_dorm_professor': vz.encontrar_max(df_sp, 'IN_DORMITORIO_PROFESSOR','NO_MUNICIPIO')
    }

    # Calcular as estatísticas para Minas Gerais e armazená-las no dicionário
    estatisticas['MG'] = {
        'estatisticas': vz.calcular_estatisticas(df_mg),
        'max_banheiro': vz.encontrar_max(df_mg, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_mg, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_mg, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_mg, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_dorm_professor': vz.encontrar_max(df_mg, 'IN_DORMITORIO_PROFESSOR','NO_MUNICIPIO')
    }

    # Calcular as estatísticas para o Pará e armazená-las no dicionário
    estatisticas['PA'] = {
        'estatisticas': vz.calcular_estatisticas(df_pa),
        'max_banheiro': vz.encontrar_max(df_pa, 'IN_BANHEIRO_PNE','NO_MUNICIPIO'),
        'max_quadra': vz.encontrar_max(df_pa, 'IN_QUADRA_ESPORTES','NO_MUNICIPIO'),
        'max_biblioteca': vz.encontrar_max(df_pa, 'IN_BIBLIOTECA','NO_MUNICIPIO'),
        'max_dorm_aluno': vz.encontrar_max(df_pa, 'IN_DORMITORIO_ALUNO','NO_MUNICIPIO'),
        'max_dorm_professor': vz.encontrar_max(df_pa, 'IN_DORMITORIO_PROFESSOR','NO_MUNICIPIO')
    }
    
    return estatisticas













