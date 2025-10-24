# Create a new file
file_name = "sample.txt"

# Create and write to file
with open(file_name, 'w') as file:
    file.write("This is a new file created using Python!")

print(f"File '{file_name}' has been created successfully!")