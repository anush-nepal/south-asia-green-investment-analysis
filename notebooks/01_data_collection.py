import pandas as pd
import requests

# Getting CO2 emissions data for South Asian countries (Nepal, India, Bangladesh, Pakistan, Sri Lanka):
countries = ["NPL", "IND", "BGD", "PAK", "LKA"] # Nepal, India, Bangladesh, Pakistan, Sri Lanka

base_url = "http://api.worldbank.org/v2/country/" # World Bank API Url
country_codes = ";".join(countries)
print("Country codes:", country_codes)

indicator = "NY.GDP.MKTP.KD.ZG" # GDP growth (annual %)
full_url = base_url + country_codes + "/indicator/" + indicator + "?format=json"
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