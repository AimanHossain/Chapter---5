# Create a list to store dictionaries of pets
pets = []

# Create a dictionary for a pet cat
cat = {
    # Set the key 'kind' to the value 'cat'
    'kind': 'cat',
    # Set the key 'owner' to the value 'Lateef'
    'owner': 'Lateef'
}
# Add the cat dictionary to the pets list
pets.append(cat)

# Create a dictionary for a pet dog
dog = {
    # Set the key 'kind' to the value 'dog'
    'kind': 'dog',
    # Set the key 'owner' to the value 'Gavin'
    'owner': 'Gavin'
}
# Add the dog dictionary to the pets list
pets.append(dog)

# Create a dictionary for a pet fish
fish = {
    # Set the key 'kind' to the value 'fish'
    'kind': 'fish',
    # Set the key 'owner' to the value 'Aiman'
    'owner': 'Aiman'
}
# Add the fish dictionary to the pets list
pets.append(fish)

# Loop through the pets list and print information about each pet
for pet in pets:
    print("Kind: " + pet['kind'])
    print("Owner: " + pet['owner'])

