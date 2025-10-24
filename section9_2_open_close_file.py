# Define the file name
file_name = "sample.txt"

# Create the file first with some content
with open(file_name, 'w') as temp:
    temp.write("Test file")

# Open the file
file = open(file_name, 'w+')
print(f"File '{file_name}' opened successfully")

# Close the file
file.close()
print(f"File '{file_name}' closed successfully")