# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Method 1: Using update() method
merged_dict1 = dict1.copy()
merged_dict1.update(dict2)
print("Merged dictionary :", merged_dict1)