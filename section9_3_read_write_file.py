file_name = "data.txt"

# Write to file
print("Writing to file...")
with open(file_name, 'w') as file:
    file.write("Hello World!\n")
    file.write("This is line 2\n")
    file.write("Python file operations\n")

# Read from file
print("Reading from file:")
with open(file_name, 'r') as file:
    content = file.read()
    print(content)

# Append to file
print("Appending to file...")
with open(file_name, 'a') as file:
    file.write("This line is appended\n")

# Read again to show appended content
print("File content after appending:")
with open(file_name, 'r') as file:
    content = file.read()
    print(content)