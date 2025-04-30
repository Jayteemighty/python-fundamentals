"""
CLASSES AND OBJECTS (OOP)
Classes are blueprints for creating objects with shared attributes and methods.
"""

# ==============================================================================
# 1. DEFINING A CLASS
# ==============================================================================
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (__init__ method)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"


# ==============================================================================
# 2. CREATING OBJECTS (INSTANTIATION)
# ==============================================================================
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

print(dog1.name)  # Output: Buddy
print(dog2.bark())  # Output: Milo says woof!
print(dog1.species)  # Output: Canis familiaris


# ==============================================================================
# 3. CLASS METHODS VS STATIC METHODS
# ==============================================================================
class Cat:
    def __init__(self, name):
        self.name = name

    # Regular instance method (requires self)
    def meow(self):
        return f"{self.name} says meow!"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Alternative constructor
        age = 2023 - birth_year
        return cls(name, age)

    @staticmethod
    def is_cat_purring(sound):
        # No access to self/cls
        return "purr" in sound.lower()


# Usage:
cat1 = Cat("Whiskers")
cat2 = Cat.from_birth_year("Snowball", 2018)

print(cat1.meow())  # Output: Whiskers says meow!
print(cat2.age)  # Output: 5 (assuming current year is 2023)
print(Cat.is_cat_purring("Purr..."))  # Output: True


# ==============================================================================
# 4. INHERITANCE
# ==============================================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


class Lion(Animal):
    def speak(self):
        return f"{self.name} roars!"


class Mouse(Animal):
    def speak(self):
        return f"{self.name} squeaks!"


# Polymorphism in action
animals = [Lion("Simba"), Mouse("Jerry")]
for animal in animals:
    print(animal.speak())
# Output:
# Simba roars!
# Jerry squeaks!


# ==============================================================================
# 5. SPECIAL (MAGIC/DUNDER) METHODS
# ==============================================================================
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Length implementation
    def __len__(self):
        return self.pages

    # Operator overloading (+)
    def __add__(self, other):
        return Book(
            title=f"{self.title} & {other.title}",
            author=f"{self.author} and {other.author}",
            pages=self.pages + other.pages
        )


# Usage
book1 = Book("Python 101", "John Doe", 200)
book2 = Book("OOP Basics", "Jane Smith", 150)

print(book1)  # Output: 'Python 101' by John Doe
print(len(book2))  # Output: 150
combined = book1 + book2
print(combined.title)  # Output: Python 101 & OOP Basics


# ==============================================================================
# 6. PROPERTIES (GETTERS/SETTERS)
# ==============================================================================
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Usage
temp = Temperature(25)
print(temp.fahrenheit)  # Output: 77.0
temp.celsius = 30  # Uses setter
print(temp.fahrenheit)  # Output: 86.0