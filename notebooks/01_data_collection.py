import pandas as pd
import requests

# Getting CO2 emissions data for South Asian countries (Nepal, India, Bangladesh, Pakistan, Sri Lanka):
countries = ["NPL", "IND", "BGD", "PAK", "LKA"] # Nepal, India, Bangladesh, Pakistan, Sri Lanka

base_url = "http://api.worldbank.org/v2/country/" # World Bank API Url
country_codes = ";".join(countries)
print("Country codes:", country_codes)

indicator = "NY.GDP.MKTP.KD.ZG" # GDP growth (annual %)
full_url = base_url + country_codes + "/indicator/" + indicator + "?format=json&per_page=500"
print("Full URL:", full_url)


response = requests.get(full_url)
print("Status code:", response.status_code)

data = response.json()
print("Type of data:", type(data))
print("Length of data:", len(data))
print("First item:", data[0])
print("Second item:", data[1])

# Extracting the actual data (skipping the metadata)
actual_data = data [1]
print("Number of records:", len(actual_data))
print("First record:", actual_data[0])

unique_countries = set(record['country']['value'] for record in actual_data)
print("Countries we got:", unique_countries)
print("Number of records:", len(actual_data))

# Converting to pandas DataFrame for easier analysis
import pandas as pd

df= pd.DataFrame(actual_data)
print("\nDataFrame shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# Extracting the key information
df_clean = pd.DataFrame({
    'country': [record['country']['value'] for record in actual_data],
    'country_code': [record['countryiso3code'] for record in actual_data],
    'year': [int(record['date']) for record in actual_data],
    'gdp_growth': [record['value'] for record in actual_data]
})

print("\nCleaned data:")
print(df_clean.head())
print("\nCountries and their data counts:")
print(df_clean['country'].value_counts())

recent_data = df_clean[df_clean['year']>= 2020].sort_values(['country', 'year'])
print("\nRecent GDP Growth (2020-2024):")
print(recent_data.pivot(index='year', columns='country', values='gdp_growth'))

# CO2 indicator - CO2 emissions per capita
co2_indicator = "EN.ATM.CO2E.PC" # CO2 emissions per capita
co2_url = base_url + country_codes + "/indicator/" + co2_indicator + "?format=json&per_page=500"
print(f"\nGetting CO2 data from: {co2_url}")