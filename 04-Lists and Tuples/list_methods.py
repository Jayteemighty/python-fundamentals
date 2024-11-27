# 1. Append() - Add an item to the end of the list.
my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)   # Output: [1,2,3,4,5,6]

# 2. insert() - Insert an item at a specific position.
my_list =[1,2,4]
my_list.insert(2,3)  # postion, replacement
print(my_list)  # Output: [1,2,3,4]

# 3. remove() - Remove the first occurrence of a value.
my_list = [1,2,3,2]
my_list.remove(2)
print(my_list) #Output: [1,3,2]

# 4. pop() - Remove and return the item at a specific position.
my_list = [1,2,3,4,5]
print(my_list.pop(1)) # Output: 2
print(my_list)        # Output: [1, 3]

# 5. sort() - Sort the list in ascending order (or descending with reverse=True).
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# 6. reverse() - Reverse the order of the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# 7. len() - Get the number of elements in the list.
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3
