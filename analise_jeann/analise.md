# ANÁLISE DOS RECURSOS ECOLÓGICOS PRESENTES NAS ESCOLAS BRASILEIRAS EM 2021

Nessa análise, serão abordados os aspectos descritivos e correlativos entre as instituições escolares dos diferentes locais e tipos e a distribuição dos recursos ecológicos (água, energia, esgoto e tratamento de lixo) nas mesmas.

A base de dados utilizda foi:

Para mais detalhes sobre o que cada coluna representa, consulte o dicionário de dados.

Essas análises foram retiradas dos prints e dos datasets e imagens salvos do arquivo _analise.py_. Para mais detalhes, confira o arquivo presente neste mesmo diretório.

## ANÁLISE DESCRITIVA

Primeiramente, vamos abordar o ponto de vista descritivo para efetuar a análise de como é distribuido os recursos ecológicos nas escolas do país. As medidas estatísticas utilizadas foram o mínimo, o máximo, a média, a mediana e o desvio padrão.

## ANÁLISE CORRELATIVA

Agora, vamos analisar a correlação entre cada um dos indicadores e o tipo de localização em que as escolas se encontram (urbana e rural) ou localização diferenciada (assentamentos, terras indígenas e remanescentes de quilombos) e o tipo de dependência escolar (federal, estadual, pública e privada), a fim de inferir como ocorre a proporção em cada um destes.

## IDEIAS ADICIONAIS

Analisando a base de dados (principalmente do ponto de vista de municípios e escolas - colunas NO_MUNICIPIO e NO_ENTIDADE, respectivamente - que não foram utilizados no dataframe para as análises, já que as mesmas se limitaram a uma visão global por regiões ou estados), observa-se que podemos associar a cada linha, um vetor, onde cada coordenada representa um dos indicadores ecológicos em questão. A fim de encontrar cidades (ou mesmo escolas) que são semelhantes de um modo geral nesses indicadores, devemos efetuar a distância entre cada um dos vetores agrupá-las em grupos (clusters) que indiquem que elas são similares entre si. Entretanto, isso seria um trabalho um pouco demorado (foram feitos alguns testes e o código demorou horas e não terminou de rodar). Pesquisei sobre isso e descobri que a bibliotecas em python que fazem esse agrupamento (ou clusterização), como a função kmeans presente na biblioteca sklearn. Mas, pelo tempo escasso para entender essa biblioteca e por recomendações externas de não utilizar ela pois ela seria vista em um curso futuro (pelo menos em Ciência de Dados) de Aprendizado de Máquina, resolvi me abster e ficar apenas com a motivação. Mas pretendo pesquisar mais a fundo em detalhes sobre essa ideia.

