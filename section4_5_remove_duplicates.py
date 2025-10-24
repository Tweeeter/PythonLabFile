# Using set() (Order not preserved)
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("Order not preserved:", unique_list)

# Using loop (Order preserved)
my_list = [1, 3, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("Order preserved:", unique_list)