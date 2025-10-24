# Create a list of tuples
tuples_list = [(1, 3), (3, 2), (2, 1), (4, 4)]

# Sort by last element
sorted_list = sorted(tuples_list, key=lambda x: x[-1])

# Result
print(f"Original list: {tuples_list}")
print(f"Sorted list by last element: {sorted_list}")
