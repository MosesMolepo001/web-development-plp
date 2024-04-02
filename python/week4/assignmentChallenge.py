class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, your details are {self.name}. I am {self.age} years old and I am {self.gender}.")

# Accept input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

# Create an instance of the Person class with user input
person1 = Person(name, age, gender)

# Call the introduce method to display the person's information
person1.introduce()
