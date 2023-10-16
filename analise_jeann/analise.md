# ANÁLISE DOS RECURSOS ECOLÓGICOS PRESENTES NAS ESCOLAS BRASILEIRAS EM 2021

Nessa análise, serão abordados os aspectos descritivos e correlativos entre as instituições escolares dos diferentes locais e tipos e a distribuição dos recursos ecológicos (água, energia, esgoto e tratamento de lixo) nas mesmas.

A base de dados utilizada foi:

|        | NO_REGIAO    | SG_UF   |   TP_LOCALIZACAO |   TP_LOCALIZACAO_DIFERENCIADA |   TP_DEPENDENCIA |   IN_AGUA_POTAVEL |   IN_AGUA_REDE_PUBLICA |   IN_AGUA_POCO_ARTESIANO |   IN_AGUA_CACIMBA |   IN_AGUA_FONTE_RIO |   IN_AGUA_INEXISTENTE |   IN_ENERGIA_REDE_PUBLICA |   IN_ENERGIA_GERADOR_FOSSIL |   IN_ENERGIA_RENOVAVEL |   IN_ENERGIA_INEXISTENTE |   IN_ESGOTO_REDE_PUBLICA |   IN_ESGOTO_FOSSA_SEPTICA |   IN_ESGOTO_FOSSA_COMUM |   IN_ESGOTO_FOSSA |   IN_ESGOTO_INEXISTENTE |   IN_LIXO_SERVICO_COLETA |   IN_LIXO_QUEIMA |   IN_LIXO_ENTERRA |   IN_LIXO_DESTINO_FINAL_PUBLICO |   IN_LIXO_DESCARTA_OUTRA_AREA |   IN_TRATAMENTO_LIXO_SEPARACAO |   IN_TRATAMENTO_LIXO_REUTILIZA |   IN_TRATAMENTO_LIXO_RECICLAGEM |   IN_TRATAMENTO_LIXO_INEXISTENTE |
|-------:|:-------------|:--------|-----------------:|------------------------------:|-----------------:|------------------:|-----------------------:|-------------------------:|------------------:|--------------------:|----------------------:|--------------------------:|----------------------------:|-----------------------:|-------------------------:|-------------------------:|--------------------------:|------------------------:|------------------:|------------------------:|-------------------------:|-----------------:|------------------:|--------------------------------:|------------------------------:|-------------------------------:|-------------------------------:|--------------------------------:|---------------------------------:|
|      0 | Norte        | RO      |                2 |                             2 |                2 |                 1 |                      0 |                        1 |                 0 |                   0 |                     0 |                         0 |                           1 |                      0 |                        0 |                        0 |                         0 |                       0 |                 0 |                       1 |                        0 |                1 |                 1 |                               0 |                             0 |                              0 |                              0 |                               0 |                                1 |
|      1 | Norte        | RO      |                1 |                             0 |                2 |                 1 |                      1 |                        0 |                 0 |                   0 |                     0 |                         1 |                           0 |                      0 |                        0 |                        0 |                         1 |                       0 |                 1 |                       0 |                        1 |                0 |                 0 |                               0 |                             0 |                              0 |                              0 |                               0 |                                1 |
|      2 | Norte        | RO      |                2 |                             0 |                3 |                 1 |                      0 |                        0 |                 1 |                   0 |                     0 |                         1 |                           0 |                      0 |                        0 |                        0 |                         1 |                       0 |                 1 |                       0 |                        0 |                1 |                 0 |                               0 |                             0 |                              0 |                              0 |                               0 |                                1 |
|      3 | Norte        | RO      |                1 |                             0 |                3 |                 1 |                      0 |                        0 |                 1 |                   0 |                     0 |                         1 |                           0 |                      0 |                        0 |                        0 |                         1 |                       0 |                 1 |                       0 |                        1 |                0 |                 0 |                               0 |                             0 |                              0 |                              0 |                               0 |                                1 |
|      4 | Norte        | RO      |                2 |                             0 |                3 |                 1 |                      0 |                        1 |                 0 |                   0 |                     0 |                         1 |                           0 |                      0 |                        0 |                        0 |                         1 |                       0 |                 1 |                       0 |                        0 |                1 |                 0 |                               0 |                             0 |                              0 |                              0 |                               0 |                                1 |
|      5 | Norte        | RO      |                1 |                             0 |                2 |                 1 |                      1 |                        1 |                 0 |                   0 |                     0 |                         1 |                           0 |                      0 |                        0 |                        0 |                         1 |                       0 |                 1 |                       0 |                        1 |                0 |                 0 |                               0 |                             0 |                              0 |                              1 |                               1 |                                0 |
|      ... | ...        | ...      |                ... |                             ... |                ... |                 ... |                      ... |                        ... |                 ... |                   ... |                     ... |                         ... |                           ... |                      ... |                        ... |                        ... |                         ... |                       ... |                 ... |                       ... |                        ... |                ... |                 ... |                               ... |                             ... |                              ... |                              ... |                               ... |                                ... |


