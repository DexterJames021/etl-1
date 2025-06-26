import requests
import re
import array

# Comments in Python start with the '#' symbol.
# This is a single-line comment.

"""
This is a multi-line comment or docstring.
It can be used to describe modules, functions, classes, or code sections.
"""

# Example of a for loop in Python
for i in range(5):
    print(f"For loop iteration: {i}")

# Example of a while loop in Python
count = 0
while count < 5:
    print(f"While loop iteration: {count}")
    count += 1

# Example of an if-elif-else condition in Python
number = 7
if number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is less than 10")
    
# Example of a function in Python
def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"

# Calling the function
greeting = greet("Alice")
print(greeting)

# Examples of basic data types in Python

# Integer
my_int = 42
print(f"Integer: {my_int} (type: {type(my_int)})")

# Float
my_float = 3.14
print(f"Float: {my_float} (type: {type(my_float)})")

# String
my_str = "Hello, world!"
print(f"String: {my_str} (type: {type(my_str)})")

# Boolean
my_bool = True
print(f"Boolean: {my_bool} (type: {type(my_bool)})")

# List
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list} (type: {type(my_list)})")

# Tuple
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple} (type: {type(my_tuple)})")

# Set
my_set = {1, 2, 3}
print(f"Set: {my_set} (type: {type(my_set)})")

# Dictionary
my_dict = {"name": "Alice", "age": 30}
# 
# In Python, a dictionary is a built-in data type that stores key-value pairs.
# Each key in a dictionary must be unique and immutable (such as strings, numbers, or tuples).
# Values can be of any data type and can be duplicated.
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons.
# Example:
# my_dict = {"name": "Alice", "age": 30}
# You can access values by their keys, add new key-value pairs, or update existing ones.

# Example: Fetch data from a public API (JSONPlaceholder)
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print("Fetched data from API:", data)
else:
    print("Failed to fetch data from API. Status code:", response.status_code)
    
# Note: Ensure you have the 'requests' library installed to run the API example.

# To install the requests library, you can use pip:
# pip install requests
print(f"Dictionary: {my_dict} (type: {type(my_dict)})")

# Example of a class in Python
class Person:
    """A simple class to represent a person."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Method to introduce the person."""
        return f"My name is {self.name} and I am {self.age} years old."
    
# Creating an instance of the Person class
person = Person("Bob", 25)
print(person.introduce())

# Example of a simple list comprehension in Python
squares = [x**2 for x in range(10)]
print(f"Squares from 0 to 9: {squares}")


# Example of a simple try-except block for error handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")   
    
# Example of a simple generator function
def count_up_to(n):
    """Generator function to count up to n."""
    count = 1
    while count <= n:
        yield count
        count += 1
        
# Using the generator function
for number in count_up_to(5):
    print(f"Generator count: {number}") 
    
# Example of using a context manager to handle file operations
with open("example.txt", "w") as file:
    file.write("Hello, world!")
    
# Example of common string functions in Python

sample_str = "  Hello, Python World!  "

# Convert to uppercase
print(f"Uppercase: {sample_str.upper()}")

# Convert to lowercase
print(f"Lowercase: {sample_str.lower()}")

# Remove leading and trailing whitespace
print(f"Stripped: '{sample_str.strip()}'")

# Replace a substring
print(f"Replace 'Python' with 'Programming': {sample_str.replace('Python', 'Programming')}")

# Split the string into a list
print(f"Split by spaces: {sample_str.split()}")

# Find the position of a substring
print(f"Index of 'Python': {sample_str.find('Python')}")

# Check if the string starts with a substring
print(f"Starts with '  Hello': {sample_str.startswith('  Hello')}")

# Check if the string ends with a substring
print(f"Ends with 'World!  ': {sample_str.endswith('World!  ')}")


# Example of using regular expressions (regex) in Python

text = "The rain in Spain falls mainly in the plain."

# Find all words that start with 'S' or 's'
words_starting_with_s = re.findall(r'\b[Ss]\w*', text)
print(f"Words starting with 'S' or 's': {words_starting_with_s}")

# Replace all occurrences of 'ain' with '___'
replaced_text = re.sub(r'ain', '___', text)
print(f"Text after replacement: {replaced_text}")

# Check if the text contains the word 'plain'
match = re.search(r'plain', text)
if match:
    print(f"'plain' found at position: {match.start()}")
else:
    print("'plain' not found in the text.")
    
# Example of using an array in Python

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])
print(f"Array: {my_array} (type: {type(my_array)})")

# Access elements
print(f"First element: {my_array[0]}")

# Append an element
my_array.append(6)
print(f"Array after append: {my_array}")

# Remove an element
my_array.remove(3)
print(f"Array after removing 3: {my_array}")

