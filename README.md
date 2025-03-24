# etl-python-csv

Python ETL with data contract to validate CSV

**Tech:** python, git, pydantic, pandas, streamlit, ydata-profiling

## Agradecimentos

Agradecimentos especiais ao [@lvgalvao](https://github.com/lvgalvao) pelo conhecimento disponibilizado gratuitamente!

O projeto feito baseado na proposta da live [Pipeline ETL com Python: Validando Dados e Planilhas de Excel para BI (Projeto end-to-end!)
](https://youtu.be/JuOyNPjAer8).

O repo feito durante a live: [etl-python-excel-aovivo](https://github.com/lvgalvao/etl-python-excel-aovivo).

## Explicando o projeto e o desafio

- **O problema:** criar um *contrato de dados* agnóstico, que independe do output (locker, streamlit, powerbi, etc.)

![problema](/images/problema.png)

## Qual é a nossa motivação?

- **A motivação:** capacitar analistas, porque engenharia de dados dá mais dinheiro e proporcionaria qualidade de vida melhor

![motivacao](/images/motivacao.png)
 
# Projeto

## Planejando as etapas do projeto

1. Criar o projeto (10 minutos) - Github e o projeto Python  
2. Uma análise exploratória dos meus dados (20 minutos)
3. Explicação do Pydantic e do Pandora (30 minutos)
   - *(ferramentas de validação de dados em tempo real)*
4. Aplicação de validação (30 minutos)
5. Salvamento no banco de dados (30 minutos)

## Análise exploratória (Pandas Profiling)

- Instalar *ydata-profiling*
- `/src/profiling.py`

A análise exploratória do ydata-profiling está em [report.html](/output/report.html).

## Validação de dados

### Explicando as libs Pydantic e Pandera

- *pandera:* valida o dataset inteiro
- *pydantic:* valida cada linha como se fosse um objeto

Vamos utilizar o *pydantic* para firmar o contrato de dados.
No *pydantic*, definimos quais colunas e quais tipos de dados esperamos para cada uma (como um dict dtypes!).

### Aplicação da validação

O [validator.py](/src/validator.py) foi construído utilizando o arquivo [data.csv](/data/data.csv).
Para validar o validador, o csv [data_2025.csv](/data/data_2025.csv) foi utilizado.
Podemos verificar que o csv [data_2025-validated.csv](/data/data_2025.csv) atende ao contrato de dados. É o arquivo corrigido manualmente.
É importante notar que o validador apenas aponta os erros no arquivo, mas não os corrige.

## Estrutura básica do projeto

```bash
etl-python-excel/
├── data/
│   ├── data.csv                 # used to build the validator
│   ├── data_2025.csv            # used to test the validator
│   ├── data_2025-validated.csv  # corrected dataset after using the validator
│   └── people.csv               # example validator
├── output/
│   ├── report.html              # output profiling.py
│   └── ...
├── src/
│   ├── app.py                   # streamlit frontend + backend
│   ├── profiling.py             # análise exploratória
│   ├── validator-example.py
│   ├── validator.py             # modelo Pydantic + função validate_dataframe
│   └── ...
├── .gitignore
├── pyproject.toml
├── README.md
├── ...
```
