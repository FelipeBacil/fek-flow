# FEK — Fengbir Engineering Kernel

Kernel de engenharia especializado em implementos rodoviários, estruturas
soldadas, automação CAD/CAE e preparação de modelos para simulação.

## Princípio arquitetural

O FEK permanece desacoplado do site Fengbir. O site consome somente dados
publicados pelo FEK por meio de arquivos de exportação versionados.

## Integração inicial com o site

Fonte oficial:

`management/activity-index.json`

Arquivo de consumo do dashboard:

`management/exports/fek-dashboard.json`
