# Create a dictionary
scores = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'Eva': 95,
    'Mike': 88
}

# Sort dictionary by values in ascending order
sorted_dict_asc = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Dictionary sorted by value (ascending):\n",sorted_dict_asc)
