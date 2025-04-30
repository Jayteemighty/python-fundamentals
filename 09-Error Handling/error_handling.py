"""
ERROR HANDLING (EXCEPTIONS)
Managing unexpected errors to prevent program crashes and provide useful feedback.
"""
from datetime import datetime
# ==============================================================================
# 1. BASIC TRY-EXCEPT BLOCK
# ==============================================================================
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling multiple exceptions
try:
    num = int("abc")
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {type(e).__name__} - {e}")


# ==============================================================================
# 2. ELSE AND FINALLY CLAUSES
# ==============================================================================
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"Result is {result}")  # Runs if no exception
    finally:
        print("Execution complete")  # Always runs

divide(10, 2)  # Result is 5.0 \n Execution complete
divide(10, 0)  # Division by zero! \n Execution complete


# ==============================================================================
# 3. CUSTOM EXCEPTIONS
# ==============================================================================
class InvalidAgeError(Exception):
    """Raised when age is negative or unrealistically high"""
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    if age > 120:
        raise InvalidAgeError("Age seems unrealistic!")
    return f"Age {age} is valid"

try:
    print(check_age(25))
    print(check_age(-5))
except InvalidAgeError as e:
    print(f"Invalid age: {e}")


# ==============================================================================
# 4. EXCEPTION HIERARCHY
# ==============================================================================
try:
    file = open("nonexistent.txt")
except OSError:  # Catches FileNotFoundError, PermissionError, etc.
    print("OS error occurred")


# ==============================================================================
# 5. ASSERTIONS
# ==============================================================================
def calculate_inverse(number):
    assert number != 0, "Number cannot be zero!"
    return 1 / number

try:
    print(calculate_inverse(5))
    print(calculate_inverse(0))
except AssertionError as e:
    print(f"Assertion failed: {e}")


# ==============================================================================
# 6. LOGGING EXCEPTIONS
# ==============================================================================
import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR)

try:
    import non_existent_module # This will deliberately fail
except ImportError as e:
    logging.error(f"Import error at {datetime.now()}: {e}", exc_info=True)
    print("Module not found - check errors.log for details")


# ==============================================================================
# 7. REAL-WORLD EXAMPLE: FILE VALIDATION
# ==============================================================================
def process_file(filename):
    try:
        with open(filename) as file:
            content = file.read()
            if not content:
                raise ValueError("File is empty")
            return content
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except PermissionError:
        print(f"Error: No permission to read {filename}")
    except UnicodeDecodeError:
        print(f"Error: Could not decode {filename}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")
    else:
        print("File processed successfully")
    finally:
        print(f"Attempted to process {filename}")

process_file("valid.txt")
process_file("missing.txt")
process_file("/root/protected.txt")


# ==============================================================================
# 8. BEST PRACTICES
# ==============================================================================
"""
1. Be specific with exception types (don't use bare except:)
2. Create custom exceptions for your application logic
3. Include cleanup code in finally blocks
4. Log exceptions with context (use logging module)
5. Don't suppress exceptions unless absolutely necessary
6. Use assertions for debugging, not for regular error handling
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a function that validates email format (raise custom exception if invalid)
# 2. Write a number parser that handles various invalid inputs gracefully
# 3. Implement a context manager that logs all exceptions