Para mais detalhes sobre o que cada coluna representa, consulte o dicionário de dados.

Essas análises foram retiradas dos prints e dos datasets e imagens salvos do arquivo _analise.py_. Para mais detalhes, confira o arquivo presente neste mesmo diretório.

## ANÁLISE DESCRITIVA

Primeiramente, vamos abordar o ponto de vista descritivo para efetuar a análise de como é distribuido os recursos ecológicos nas escolas do país. As medidas estatísticas utilizadas foram o mínimo, o máximo, a média, a mediana e o desvio padrão.

De modo geral, temos os seguintes dados estatísticos a cerca de cada um dos indicadores

- Por região:

|               |   IN_AGUA_POTAVEL |   IN_AGUA_REDE_PUBLICA |   IN_AGUA_POCO_ARTESIANO |   IN_AGUA_CACIMBA |   IN_AGUA_FONTE_RIO |   IN_AGUA_INEXISTENTE |   IN_ENERGIA_REDE_PUBLICA |   IN_ENERGIA_GERADOR_FOSSIL |   IN_ENERGIA_RENOVAVEL |   IN_ENERGIA_INEXISTENTE |   IN_ESGOTO_REDE_PUBLICA |   IN_ESGOTO_FOSSA_SEPTICA |   IN_ESGOTO_FOSSA_COMUM |   IN_ESGOTO_FOSSA |   IN_ESGOTO_INEXISTENTE |   IN_LIXO_SERVICO_COLETA |   IN_LIXO_QUEIMA |   IN_LIXO_ENTERRA |   IN_LIXO_DESTINO_FINAL_PUBLICO |   IN_LIXO_DESCARTA_OUTRA_AREA |   IN_TRATAMENTO_LIXO_SEPARACAO |   IN_TRATAMENTO_LIXO_REUTILIZA |   IN_TRATAMENTO_LIXO_RECICLAGEM |   IN_TRATAMENTO_LIXO_INEXISTENTE |
|:--------------|------------------:|-----------------------:|-------------------------:|------------------:|--------------------:|----------------------:|--------------------------:|----------------------------:|-----------------------:|-------------------------:|-------------------------:|--------------------------:|------------------------:|------------------:|------------------------:|-------------------------:|-----------------:|------------------:|--------------------------------:|------------------------------:|-------------------------------:|-------------------------------:|--------------------------------:|---------------------------------:|
| MINIMO        |           10163   |                 7305   |                  1909    |             261   |              162    |                20     |                   10240   |                      23     |                183     |                      6   |                   2942   |                   2795    |                 1941    |            4736   |                   61    |                   9615   |           611    |           233     |                            99   |                        105    |                        4979    |                        1551    |                         2160    |                           6803   |
| MAXIMO        |           59627   |                55103   |                 10955    |           10869   |             4174    |              1992     |                   59982   |                    1733     |                528     |                   2851   |                  53047   |                  18889    |                16631    |           35520   |                 3992    |                  43161   |         17401    |          1917     |                         21729   |                       3362    |                       24252    |                        9542    |                        13032    |                          55624   |
| MEDIA         |           34034   |                27154.4 |                  5571.6  |            3200.8 |             1410.2  |               712.6   |                   34558.6 |                     393.6   |                379.8   |                    651   |                  20282.4 |                   8064.6  |                 6418.8  |           14483.4 |                 1513    |                  25250.4 |          6390.8  |           836.6   |                          4822.4 |                       1066.2  |                       14821.8  |                        4785.2  |                         7089.6  |                          25912.6 |
| MEDIANA       |           25008   |                23283   |                  4089    |            1865   |             1077    |               122     |                   25777   |                      74     |                453     |                     22   |                  16630   |                   6698    |                 3468    |           10166   |                  290    |                  25118   |          2415    |           744     |                           540   |                        301    |                       19522    |                        3504    |                         7089    |                          20266   |
| DESVIO PADRAO |           23001.8 |                20706.6 |                  3863.21 |            4386.6 |             1618.87 |               924.148 |                   23809.3 |                     749.376 |                156.009 |                   1239.4 |                  20049.4 |                   6296.59 |                 6188.02 |           12386.9 |                 1886.32 |                  15311   |          7418.23 |           687.117 |                          9469.2 |                       1400.84 |                        8934.62 |                        3208.73 |                         4719.35 |                          21359.5 |

