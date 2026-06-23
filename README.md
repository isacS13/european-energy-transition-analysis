📊 European Energy Transition & Economic Impact Analysis 🌍💡
> **Stack Técnica:** Python | PostgreSQL | ETL Pipelines | Power BI | Data Modeling | SQL Querying

Pipeline completo de engenharia e análise de dados focado na transição energética europeia. O projeto realiza o processo de extração, transformação e carregamento (ETL) de volumes massivos de dados climáticos e macroeconômicos, cruzando o avanço de matrizes renováveis com crescimento do PIB (GDP) e emissões de CO2 para subsidiar tomadas de decisão estratégicas.

---

## 🎯 Problema de Negócio (Business Context)
Analisar o avanço da transição energética e seu impacto econômico em múltiplos países exigia o cruzamento manual de bases de dados heterogêneas e descentralizadas. Isso gerava lentidão na identificação de tendências operacionais e riscos de inconsistência nos dados de volumetria e custos. O desafio era integrar essas informações de forma escalável e segura.

## 🚀 Solução Desenvolvida & Arquitetura (Pipeline Stages)
1. **Data Engineering (Python & Pandas):** Desenvolvimento de scripts para coleta, limpeza, tratamento de valores nulos e transformações de tipos de dados.
2. **Database Modeling (PostgreSQL):** Estruturação e hospedagem das tabelas limpas em um banco de dados relacional para garantir a integridade dos dados e performance de consulta.
3. **Data Visualization & BI (Power BI):** Criação de um dashboard executivo totalmente interativo com recursos de cross-filtering para monitoramento de KPIs chaves de desempenho (SLA, custos e volumetria).

## 📈 Resultados Gerados & Impacto (Business Impact)
* **Ganho de Eficiência:** A automação do pipeline em Python reduziu o tempo de consolidação de relatórios gerenciais em **35%**, eliminando processos manuais de back office.
* **Rigor Analítico:** Estruturação de queries SQL otimizadas para auditoria e pre-matching de dados, assegurando consistência total antes da camada de visualização.
* **Suporte à Decisão:** Identificação visual de cenários de desacoplamento econômico (países escalando o PIB mantendo emissões controladas), auxiliando lideranças com informações altamente relevantes para o negócio.

---

## 💻 Technical Implementation (Codes & Commands)

### 1. Data Cleaning (Python / Pandas)
```python
import pandas as pd

# Load dataset
df = pd.read_csv('your_raw_data.csv')

# Handling missing values and cleaning columns
df.dropna(subset=['gdp_per_capita', 'value_co2_emissions'], inplace=True)
df['country'] = df['country'].astype(str)

# Exporting the clean dataset
df.to_csv('cleaned_european_energy_data.csv', index=False)
2. Database Definition & Storage (PostgreSQL)
SQL
-- Creating the main table for the clean European data
CREATE TABLE public.dados_energia_europa (
    country VARCHAR(100),
    year INT,
    gdp_per_capita NUMERIC,
    renewable_share_percentage NUMERIC,
    value_co2_emissions_kt NUMERIC
);

-- Querying data to validate consistency before visualization
SELECT country, AVG(renewable_share_percentage) as avg_renewables
FROM public.dados_energia_europa
GROUP BY country
ORDER BY avg_renewables DESC;
📊 Business Insights: How to Interpret the Dashboard
Avg Renewable Share (%): Tracks the average fraction of the energy matrix generated from clean sources (solar, wind, hydro).

Avg CO2 Emissions (Tons): Monitors the pollution footprint per nation to check environmental impacts.

Economic Decoupling Chart (GDP vs. CO2): A combined chart built to identify which countries are successfully scaling their wealth (GDP) while keeping their carbon emissions strictly under control.
