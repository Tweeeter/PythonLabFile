# Create a list and tuple
my_list = [1, 2, 3]
my_tuple = (4, 5)

# Add tuple to list
my_list.extend(my_tuple)
print(f"After adding tuple to list: {my_list}")

# Add list to tuple
new_list = [6, 7]
new_tuple = my_tuple + (6, 7)
print(f"After adding list to tuple: {new_tuple}")
