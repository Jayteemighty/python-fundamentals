# If-else Statements: These are used in Python to execute code based on conditions.

#if-else statements typically goes something like this:

#if condition:
    # code to be executed when condition is true
#else:
    # code to be executed when condition is false

# Exzmples:
# 1. Simple If-Else Statement
x = 10

if x > 5:
    print("x is bigger than we thought")
else:
    print("x is smaller than we thought")

# 2. If-elif-else statements (elif means else if)
x = 25

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equals to 10")
else:
    print("x is less than 10")

# 3. Nested if-else statement
x = 24

if x > 18:
    if x % 2 == 0:
        print("Can date individual and age is even number")
    else:
        print("Can not date individual and age is not even number")

# 4. Logical operators like "and", "or", "not"
x = 20

if x > 10 and x < 30:
    print("x is between 10 and 30")
else:
    print("x is out of range")

# 5. One liner if-else (tenary operator)
x = 6
result = "Positive" if x > 0 else "Negative"
print(result)