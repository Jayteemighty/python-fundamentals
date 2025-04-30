"""
MODULES AND LIBRARIES
Organizing code into reusable modules and leveraging Python's extensive library ecosystem.

Definitions:
1. MODULE: A single Python file (.py) containing reusable code (functions, classes, variables)
   - Example: 'math.py' is a built-in module for mathematical operations

2. LIBRARY: A collection of modules/packages that provide specific functionality
   - Example: 'requests' library for HTTP operations (made of multiple .py files)

3. PACKAGE: A directory containing multiple modules and an __init__.py file
   - Example: 'urllib' package (contains request.py, response.py, etc.)

4. PYPI: Python Package Index - repository of third-party libraries (pip installs from here)
"""

# ==============================================================================
# 1. IMPORTING BUILT-IN MODULES
# ==============================================================================
# Standard library imports
import math
from datetime import datetime
import os
import sys

# Using math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi constant: {math.pi:.3f}")

# Using datetime
now = datetime.now()
print(f"Current date/time: {now:%Y-%m-%d %H:%M:%S}")

# Using os and sys
print(f"Current working directory: {os.getcwd()}")
print(f"Python version: {sys.version[:5]}")


# ==============================================================================
# 2. CREATING AND USING CUSTOM MODULES
# ==============================================================================
# Create these files in the same directory:
# File: my_utils.py
"""
def greet(name):
    return f"Hello, {name}!"

def calculate_circle_area(radius):
    return math.pi * radius ** 2
"""

# Importing custom module
import my_utils

print(my_utils.greet("Alice"))
print(f"Area of circle: {my_utils.calculate_circle_area(3):.2f}")


# ==============================================================================
# 3. THIRD-PARTY LIBRARIES (PIP)
# ==============================================================================
# Common installation command: pip install package_name

# Example with requests (install first: pip install requests)
try:
    import requests
    response = requests.get("https://api.github.com")
    print(f"\nGitHub API status: {response.status_code}")
except ImportError:
    print("Requests library not installed. Run: pip install requests")


# ==============================================================================
# 4. VIRTUAL ENVIRONMENTS
# ==============================================================================
"""
Best Practice: Always use virtual environments for project-specific dependencies

# Create virtual environment:
python -m venv myenv

# Activate (Windows):
myenv\Scripts\activate

# Activate (Mac/Linux):
source myenv/bin/activate

# Install packages:
pip install package_name

# Freeze requirements:
pip freeze > requirements.txt

# Install from requirements:
pip install -r requirements.txt
"""


# ==============================================================================
# 5. POPULAR LIBRARY CATEGORIES
# ==============================================================================
# Web Development: Flask, Django
# Data Science: pandas, numpy, matplotlib
# Machine Learning: tensorflow, scikit-learn
# GUI: tkinter, PyQt
# Games: pygame

# Example with pandas (install first: pip install pandas)
try:
    import pandas as pd
    data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
    df = pd.DataFrame(data)
    print("\nPandas DataFrame:")
    print(df)
except ImportError:
    print("Pandas not installed. Run: pip install pandas")


# ==============================================================================
# 6. ALIASING IMPORTS
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt

# Example NumPy array
arr = np.array([1, 2, 3])
print(f"\nNumPy array: {arr}")


# ==============================================================================
# 7. IMPORTING SPECIFIC FUNCTIONS
# ==============================================================================
from collections import Counter, defaultdict
from math import factorial, log2

print(f"Factorial of 5: {factorial(5)}")
print(f"Log2 of 8: {log2(8)}")

word_counts = Counter(["apple", "banana", "apple"])
print(f"Word counts: {word_counts}")


# ==============================================================================
# 8. PACKAGE STRUCTURE
# ==============================================================================
"""
Example package structure:

my_package/
├── __init__.py
├── module1.py
└── subpackage/
    ├── __init__.py
    └── module2.py
"""


# ==============================================================================
# 9. RELATIVE IMPORTS (FOR PACKAGES)
# ==============================================================================
# Inside a package, you can use:
# from .module1 import function1
# from ..parent_package.module import function


# ==============================================================================
# 10. BEST PRACTICES
# ==============================================================================
"""
1. Organize related code into modules
2. Use descriptive module names (avoid single-letter names)
3. Document modules with docstrings
4. Use virtual environments
5. Specify dependencies in requirements.txt
6. Follow PEP 8 style guide for imports:
   - Standard library imports first
   - Third-party libraries next
   - Local application imports last
"""


# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a custom module with math utilities (fibonacci, prime check)
# 2. Install and test a new library (e.g., rich for console formatting)
# 3. Build a package with multiple modules and subpackages