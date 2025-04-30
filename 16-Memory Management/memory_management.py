"""
PYTHON MEMORY MANAGEMENT
Understanding how Python handles memory allocation and garbage collection.

Key Concepts:
- Object creation and deletion
- Reference counting
- Garbage collection (GC)
- Memory profiling
- id() and object identity
"""

import sys
import gc
from memory_profiler import profile
from weakref import ref

# ==============================================================================
# 1. OBJECT IDENTITY AND id()
# ==============================================================================
a = 42
b = 42
c = 500
d = 500

print(f"\nid() examples:")
print(f"a and b (small ints): {id(a)}, {id(b)}")  # Same id (interning)
print(f"c and d (large ints): {id(c)}, {id(d)}")  # Different ids

# ==============================================================================
# 2. REFERENCE COUNTING
# ==============================================================================
def ref_count_example():
    x = [1, 2, 3]
    y = x
    print(f"\nReference count: {sys.getrefcount(x)}")  # 3 (x, y, and getrefcount arg)

ref_count_example()

# ==============================================================================
# 3. GARBAGE COLLECTION
# ==============================================================================
class CircularRef:
    def __init__(self):
        self.other = None

# Create circular reference
obj1 = CircularRef()
obj2 = CircularRef()
obj1.other = obj2
obj2.other = obj1

# Force garbage collection
print("\nGarbage collection:")
print(f"Before GC: {gc.get_count()}")  # (generation 0, 1, 2)
gc.collect()  # Manually trigger collection
print(f"After GC: {gc.get_count()}")

# ==============================================================================
# 4. WEAK REFERENCES
# ==============================================================================
class Data:
    def __init__(self, value):
        self.value = value

strong_ref = Data(100)
weak_ref = ref(strong_ref)

print("\nWeak references:")
print(f"Strong ref: {strong_ref.value}")
print(f"Weak ref: {weak_ref().value}")  # Access via ()

del strong_ref
print(f"After deletion: {weak_ref()}")  # None

# ==============================================================================
# 5. MEMORY PROFILING
# ==============================================================================
@profile
def memory_intensive():
    """Function that allocates significant memory"""
    big_list = [x for x in range(100000)]
    del big_list  # Explicit deletion
    return None

print("\nMemory profiling:")
memory_intensive()

# ==============================================================================
# 6. DEL STATEMENT AND OBJECT LIFECYCLE
# ==============================================================================
class Resource:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"\nCleaning up {self.name}")

res = Resource("Database Connection")
del res  # Triggers __del__

# ==============================================================================
# 7. INTERNING AND MEMORY OPTIMIZATION
# ==============================================================================
# Small integers and strings are interned
s1 = "hello"
s2 = "hello"
print(f"\nString interning: {s1 is s2}")  # True

# Large strings are not
l1 = "hello world!"
l2 = "hello world!"
print(f"Large strings: {l1 is l2}")  # False (implementation dependent)

# ==============================================================================
# 8. MEMORYVIEW FOR EFFICIENT ACCESS
# ==============================================================================
data = bytearray(b'abcd')
mv = memoryview(data)
print("\nMemoryview:")
print(f"First byte: {mv[0]}")  # 97 (ASCII 'a')
mv[1] = 122  # Modify through view (ASCII 'z')
print(f"Modified: {data}")  # bytearray(b'a zcd')

# ==============================================================================
# 9. BEST PRACTICES
# ==============================================================================
"""
1. Use del for large objects when done
2. Avoid circular references (or use weakref)
3. Prefer generators for large datasets
4. Use memoryview for binary data
5. Profile before optimizing (memory_profiler, tracemalloc)
6. Consider __slots__ for memory-heavy classes
"""

# ==============================================================================
# 10. REAL-WORLD EXAMPLE
# ==============================================================================
class EfficientUser:
    __slots__ = ['id', 'name', 'email']  # Saves memory by preventing __dict__
    
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

print("\nMemory with __slots__:")
print(f"Normal class size: {sys.getsizeof(Resource('test'))} bytes")
print(f"Slots class size: {sys.getsizeof(EfficientUser(1, 'Alice', 'a@test.com'))} bytes")

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a memory leak scenario and fix it
# 2. Implement a context manager for resource cleanup
# 3. Compare memory usage between list and generator