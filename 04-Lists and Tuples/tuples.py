# Tuples = is an immutable (unchangeable) collection of ordered items.

# Empty tuple
my_tuple = ()

# Tuple with values
my_tuple = (1, 2, 3)

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

#TUPLE OPERATIONS
# 1. Accessing elements
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])  # Output: 10
print(my_tuple[-1])  # Output: 40

# 2. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)

# 3. Immutability
my_tuple = (1, 2, 3)
# my_tuple[1] = 10  # This will raise an error!

# 4. Unpacking
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# 5. Single Element Tuple: To create a tuple with one element, add a trailing comma.
single = (42,)  # This is a tuple
not_a_tuple = (42)  # This is an integer
