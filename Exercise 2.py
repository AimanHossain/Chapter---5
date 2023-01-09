# Create a glossary to store programming terms and their meanings
glossary = {
    # Set the key 'variable' to the value 'A value that can change'
    'variable': 'A value that can change',
    # Set the key 'function' to the value 'A block of code that performs a specific task'
    'function': 'A block of code that performs a specific task',
    # Set the key 'loop' to the value 'A control flow statement that allows a block of code to be repeated multiple times'
    'loop': 'A control flow statement that allows a block of code to be repeated multiple times',
    # Set the key 'string' to the value 'A sequence of characters'
    'string': 'A sequence of characters',
    # Set the key 'list' to the value 'An ordered collection of values'
    'list': 'An ordered collection of values'
}

# Print each term and its meaning
for term, meaning in glossary.items():
    # Print the term and its meaning on separate lines
    print(term + ':\n' + meaning + '\n')
