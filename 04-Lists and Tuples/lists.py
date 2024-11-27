# List: A list is a mutable (changeable) collection of ordered items.

# 1. Empty List
my_list = []

# 2. List with values
my_list = [1,2,3,4,5]

# 3. List with mixed data types
mixed_list = [1, "Ororo", 2.0, True]

# LIST OPERATIONS
# 1. Accessing elements
my_list = [1,2,3,4,5]
print(my_list[0]) # Output: 1
print(my_list[-1]) # Output: 5 (last element)

# 2. Slicing
my_list = [1,2,3,4,5,6,7]
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[::2])  # Output: [1, 3, 5, 7] (step size 2)

# 3. Modifying elements
my_list = [1,2,3]
my_list[1] = 30
print(my_list) #Output: [1,30,3]

# 4. Concatenation
list1 = [1,2]
list2 = [3,4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
print(list1 * 2)      # Output: [1, 2, 1, 2]