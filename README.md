## Projeto MLOps de Detecção de Anomalias

Este projeto implementa um pipeline MLOps de ponta a ponta para detectar anomalias em dados de séries temporais. O sistema é automatizado, versionado e implantado na nuvem, usando boas práticas em Engenharia de Machine Learning.

## Problema
O objetivo deste projeto é detectar anomalias de ponto em dados de utilização de CPU de um servidor em nuvem. A detecção precoce é crucial para a manutenção da saúde e segurança do sistema.

## Dataset
O projeto utiliza o dataset [`ec2_cpu_utilization_24ae8d.csv`](https://github.com/numenta/NAB) fornecido pela Numenta Anomaly Benchmark (NAB).

## Baseline
A abordagem inicial utiliza um modelo IsolationForest do scikit-learn. Este é um algoritmo de detecção de anomalias não supervisionado e eficiente.

## Resultados Iniciais:

![Modelo com desempenho baixo — excesso de detecções irrelevantes](https://raw.githubusercontent.com/o-brn/anomaly-detection-mlops/main/docs/images/anonewplot.png)


## Convenção de Commits

Este projeto usa a [Commits Convencionais](https://www.conventionalcommits.org/en/v1.0.0/), com o propósito de obter um histórico de commits legíveis e que facilitem alterações futuras. Abaixo seguem os tipos mais comuns utilizados:

| Tipo     | Título                 | Descrição                                                                   |
|----------|------------------------|-----------------------------------------------------------------------------|
| feat     | Features               | Nova funcionalidade.                                                        |
| fix      | Correções de Bugs      | Correção de bug.                                                            |
| docs     | Documentação           | Alterações apenas na documentação.                                          |
| style    | Estilos                | Alterações de estilo de código.                                             |
| refactor | Refatoração de Código  | Alteração de código que não corrige um bug nem adiciona uma funcionalidade. |
| perf     | Desempenho             | Uma alteração de código que melhora o desempenho.                           |
| test     | Testes                 | Adicionando ou corrigindo testes.                                           |
| build    | Sistema de Build       | Alterações no sistema de build ou dependências.                             |
| ci       | CI/CD                  | Alterações nos arquivos e scripts de CI/CD.                                 |
| chore    | Tarefas                | Outras alterações que não modificam os arquivos src ou test.                |