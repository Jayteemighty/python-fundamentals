# A function is a reusable block of code that performs a specific task.
# Instead of writing the same code repeatedly, you can define a function and call it whenever needed.

def function_name(parameters_or_arguments):
    """
    Optional docstring: explains what the function does.
    """
    # Function body
    return # optional

# Example 1
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# Example 2
def greet_user(name):
    print(f"Hello, {name}")

greet_user("anthony")

# Example 3
def add_numbers(a, b):
    return a + b

add_numbers(11, 13)