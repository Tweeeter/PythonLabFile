# Create a tuple and a list
my_tuple = (1, 2, 3, 4, 5)
my_list = [3, 6, 7]

# Check if any list element is in tuple
found = False
for item in my_list:
    if item in my_tuple:
        print(f"{item} is present in the tuple")
        found = True

# Result
if not found:
    print("No list elements are present in the tuple")
