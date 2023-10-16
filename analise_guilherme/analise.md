# Análise Guilherme

## Análise de Acessibilidade na Educação Básica

O objetivo principal desta análise é avaliar a situação da acessibilidade nas escolas de educação básica com base em dados do governo. Foi obtido um conjunto de dados do governo (https://dados.gov.br/) contendo informações sobre escolas de educação básica, que inclui detalhes sobre a acessibilidade.

Os dados foram carregados em um DataFrame utilizando a biblioteca Pandas, facilitando a manipulação e análise. Em seguida, as colunas relacionadas à acessibilidade foram filtradas, criando um novo DataFrame que continha apenas essas informações.

Realizou-se uma análise descritiva das colunas de acessibilidade. Um gráfico de barras foi criado para ilustrar a situação da acessibilidade nas escolas. No eixo y, as diferentes categorias ou métricas de acessibilidade foram representadas, e no eixo x, foram representados os valores correspondentes. Ademais, é possível observar que existe uma ordenação para as colunas de acessibilidade: Primeiro "inexistente" representando a quantidade de escolas sem nenhum tipo de adaptação ou acessibilidade, segundo grupo formado por "Sinal tátil, pisos táteis e sinal sonoro" representando acessibilidade para deficientes visuais, terceiro grupo "Sinal Visual" que mostra a quantidade de escolas com adaptações para deficiente auditivo, e por último as colunas restantes representando acessibilidade para deficientes com mobilidade reduzida.
![](analise_guilherme/acessibilidade.png)

Com base na análise e na visualização, foram identificados os seguintes insights:
- Em 28,7% das escolas ainda não existe **nenhum tipo** de adaptação para pessoas com deficiência.
- Em pelo menos 7,3% das escolas existem algum tipo de adaptação para **deficiência visual**.
- Em 6,6% das escolas analisadas já possuem acessibilidade para **deficiência auditiva**.
- Em 41,2% já possuem pelo menos uma adaptação para **deficiência física**.

Sendo assim, em 71,2% das instituições já estão presentes algum tipo de adaptação para pessoas com deficiência, um número que pessoalmente me surpreendeu. Mas considerando os números individualmente, como por exemplo, deficiências visuais e auditivas, são dados que ainda precisam aumentar.