- Por estado:

|               |   IN_AGUA_POTAVEL |   IN_AGUA_REDE_PUBLICA |   IN_AGUA_POCO_ARTESIANO |   IN_AGUA_CACIMBA |   IN_AGUA_FONTE_RIO |   IN_AGUA_INEXISTENTE |   IN_ENERGIA_REDE_PUBLICA |   IN_ENERGIA_GERADOR_FOSSIL |   IN_ENERGIA_RENOVAVEL |   IN_ENERGIA_INEXISTENTE |   IN_ESGOTO_REDE_PUBLICA |   IN_ESGOTO_FOSSA_SEPTICA |   IN_ESGOTO_FOSSA_COMUM |   IN_ESGOTO_FOSSA |   IN_ESGOTO_INEXISTENTE |   IN_LIXO_SERVICO_COLETA |   IN_LIXO_QUEIMA |   IN_LIXO_ENTERRA |   IN_LIXO_DESTINO_FINAL_PUBLICO |   IN_LIXO_DESCARTA_OUTRA_AREA |   IN_TRATAMENTO_LIXO_SEPARACAO |   IN_TRATAMENTO_LIXO_REUTILIZA |   IN_TRATAMENTO_LIXO_RECICLAGEM |   IN_TRATAMENTO_LIXO_INEXISTENTE |
|:--------------|------------------:|-----------------------:|-------------------------:|------------------:|--------------------:|----------------------:|--------------------------:|----------------------------:|-----------------------:|-------------------------:|-------------------------:|--------------------------:|------------------------:|------------------:|------------------------:|-------------------------:|-----------------:|------------------:|--------------------------------:|------------------------------:|-------------------------------:|-------------------------------:|--------------------------------:|---------------------------------:|
| MINIMO        |            539    |                 269    |                    67    |             6     |               2     |                 0     |                    579    |                      0      |                 5      |                    0     |                    96    |                     85    |                   37    |            122    |                   0     |                   361    |             9    |             2     |                           3     |                         2     |                         135    |                         62     |                           65    |                           657    |
| MAXIMO        |          29919    |               29089    |                  4489    |          2276     |            2168     |               987     |                  29933    |                    805      |               307      |                 1175     |                 28440    |                   5176    |                 5132    |           8537    |                1564     |                 13948    |          6513    |           680     |                       21434     |                      2517     |                       10785    |                       2848     |                         6367    |                         16558    |
| MEDIA         |           6302.59 |                5028.59 |                  1031.78 |           592.741 |             261.148 |               131.963 |                   6399.74 |                     72.8889 |                70.3333 |                  120.556 |                  3756    |                   1493.44 |                 1188.67 |           2682.11 |                 280.185 |                  4676    |          1183.48 |           154.926 |                         893.037 |                       197.444 |                        2744.78 |                        886.148 |                         1312.89 |                          4798.63 |
| MEDIANA       |           4434    |                2856    |                   689    |           233     |              83     |                21     |                   4267    |                      9      |                54      |                    5     |                  1359    |                   1289    |                  750    |           2007    |                  75     |                  2933    |           395    |            73     |                          52     |                        43     |                        1347    |                        667     |                          710    |                          3032    |
| DESVIO PADRAO |           6359.26 |                6030.44 |                  1103.96 |           671.51  |             489.716 |               246.049 |                   6448.36 |                    197.031  |                68.6995 |                  285.519 |                  5867.65 |                   1142.98 |                 1321.03 |           2303.03 |                 472.916 |                  3904.65 |          1719.31 |           170.147 |                        4107.43  |                       482.905 |                        2767.93 |                        760.756 |                         1393.73 |                          4570.02 |

