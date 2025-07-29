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
