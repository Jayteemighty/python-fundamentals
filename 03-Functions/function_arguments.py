# Functions can accept arguments to work with data. There are several ways to pass arguments:

# 1. Positional arguments: arguments are passed in the order they are defined in the function
def substract(a, b):
    return a - b
print(substract(650 - 90)) # Output: 590

# 2. Keywords arguments: Arguments are passed by name, not position
def describe_person(name, age):
    print(print(f"{name} is {age} years old"))

describe_person(age=30, name="Bob") # Output: Bob is 30 years old

# 3. Default Arguments: You can specify default values for parameters. If no argument is provided, the default is used.
def greet(name="stranger"):
    print(f"Hello, {name}!")

greet()             # Output: Hello, stranger!
greet("Adesina")    # Output: Hello, Adesina!


# 4. Variable-length arguments:

# *args: Allows a function to accept any number of positional arguments.
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # Output: 10

# **kwargs: Allows a function to accept any number of keyword arguments.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, job="Engineer")
