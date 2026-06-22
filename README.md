# European Energy Transition & Economic Impact Analysis 🌍💡

This repository contains an end-to-end data project developed to analyze the historical evolution of renewable energy shares across European countries, crossing this transition with economic growth (GDP) and carbon emissions ($CO_2$).

---

## 🛠️ Project Architecture & Tech Stack

The project was structured into four data pipeline stages:

1. **Data Extraction & Ingestion:** Historical climate and macroeconomic data consolidated from international datasets.
2. **Data Engineering (Python):** Data cleaning, type transformations, and handling of null/missing values using the **Pandas** library.
3. **Database Modeling (PostgreSQL):** Structuring and storing the cleaned tables into a relational database to ensure data integrity and performance.
4. **Data Visualization (Power BI):** Creation of an executive, fully interactive dashboard with cross-filtering features to extract insights easily.

---

## 💻 Technical Implementation (Codes & Commands)

### 1. Data Cleaning (Python / Pandas)
Below is the core logic used to process and clean the data tables:

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
The processed clean data was hosted in a PostgreSQL database using the following relational structure:

SQL-- Creating the main table for the clean European data

CREATE TABLE public.dados_energia_europa (country VARCHAR(100),
    year INT,
    gdp_per_capita NUMERIC,
    renewable_share_percentage NUMERIC,
    value_co2_emissions_kt NUMERIC);

-- Querying data to validate consistency before visualization
SELECT country, AVG(renewable_share_percentage) as avg_renewables
FROM public.dados_energia_europa
GROUP BY country
ORDER BY avg_renewables DESC;

##📊 Business Insights: How to Interpret the Dashboard

The visual analytics layer built in Power BI focuses on key executive metrics:

Avg Renewable Share (%): Tracks the average fraction
of the energy matrix generated from clean sources (solar, wind, hydro).

Avg $CO_2$ Emissions (Tons):
 Monitors the pollution footprint per nation to check environmental impacts.

Economic Decoupling Chart (GDP vs. $CO_2$):
 A combined chart built to identify which countries are successfully scaling their wealth (GDP)
while keeping their carbon emissions strictly under control.
