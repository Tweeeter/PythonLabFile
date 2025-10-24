# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'job': 'Engineer'
}

print("Original dictionary:\n", my_dict)
# Using pop() method
removed_value = my_dict.pop('age', 'Not found')
print("After deleting 'age' using pop():\n", my_dict)
print("Removed value:\n", removed_value)
