# Task 1: Accept user input to create a list of integers and compute their sum
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert input to integers
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)

# Task 2: Create a tuple containing the names of five favorite books and print them using a loop
favorite_books = ("the alchemist", "subtle art of not giving a f*ck", "the prophet", "5am club", "becoming")
print("List of favorite books:")
for book in favorite_books:
    print(book)

# Task 3: Use a dictionary to store information about a person and print the dictionary
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Information about the person:")
print(person)

# Task 4: Accept user input to create two sets of integers and find their intersection
set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
set2 = set(input("Enter integers for set 2 separated by spaces: ").split())
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)

# Task 5: Use list comprehension to filter words with odd number of characters
words = ["apple", "banana", "orange", "pear", "grape"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
