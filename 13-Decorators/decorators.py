"""
DECORATORS
Functions that modify the behavior of other functions without changing their source code.

Key Concepts:
- Higher-order functions (accept or return functions)
- Closure (functions that remember their environment)
- The @ syntax sugar
"""

# ==============================================================================
# 1. BASIC DECORATOR TEMPLATE
# ==============================================================================
def simple_decorator(func):
    """Adds behavior before and after function execution"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello World!")

greet()
# Output:
# Before function call
# Hello World!
# After function call

# ==============================================================================
# 2. DECORATING FUNCTIONS WITH ARGUMENTS
# ==============================================================================
def args_decorator(func):
    """Handles decorated functions with arguments"""
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@args_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # Output: Running add with (3, 5), {} \n 8

# ==============================================================================
# 3. DECORATORS WITH PARAMETERS
# ==============================================================================
def repeat(num_times):
    """Decorator factory that accepts arguments"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Alice")
# Output:
# Hello Alice!
# Hello Alice!
# Hello Alice!

# ==============================================================================
# 4. REAL-WORLD USE CASES
# ==============================================================================
import time
from functools import wraps

# A. Timing Decorator
def timer(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)

slow_function()  # Output: slow_function took 0.5000 seconds

# B. Authorization Decorator
def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != role:
                raise PermissionError(f"Requires {role} role")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@requires_role('admin')
def delete_database(user):
    print(f"Database deleted by {user['name']}")

admin_user = {'name': 'Alice', 'role': 'admin'}
delete_database(admin_user)  # Output: Database deleted by Alice

# ==============================================================================
# 5. CLASS DECORATORS
# ==============================================================================
def singleton(cls):
    """Ensures a class has only one instance"""
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Initializing database...")

db1 = Database()
db2 = Database()
print(db1 is db2)  # Output: True (same instance)

# ==============================================================================
# 6. DECORATOR STACKING
# ==============================================================================
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def hello():
    return "Hello"

print(hello())  # Output: <b><i>Hello</i></b>

# ==============================================================================
# 7. BEST PRACTICES
# ==============================================================================
"""
1. Use @functools.wraps to preserve metadata
2. Document decorator behavior clearly
3. Avoid side effects in decorators
4. Consider performance impact
5. For complex decorators, use classes with __call__
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a @cache decorator that memoizes function results
# 2. Make a @retry decorator that retries failed functions
# 3. Implement a @validate_input decorator for type checking