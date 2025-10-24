# Create a list
my_list = ['a', 'b', 'a', 'c', 'b', 'a']

# Count frequency
frequency = {}
for item in my_list:
    frequency[item] = my_list.count(item)

# Convert to tuple
result = tuple(frequency.items())

# Result
print(f"Frequency as tuples: {result}")
