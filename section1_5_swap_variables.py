# input 
x = input("Enter first value: ")
y = input("Enter second value: ")

# Display original values
print(f"Before swapping: x = {x}, y = {y}")

# Swap the variables
temp = x
x = y
y = temp

# Display the swapped values
print(f"After swapping: x = {x}, y = {y}")