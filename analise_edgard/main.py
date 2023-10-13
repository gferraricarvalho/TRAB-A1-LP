import visualizacao as vz

colunas = ['SG_UF','IN_BANHEIRO_PNE', 'IN_BIBLIOTECA',
    'IN_DORMITORIO_ALUNO', 'IN_DORMITORIO_PROFESSOR', 'IN_QUADRA_ESPORTES'
    ]
df_inicial = vz.localizacao( 'microdados_ed_basica_2021.csv')
df_modificado = vz.organiza('SG_UF',df_inicial,colunas)

vz.visualização_RG(df_modificado,'IN_BIBLIOTECA','escolas com bibliotecas',df_modificado['SG_UF'],'Escolas com bibliotecas por Unidade da Federação','imagem_1')
vz.visualização_RG(df_modificado,'IN_BANHEIRO_PNE','quantidade de banheiros adaptados',df_modificado['SG_UF'],'quantidade de escolas com banheiros adaptados','imagem_2')
vz.visualização_RG(df_modificado,'IN_DORMITORIO_ALUNO','dormitórios para alunos',df_modificado['SG_UF'],'Escolas dormitórios para alunos por Unidade da Federação','imagem_3')
vz.visualização_RG(df_modificado,'IN_DORMITORIO_PROFESSOR','dormitórios para professores',df_modificado['SG_UF'],'Escolas com dormitórios para professores por Unidade da Federação','imagem_4')
vz.visualização_RG(df_modificado,'IN_QUADRA_ESPORTES','quadras esportivas',df_modificado['SG_UF'],'Escolas com quadras esportivas por Unidade da Federação','imagem_5')

