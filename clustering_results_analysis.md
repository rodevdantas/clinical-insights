# Segmentação de Pacientes com Clustering e PCA
Todos os dados são artificiais e foram criados exclusivamente para fins educacionais e de portfólio.

## Descrição

Este documento apresenta os resultados da etapa de **clusterização de pacientes** com base em suas características demográficas e de plano de saúde. A análise foi realizada utilizando o algoritmo KMeans, com dados fictícios gerados previamente.


## Objetivo da Clusterização

Agrupar pacientes com perfis semelhantes, utilizando as seguintes variáveis:

- Idade
- Sexo 
- Plano de saúde 

O objetivo principal é identificar padrões ocultos que possam ser úteis para:

- Segmentação estratégica
- Personalização de serviços
- Análise exploratória da base de pacientes


## Etapas Realizadas

### 1. Pré-processamento

- Conversão da data de nascimento em idade.
- Padronização das variáveis numéricas com **StandardScaler**.
- Codificação das variáveis categóricas.

### 2. Escolha do Número de Clusters

- O método do cotovelo (Elbow Method) foi utilizado para avaliar a variação da inércia entre diferentes valores de k (de 1 a 10).
- Foi identificado um ponto de inflexão evidente em k=4, sendo este o valor utilizado na clusterização.

### 3. Resultados dos Clusters

Após aplicação do algoritmo com k = 4, obteve-se a seguinte média dos atributos por cluster:

| Cluster | Idade Média | Sexo (0=Fem, 1=Masc) | Plano de Saúde (0=Popular, 1=Executivo, 2=Premium) |
|---------|-------------|---------------|--------------|
| 0       | 70.20       | 1.00          | 0.25         |
| 1       | 26.91       | 1.00          | 0.20         |
| 2       | 48.54       | 0.22          | 1.48         |
| 3       | 48.52       | 0.00          | 0.00         |

**Interpretação dos Grupos:**

- **Cluster 0:** Homens idosos com predominância do plano Popular.
- **Cluster 1:** Homens jovens com predominância do plano Popular.
- **Cluster 2:** Majoritariamente mulheres de meia idade com predominância de planos Premium e Executivo.
- **Cluster 3:** Mulheres de meia idade apenas com plano Popular.

### 4. Visualizações

- Gráfico do Elbow Method para justificativa do k.
- Boxplot para a variável Idade por cluster.
- Countplots para as variáveis Sexo e Planos por cluster.


## Conclusões

A clusterização foi eficaz em agrupar pacientes com características similares, revelando perfis que podem ser explorados para decisões estratégicas. Essa segmentação também pode ser integrada a análises futuras, como predição de adesão a planos ou detecção de padrões de comportamento por grupo.

A análise de clusters possibilitou a descoberta de **quatro perfis distintos** entre os pacientes da clínica. Essa segmentação pode ser usada como base para:

- Estratégias de atendimento e comunicação direcionadas
- Análise de distribuição dos planos de saúde por perfil
- Priorização de recursos com base nos grupos mais relevantes

Este processo não visa prever doenças ou comportamentos diretamente, mas agrupar indivíduos com características semelhantes, permitindo futuras análises mais profundas ou aplicações com modelos supervisionados.


## Visualização com PCA

Para facilitar a interpretação dos clusters formados, apliquei a técnica de Análise de Componentes Principais (PCA), reduzindo a dimensionalidade dos dados de três variáveis (idade, sexo, plano_saude) para dois componentes principais (PCA1 e PCA2).

O objetivo principal foi gerar uma visualização bidimensional dos agrupamentos identificados pelo algoritmo KMeans, sem perder a variabilidade essencial dos dados.

O gráfico resultante mostrou que os clusters estão nitidamente separados entre si, com baixa sobreposição, o que valida visualmente a segmentação proposta.

Essa etapa agregou valor à análise ao permitir:

- Validar visualmente a separação entre os clusters
- Reforçar a qualidade do agrupamento proposto
- Fornecer uma base visual para futuras decisões estratégicas ou análises aprofundadas

A visualização por PCA reforçou a validade dos clusters e facilitou a comunicação dos resultados, encerrando esta etapa com uma representação clara e interpretável.
