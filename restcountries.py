import requests

# Fetch data from the RestCountries API
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data")
    exit()

# Display countries with currencies and symbols
print("\nCountries and their currencies:")
for country in data:
    name = country.get('name', {}).get('common', 'Unknown')
    currencies = country.get('currencies', {})
    for code, currency_info in currencies.items():
        symbol = currency_info.get('symbol', 'N/A')
        print(f"{name}: {code} ({symbol})")

# Display countries using the Dollar as currency
print("\nCountries using Dollar as currency:")
for country in data:
    currencies = country.get('currencies', {})
    if 'USD' in currencies:
        print(country.get('name', {}).get('common', 'Unknown'))

# Display countries using the Euro as currency
print("\nCountries using Euro as currency:")
for country in data:
    currencies = country.get('currencies', {})
    if 'EUR' in currencies:
        print(country.get('name', {}).get('common', 'Unknown'))