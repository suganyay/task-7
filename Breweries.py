import requests

# Base URL for the OpenBreweryDB API
base_url = "https://api.openbrewerydb.org/breweries"
states = ["Alaska", "Maine", "New York"]

# Fetch and display breweries for each state
print("\nBreweries in specified states:")
for state in states:
    response = requests.get(f"{base_url}?by_state={state}")
    if response.status_code == 200:
        breweries = response.json()
        print(f"\n{state}:")
        for brewery in breweries:
            print(brewery.get('name', 'Unknown'))
    else:
        print(f"Failed to fetch breweries for {state}")

# Count breweries in each state
print("\nNumber of breweries in each state:")
for state in states:
    response = requests.get(f"{base_url}?by_state={state}")
    if response.status_code == 200:
        breweries = response.json()
        print(f"{state}: {len(breweries)}")
    else:
        print(f"Failed to fetch breweries for {state}")

# List breweries with websites
print("\nBreweries with websites:")
for state in states:
    response = requests.get(f"{base_url}?by_state={state}")
    if response.status_code == 200:
        breweries = response.json()
        print(f"\n{state}:")
        for brewery in breweries:
            website = brewery.get('website_url')
            if website:
                print(f"{brewery.get('name', 'Unknown')}: {website}")
    else:
        print(f"Failed to fetch breweries for {state}")