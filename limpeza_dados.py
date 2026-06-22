import pandas as pd
import os

# 1. Definir o nome do arquivo que você baixou
arquivo_bruto = "global-data-on-sustainable-energy (1).csv"
arquivo_limpo = "energy_data_europe.csv"

print("🚀 Iniciando a automação de limpeza de dados...")

# Verificar se o arquivo realmente está na pasta
if not os.path.exists(arquivo_bruto):
    # Caso o nome tenha vindo um pouco diferente, tenta achar qualquer CSV na pasta
    arquivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]
    if arquivos_csv:
        arquivo_bruto = arquivos_csv[0]

# 2. Carregar os dados usando o Pandas
df = pd.read_csv(arquivo_bruto)

# 3. Filtrar apenas os países da Europa (Foco no Mercado Europeu)
# Criamos uma lista com os principais países europeus presentes no dataset
paises_europeus = [
    'Germany', 'France', 'United Kingdom', 'Italy', 'Spain', 'Netherlands', 
    'Belgium', 'Sweden', 'Poland', 'Norway', 'Austria', 'Denmark', 'Finland', 
    'Portugal', 'Greece', 'Ireland', 'Switzerland', 'Czechia', 'Romania'
]
df_europa = df[df['Entity'].isin(paises_europeus)].copy()

# 4. Tratamento de Dados (Data Wrangling Avançado)
# Substituir valores vazios (NaN) por 0 nas colunas numéricas para não quebrar o SQL
colunas_numericas = df_europa.select_dtypes(include=['float64', 'int64']).columns
df_europa[colunas_numericas] = df_europa[colunas_numericas].fillna(0)

# Renomear as colunas para facilitar a escrita das queries no SQL amanhã (remover espaços e caracteres especiais)
df_europa.rename(columns={
    'Entity': 'country',
    'Year': 'year',
    'Access to electricity (% of population)': 'access_electricity_pct',
    'Renewable-electricity-generating-capacity-per-capita': 'renewable_capacity_per_capita',
    'Financial flows to developing countries (US $)': 'financial_flows',
    'Renewable energy share in the total final energy consumption (%)': 'renewable_share_pct',
    'Electricity from fossil fuels (TWh)': 'electricity_fossil_twh',
    'Electricity from nuclear (TWh)': 'electricity_nuclear_twh',
    'Electricity from renewables (TWh)': 'electricity_renewables_twh',
    'Low-carbon electricity (% electricity)': 'low_carbon_electricity_pct',
    'Primary energy consumption per capita (kWh/person)': 'energy_consumption_per_capita',
    'Energy intensity level of primary energy (MJ/$2017 PPP GDP)': 'energy_intensity',
    'Value_co2_emissions_metric_tons_per_capita': 'co2_per_capita',
    'Renewables (% equivalent primary energy)': 'renewables_pct_primary'
}, inplace=True)

# 5. Exportar o arquivo final perfeitamente limpo
df_europa.to_csv(arquivo_limpo, index=False)

print(f"✅ Sucesso! O arquivo filtrado e limpo foi salvo como: {arquivo_limpo}")
print(f"📊 Total de registros processados da Europa: {len(df_europa)} linhas.")