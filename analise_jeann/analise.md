# ANÁLISE DOS RECURSOS ECOLÓGICOS PRESENTES NAS ESCOLAS BRASILEIRAS EM 2021

Nessa análise, serão abordados os aspectos descritivos, correlativos e de similaridade entre as instituições escolares dos diferentes locais e a distribuição dos recursos ecológicos (água, energia, esgoto e tratamento de lixo) nas mesmas.

As colunas da base de dados utilizadas para essa análise foram:
- local: 'NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'TP_DEPENDENCIA'
- água: 'IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO', 'IN_AGUA_CACIMBA',                'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE'
- energia: 'IN_ENERGIA_REDE_PUBLICA', 'IN_ENERGIA_GERADOR_FOSSIL', 'IN_ENERGIA_RENOVAVEL', 'IN_ENERGIA_INEXISTENTE'
- esgoto: 'IN_ESGOTO_REDE_PUBLICA', 'IN_ESGOTO_FOSSA_SEPTICA', 'IN_ESGOTO_FOSSA_COMUM', 'IN_ESGOTO_FOSSA', 'IN_ESGOTO_INEXISTENTE'
- tratamento de lixo: 'IN_LIXO_SERVICO_COLETA', 'IN_LIXO_QUEIMA', 'IN_LIXO_ENTERRA', 'IN_LIXO_DESTINO_FINAL_PUBLICO', 'IN_LIXO_DESCARTA_OUTRA_AREA', 'IN_TRATAMENTO_LIXO_SEPARACAO', 'IN_TRATAMENTO_LIXO_REUTILIZA', 'IN_TRATAMENTO_LIXO_RECICLAGEM', 'IN_TRATAMENTO_LIXO_INEXISTENTE'

Para mais detalhes sobre o que cada coluna representa, consulte o dicionário de dados.

## ANÁLISE DESCRITIVA

Primeiramente, vamos abordar o ponto de vista descritivo para efetuar a análise de como é distribuido os recursos ecológicos nas escolas do país. As medidas estatísticas utilizadas foram o mínimo, o máximo, a média, a mediana e o desvio padrão.

Do ponto de vista das Regiões Demográficas do Brasil, temos as seguintes medidas estatísticas:

![Dados Descritivos das Escolas Brasileiras, por Regiões Demográficas](dados_reg.csv)

Destas, as que se encontram acima da média em cada indicador são:

IN_AGUA_POTAVEL: ['Nordeste', 'Sudeste']
IN_AGUA_REDE_PUBLICA: ['Nordeste', 'Sudeste']
IN_AGUA_POCO_ARTESIANO: ['Norte', 'Nordeste']
IN_AGUA_CACIMBA: ['Nordeste']
IN_AGUA_FONTE_RIO: ['Norte']
IN_AGUA_INEXISTENTE: ['Norte', 'Nordeste']
IN_ENERGIA_REDE_PUBLICA: ['Sudeste', 'Nordeste']
IN_ENERGIA_GERADOR_FOSSIL: ['Norte']
IN_ENERGIA_RENOVAVEL: ['Sudeste', 'Norte', 'Nordeste']
IN_ENERGIA_INEXISTENTE: ['Norte']
IN_ESGOTO_REDE_PUBLICA: ['Nordeste', 'Sudeste']
IN_ESGOTO_FOSSA_SEPTICA: ['Nordeste']
IN_ESGOTO_FOSSA_COMUM: ['Norte', 'Nordeste']
IN_ESGOTO_FOSSA: ['Norte', 'Nordeste']
IN_ESGOTO_INEXISTENTE: ['Nordeste', 'Norte']
IN_LIXO_SERVICO_COLETA: ['Sudeste', 'Nordeste']
IN_LIXO_QUEIMA: ['Norte', 'Nordeste']
IN_LIXO_ENTERRA: ['Nordeste', 'Norte']
IN_LIXO_DESTINO_FINAL_PUBLICO: ['Sudeste']
IN_LIXO_DESCARTA_OUTRA_AREA: ['Nordeste', 'Norte']
IN_TRATAMENTO_LIXO_SEPARACAO: ['Sul', 'Nordeste', 'Sudeste']
IN_TRATAMENTO_LIXO_REUTILIZA: ['Sudeste', 'Nordeste']
IN_TRATAMENTO_LIXO_RECICLAGEM: ['Sul', 'Nordeste', 'Sudeste']
IN_TRATAMENTO_LIXO_INEXISTENTE: ['Sudeste', 'Nordeste']

Analogamente, podemos fazer o mesmo para os estados brasileiros:

