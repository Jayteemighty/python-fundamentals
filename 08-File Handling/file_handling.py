"""
FILE HANDLING IN PYTHON
Working with files to read, write, and manage data persistently.
"""

# ==============================================================================
# 1. READING FILES
# ==============================================================================
# Method 1: read() - Reads entire file at once
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:\n", content)

# Method 2: readline() - Reads one line at a time
with open('example.txt', 'r') as file:
    print("\nLine by line:")
    line = file.readline()
    while line:
        print(line.strip())  # strip() removes trailing newlines
        line = file.readline()

# Method 3: readlines() - Returns list of all lines
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("\nList of lines:", lines)


# ==============================================================================
# 2. WRITING FILES
# ==============================================================================
# Mode 'w' overwrites, 'a' appends
with open('output.txt', 'w') as file:
    file.write("Hello World!\n")
    file.write("This is a new line.\n")

# Writing multiple lines efficiently
lines_to_write = ["First line\n", "Second line\n", "Third line\n"]
with open('output.txt', 'a') as file:  # 'a' for append mode
    file.writelines(lines_to_write)


# ==============================================================================
# 3. USING 'WITH' STATEMENT (CONTEXT MANAGER)
# ==============================================================================
# Automatically closes file after block execution
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("\nError: File not found!")


# ==============================================================================
# 4. FILE POSITIONS (SEEK/TELL)
# ==============================================================================
with open('example.txt', 'r') as file:
    print("\nInitial position:", file.tell())  # 0
    file.seek(10)  # Move to 10th byte
    print("Position after seek:", file.tell())  # 10
    print("Content from position 10:", file.read())


# ==============================================================================
# 5. WORKING WITH DIFFERENT FILE TYPES
# ==============================================================================
# CSV Files
import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'London'])

# JSON Files
import json
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Binary Files (images, etc.)
with open('image.jpg', 'rb') as binfile:
    binary_data = binfile.read()  # Reads bytes instead of strings


# ==============================================================================
# 6. FILE OPERATIONS (OS MODULE)
# ==============================================================================
import os

# Check if file exists
print("\nFile exists?", os.path.exists('example.txt'))

# Get file size
print("File size (bytes):", os.path.getsize('example.txt'))

# List files in directory
print("Files in directory:", os.listdir('.'))

# Rename file
os.rename('old_name.txt', 'new_name.txt')

# Delete file
os.remove('file_to_delete.txt')


# ==============================================================================
# 7. BEST PRACTICES
# ==============================================================================
"""
1. Always use 'with' statements for automatic file closing
2. Handle exceptions (FileNotFoundError, PermissionError)
3. Specify encoding when needed: open('file.txt', 'r', encoding='utf-8')
4. For large files, process line-by-line instead of reading entire file
5. Use absolute paths for files outside working directory
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a program that copies a file's content to a new file
# 2. Write a script that counts word frequency in a text file
# 3. Create a CSV to JSON converter