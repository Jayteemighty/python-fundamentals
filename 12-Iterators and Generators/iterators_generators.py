"""
ITERATORS AND GENERATORS
Special objects that enable lazy evaluation and memory-efficient data processing.
"""

# ==============================================================================
# 1. ITERATORS (Protocol: __iter__() and __next__())
# ==============================================================================
class CountDown:
    """Custom iterator that counts down from given number"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Using the iterator
print("Countdown:")
for num in CountDown(5):
    print(num, end=" ")  # Output: 5 4 3 2 1

# ==============================================================================
# 2. GENERATORS (yield keyword)
# ==============================================================================
def fibonacci_gen(limit):
    """Generator function for Fibonacci sequence"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("\n\nFibonacci:")
fib = fibonacci_gen(50)
print(list(fib))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator expression (similar to list comprehension)
squares_gen = (x**2 for x in range(10))
print("Squares:", list(squares_gen))

# ==============================================================================
# 3. REAL-WORLD USE CASES
# ==============================================================================
# A. Processing large files line-by-line
def read_large_file(file_path):
    """Memory-efficient file reader"""
    with open(file_path) as file:
        for line in file:
            yield line.strip()

# B. Infinite sequence generator
def infinite_counter(start=0):
    """Generates numbers indefinitely"""
    n = start
    while True:
        yield n
        n += 1

# ==============================================================================
# 4. KEY DIFFERENCES
# ==============================================================================
"""
ITERATORS:
- Implement class with __iter__/__next__
- Maintain state in attributes
- Can be infinite or finite
- Manual implementation

GENERATORS:
- Functions using 'yield'
- Implicit state preservation
- Cleaner syntax
- Automatic iterator implementation
"""

# ==============================================================================
# 5. MEMORY EFFICIENCY DEMO
# ==============================================================================
import sys

# List approach (stores all numbers in memory)
nums_list = [x for x in range(1000000)]
print(f"\nList size: {sys.getsizeof(nums_list)/1e6:.2f} MB")

# Generator approach (produces numbers on demand)
nums_gen = (x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(nums_gen)} bytes")

# ==============================================================================
# 6. PIPELINING GENERATORS
# ==============================================================================
def filter_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            yield n

def square_numbers(numbers):
    for n in numbers:
        yield n ** 2

# Chained processing
numbers = range(10)
pipeline = square_numbers(filter_odd(numbers))
print("\nPipeline result:", list(pipeline))  # [1, 9, 25, 49, 81]

# ==============================================================================
# 7. SENDING DATA TO GENERATORS (coroutines)
# ==============================================================================
def number_accumulator():
    total = 0
    while True:
        num = yield
        if num is None:
            break
        total += num
    yield total

acc = number_accumulator()
next(acc)  # Prime the generator
for n in [1, 2, 3, 4]:
    acc.send(n)
print("Accumulated:", acc.send(None))  # Output: 10

# ==============================================================================
# 8. BEST PRACTICES
# ==============================================================================
"""
1. Use generators for memory-intensive operations
2. Prefer generator expressions for simple transformations
3. Document whether generators are finite or infinite
4. Handle StopIteration in custom iterators
5. Consider itertools for advanced patterns
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create an iterator that yields prime numbers
# 2. Make a generator that batches items from iterable (e.g., batch_size=3)
# 3. Implement a generator pipeline: read -> filter -> process -> output