![Dados Descritivos das Escolas Brasileiras, por estados](dados_est.csv)

Os estados que se encontram acima da média em cada indicador são:

IN_AGUA_POTAVEL: ['SC', 'CE', 'PE', 'PA', 'PR', 'RS', 'MA', 'RJ', 'BA', 'MG', 'SP']
IN_AGUA_REDE_PUBLICA: ['MA', 'PE', 'CE', 'SC', 'RS', 'PR', 'RJ', 'BA', 'MG', 'SP']
IN_AGUA_POCO_ARTESIANO: ['PI', 'RS', 'AM', 'MG', 'BA', 'MA', 'PA']
IN_AGUA_CACIMBA: ['RN', 'AL', 'RJ', 'MA', 'PA', 'PB', 'CE', 'BA', 'PE']
IN_AGUA_FONTE_RIO: ['MG', 'BA', 'PA', 'AM']
IN_AGUA_INEXISTENTE: ['PI', 'BA', 'PE', 'AC', 'PA', 'MA']
IN_ENERGIA_REDE_PUBLICA: ['SC', 'CE', 'PE', 'PA', 'PR', 'RS', 'RJ', 'MA', 'MG', 'BA', 'SP']
IN_ENERGIA_GERADOR_FOSSIL: ['AP', 'AC', 'AM', 'PA']
IN_ENERGIA_RENOVAVEL: ['PR', 'AM', 'RS', 'RJ', 'SP', 'MG', 'BA', 'PA']
IN_ENERGIA_INEXISTENTE: ['RR', 'BA', 'AC', 'AM', 'PA']
IN_ESGOTO_REDE_PUBLICA: ['SC', 'PE', 'PR', 'RS', 'BA', 'RJ', 'MG', 'SP']
IN_ESGOTO_FOSSA_SEPTICA: ['MG', 'CE', 'AM', 'PR', 'RS', 'SC', 'PI', 'PA', 'BA', 'MA']
IN_ESGOTO_FOSSA_COMUM: ['MG', 'PR', 'RS', 'CE', 'PE', 'MA', 'BA', 'PA']
IN_ESGOTO_FOSSA: ['SC', 'AM', 'MG', 'PI', 'PR', 'PE', 'RS', 'CE', 'PA', 'BA', 'MA']
IN_ESGOTO_INEXISTENTE: ['PI', 'BA', 'AC', 'PA', 'MA', 'AM']
IN_LIXO_SERVICO_COLETA: ['PA', 'MA', 'PE', 'CE', 'SC', 'PR', 'RS', 'SP', 'RJ', 'BA', 'MG']
IN_LIXO_QUEIMA: ['PI', 'PE', 'MG', 'AM', 'BA', 'PA', 'MA']
IN_LIXO_ENTERRA: ['MT', 'PR', 'SC', 'MA', 'BA', 'AC', 'RS', 'PA', 'AM']
IN_LIXO_DESTINO_FINAL_PUBLICO: ['SP']
IN_LIXO_DESCARTA_OUTRA_AREA: ['AC', 'BA', 'MA', 'AM', 'PA']
IN_TRATAMENTO_LIXO_SEPARACAO: ['PE', 'SC', 'BA', 'RJ', 'MG', 'RS', 'PR', 'SP']
IN_TRATAMENTO_LIXO_REUTILIZA: ['SC', 'PB', 'PA', 'SP', 'MA', 'PE', 'RS', 'MG', 'BA', 'RJ']
IN_TRATAMENTO_LIXO_RECICLAGEM: ['MA', 'PE', 'SC', 'RS', 'PR', 'BA', 'MG', 'RJ', 'SP']
IN_TRATAMENTO_LIXO_INEXISTENTE: ['AM', 'CE', 'PE', 'PA', 'RJ', 'MG', 'MA', 'BA', 'SP']

Pode-se observar, portanto, que [Análise Pessoal]

Isso pode ser facilmente comprovado visualmente, como segue nos gráficos abaixo:

![](desc_NO_REGIAO.png)

![](desc_SG_UF.png)

[Colocar gráfico específico]

[Acabar Análise Descritiva]

## ANÁLISE CORRELATIVA

Agora, vamos analisar a correlação entre cada um dos indicadores e o tipo de localização em que as escolas se encontram (urbana e rural) ou localização diferenciada (assentamentos, terras indígenas e remanescentes de quilombos) e o tipo de dependência escolar (federal, estadual, pública e privada), a fim de inferir como ocorre a proporção em cada um destes.

## ANÁLISE CLUSTERIZADA