Analisando, inicialmente, a quantidade de escolas (por região e por estado) que recebem água potável, temos as seguintes situações:

- Por regiões:

![](imagens/11.png)

- Por estados:

![](imagens/12.png)

Observa-se que há uma enorme quantidade de escolas em São Paulo que recebem água potável em relação ao demais estados (cerca de 30000), elevando assim a quantidade de escolas que recebem água potável na Região Sudeste, conforme ocorre nos gráficos acima. Além disso, Minas Gerais e Rio de Janeiro também contribuem fortemente para essa quantidade. Em seguida, vemos o Nordeste em segunda posição, com água potável em maior quantidade em escolas da Bahia, Maranhão e Pernambuco (todos abaixo de 15000). Por fim, vê-se que as três regiões restantes encontram-se em menor quantidade, mas isto não significa que elas tem menos em proporção, pois devemos levar em conta a extensão terriorial (muito rebaixada no Sul e no Centro-Oeste) e a quantidade de escolas existentes (muito rebaixada no Norte e no Centro-Oeste).

Analisando agora, a quantidade de escolas (por região e por estado) que recebem água, energia e possuem esgoto e tratamento de lixo de caráter dado pela rede pública, temos as seguintes situações:

- Por regiões:

![](imagens/21.png)

- Por estados:

![](imagens/22.png)

Novamente, observamos São Paulo com forte destaque em todos os quesitos (cerca de 30000, o que indica que provavelmente são os mesmos locais), com acompanhamento considerável de Minas Gerais e Rio de Janeiro. A Região Nordeste, ganhando destaque nesses quesitos graças a Bahia, Pernambuco e Maranhão e as demais regiões sem consideráveis posições, valendo a observação mencionada anteriormente. Ademais, convém mencionar a forte expressividade de São Paulo no quesito de escolha do destino final do lixo por meio do poder público.

A fim de analisar a ausência desses recursos para entender se, de fato, as regiões menos expressivas estão de fato em condições precárias no ambiente de ensino, temos as seguintes situações:

- Por regiões:

![](imagens/31.png)

- Por estados:

![](imagens/32.png)

Nesse caso, a Região Sudeste perde a expressividade, exceto no tratamento de lixo, onde vemos que a quantidade de escolas que não tem tratamento do lixo é relativamente alta (principalmente em São Paulo, mas também em Minas Gerais e Rio de Janeiro). A Região Nordeste tem também diversas escolas sem abastecimento de água, sem esgoto e sem tratamento de lixo, muito frequentes na Bahia e Maranhão. A Região Norte também demonstra ter muitas escolas sem água, energia e esgoto (principalmente no Amazonas, no Pará e no Acre), que deve ocorrer por diversos fatores, que podem ser geograficos, economicos ou mesmo historico-sociais. Por fim, as regiões Centro-Oeste e Sul se mantém em valores baixos, o que indica uma baixa quantidade de escolas sem algum destes indicadores, caracterizando um grau de desenvolvimento, já que em proporção há bem mais escolas com esses indicadore do que sem.

Analisando agora meios alternativos de abastecimento de água e energia nas escolas, além de tipos diferentes de esgoto e tratamento de lixo nas escolas, temos as seguintes situações:

