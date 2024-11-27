# While loop is used to repeat a block of code as long as the condition is True.
# while condition:
    # code to be executed

# 1. Basic while loops
count = 0 
while count < 5:
    print(f"count is {count}")
    count += 1

# 2. Infinite loop (Be careful)
while True:
    print("This mf will run forver")
    break # stops the loop

# 3. break and continue:
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue # skip when number = 3
    if number == 4:
        break # stop when number = 4
    print(number)

# 4. Validating Input
user_input = ""
while user_input.lower() != "yes":
    user_input = input("Do you want to continue? (yes/no): ")
print("Thank you")

# 5. Combining with Else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed")
