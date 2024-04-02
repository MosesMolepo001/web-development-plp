import json
from difflib import get_close_matches

# Load JSON data into a Python dictionary
with open("C:/Users/moses/OneDrive/Desktop/Web development plp/python/week4/miniChallenge/data.json", "r") as file:
    data = json.load(file)

# Function to get definition of a word
def get_definition(word):
    word = word.lower()  # Convert input to lowercase
    if word in data:
        return data[word]
    elif word.title() in data:  # Check for title case (capitalize first letter)
        return data[word.title()]
    elif word.upper() in data:  # Check for uppercase
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:  # Check for similar words
        suggested_word = get_close_matches(word, data.keys())[0]
        response = input(f"Did you mean '{suggested_word}' instead? Enter Y if yes, or N if no: ")
        if response.lower() == 'y':
            return data[suggested_word]
        else:
            return "The word doesn't exist. Please double check it."
    else:
        return "The word doesn't exist. Please double check it."

# Prompt user input and display definition
word = input("Enter a word: ")
definition = get_definition(word)
if isinstance(definition, list):
    for meaning in definition:
        print("-", meaning)
else:
    print(definition)
