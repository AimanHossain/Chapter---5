# Create a dictionary to store information about rivers and the countries they run through
rivers = {
    # Set the key 'nile' to the value 'Egypt'
    'nile': 'Egypt',
    # Set the key 'amazon' to the value 'Brazil'
    'amazon': 'Brazil',
    # Set the key 'yangtze' to the value 'China'
    'yangtze': 'China'
}

# Print a sentence about each river
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())