- Por regiões:

![](imagens/41.png)

- Por estados:

![](imagens/42.png)

Nesse caso, observa-se que tanto o Nordeste e o Norte ganham destaque (com o Sudeste acima da média no caso da energia renovável). Temos um domínio sobre abastecimento com poço artesiano e energia renovável em ambos, água de cacimba e esgoto dos três tipos de fossa apresentados no caso do Nordeste e água proveniente do rio (Rio Amazonas) e energia vinda de gerador fóssil no Norte.

Analisando os tipos de tratamento de lixo que ocorrem nas escolas, temos as seguintes situações:

- Por regiões:

![](imagens/51.png)

- Por estados:

![](imagens/52.png)

Quanto ao tratamento do lixo, temos uma distribuição razoavelmente equilibrada entre as regiões Nordeste (novamente, Bahia, Maranhão, Pernambuco e Paraíba), Sudeste (domínio de Minas Gerais na coleta, São Paulo na separação e reciclagem e Rio de Janeiro na reutilização) e Sul (principalmente Santa Catarina e Rio Grande do Sul). Novamente, temos uma baixa expressividade do Norte e do Centro-Oeste.

Analisando os tipos alternativos de destinos finais do lixo, temos as seguintes situações:

- Por regiões:

![](imagens/61.png)

- Por estados:

![](imagens/62.png)

Temos baixa expressividade do Sudeste, Centro-Oeste e Sul, forte presença do Nordeste (com Bahia e Maranhão), bem como do Norte, na queima do lixo e do Norte (com Amazonas e Pará) no enterramento e no descarte em outros áreas.

Em resumo, nota-se que a região Centro-Oeste não tem resultados acima da média nos quesitos acima, o que não indica necessariamente algo ruim, já que também está abaixo da média em quantidade de escolas que não possuem água, energia, esgoto ou tratamento de lixo. Vemos o Sul de forma neutra, com dados aparentemente bons em proporção, o Norte com alguns pros e alguns contras (sendo o foco: Amazonas, Pará e Acre), Nordeste com muita expressividade (sendo o foco: Bahia, Maranhão e Pernambuco) e o Sudeste com os mais diversos bons indicadores, indicando um alto desenvolvimento em relação ao país (sendo o foco: São Paulo).

## ANÁLISE CORRELATIVA

Agora, vamos analisar a correlação entre cada um dos indicadores e o tipo de localização em que as escolas se encontram (urbana e rural) ou localização diferenciada (assentamentos, terras indígenas e remanescentes de quilombos) e o tipo de dependência escolar (federal, estadual, pública e privada), a fim de inferir como ocorre a proporção em cada um destes.

![](imagens/71.png)
![](imagens/72.png)
![](imagens/73.png)

## IDEIAS ADICIONAIS

Analisando a base de dados (principalmente do ponto de vista de municípios e escolas - colunas NO_MUNICIPIO e NO_ENTIDADE, respectivamente - que não foram utilizados no dataframe para as análises, já que as mesmas se limitaram a uma visão global por regiões ou estados), observa-se que podemos associar a cada linha, um vetor, onde cada coordenada representa um dos indicadores ecológicos em questão. A fim de encontrar cidades (ou mesmo escolas) que são semelhantes de um modo geral nesses indicadores, devemos efetuar a distância entre cada um dos vetores agrupá-las em grupos (clusters) que indiquem que elas são similares entre si. Entretanto, isso seria um trabalho um pouco demorado (foram feitos alguns testes e o código demorou horas e não terminou de rodar). Pesquisei sobre isso e descobri que há bibliotecas em python que fazem esse agrupamento (ou clusterização), como a função kmeans presente na biblioteca sklearn. Mas, pelo tempo escasso para entender essa biblioteca e por recomendações externas de não utilizar ela pois esse tema seria visto em um curso futuro (pelo menos em Ciência de Dados) de Aprendizado de Máquina, resolvi me abster e ficar apenas com a motivação. Mas pretendo pesquisar mais a fundo em detalhes sobre essa ideia.

