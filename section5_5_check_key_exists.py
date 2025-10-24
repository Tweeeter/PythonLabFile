# Create a dictionary
student = {
    'name': 'John',
    'age': 20,
    'grade': 'A',
    'subjects': ['Math', 'Science', 'English']
}


# Using get() method
key_to_check = 'subjects'
value = student.get(key_to_check, 'Not Found')
if value != 'Not Found':
    print(f"Key '{key_to_check}' exists with value: {value}")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary")