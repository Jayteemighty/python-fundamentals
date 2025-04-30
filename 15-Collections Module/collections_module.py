"""
COLLECTIONS MODULE
Specialized container datatypes providing alternatives to Python's general purpose built-ins.

Key Data Structures:
1. namedtuple: Tuple with named fields
2. deque: Double-ended queue
3. Counter: Hashable object counting
4. OrderedDict: Dict that remembers insertion order
5. defaultdict: Dict with default factory
6. ChainMap: Single view of multiple mappings
"""

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap
import json

# ==============================================================================
# 1. namedtuple
# ==============================================================================
# Create a subclass of tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(f"\nnamedtuple: {p}")            # Point(x=11, y=22)
print(f"Access by name: {p.x}")       # 11
print(f"Access by index: {p[1]}")     # 22

# Useful for CSV/DB records
Employee = namedtuple('Employee', 'name age department')
emp = Employee('Alice', 30, 'Engineering')
print(f"Employee: {emp.name} in {emp.department}")

# ==============================================================================
# 2. deque (Double-ended queue)
# ==============================================================================
# Thread-safe, memory efficient appends/pops from either end
d = deque('ghi')
print("\ndeque:")
d.append('j')            # Add to right
d.appendleft('f')        # Add to left
print(f"Initial: {d}")   # deque(['f', 'g', 'h', 'i', 'j'])

d.pop()                  # Remove from right
d.popleft()              # Remove from left
print(f"After ops: {d}") # deque(['g', 'h', 'i'])

# Useful for sliding windows/queues
d.extend('jkl')          # Add multiple at once
print(f"Extended: {d}")  # deque(['g', 'h', 'i', 'j', 'k', 'l'])

# ==============================================================================
# 3. Counter
# ==============================================================================
# Count hashable objects (like multiset)
words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
word_counts = Counter(words)
print("\nCounter:")
print(f"Counts: {word_counts}")          # Counter({'blue': 3, 'red': 2, 'green': 1})
print(f"Most common: {word_counts.most_common(1)}")  # [('blue', 3)]

# Mathematical operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"Addition: {c1 + c2}")       # Counter({'a': 4, 'b': 3})
print(f"Subtraction: {c1 - c2}")    # Counter({'a': 2})

# ==============================================================================
# 4. OrderedDict
# ==============================================================================
# Dictionary that remembers insertion order (Python 3.7+ dicts do this natively)
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['c'] = 3
print("\nOrderedDict:")
print(f"Keys: {list(od.keys())}")  # ['z', 'a', 'c']

# Still useful for:
# - Equality tests with order sensitivity
# - Controlling order in JSON serialization
od.move_to_end('z')
print(f"After move: {list(od.keys())}")  # ['a', 'c', 'z']

# ==============================================================================
# 5. defaultdict
# ==============================================================================
# Dictionary with default factory for missing keys
dd = defaultdict(int)
words = ["apple", "banana", "apple"]
for word in words:
    dd[word] += 1
print("\ndefaultdict:")
print(f"Word counts: {dd}")  # defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})

# Grouping with lists
departments = [
    ('Sales', 'Alice'),
    ('Engineering', 'Bob'),
    ('Sales', 'Charlie')
]

dept_dict = defaultdict(list)
for dept, name in departments:
    dept_dict[dept].append(name)
print(f"Department groups: {dict(dept_dict)}")

# ==============================================================================
# 6. ChainMap
# ==============================================================================
# Single view of multiple mappings
defaults = {'theme': 'light', 'language': 'en'}
user_prefs = {'language': 'fr', 'accent': 'paris'}

combined = ChainMap(user_prefs, defaults)
print("\nChainMap:")
print(f"Language: {combined['language']}")  # fr (from user_prefs)
print(f"Theme: {combined['theme']}")        # light (from defaults)

# Modifications affect first mapping only
combined['theme'] = 'dark'
print(f"Modified user_prefs: {user_prefs}")  # Now includes 'theme': 'dark'

# ==============================================================================
# 7. REAL-WORLD USE CASES
# ==============================================================================
# A. Processing large files with deque (memory efficiency)
def sliding_window(iterable, size=3):
    """Generate sliding windows using deque"""
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield tuple(window)

print("\nSliding Window:")
for win in sliding_window('abcdefgh', 4):
    print(win)

# B. JSON with OrderedDict
data = json.loads('{"z":1,"a":2}', object_pairs_hook=OrderedDict)
print(f"\nOrdered JSON: {list(data.keys())}")  # ['z', 'a']

# ==============================================================================
# 8. BEST PRACTICES
# ==============================================================================
"""
1. Use namedtuple for immutable records (better than dicts when field names fixed)
2. deque for FIFO/LIFO queues (faster than list for head operations)
3. Counter when you need to count items (better than manual dict counting)
4. defaultdict reduces if-else logic for missing keys
5. ChainMap for layered configuration handling
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a inventory system using Counter (add/remove items)
# 2. Implement a LRU cache with OrderedDict
# 3. Process log files to count errors by type using defaultdict