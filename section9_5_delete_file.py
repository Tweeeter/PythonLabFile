import os

# Create a file to delete
file_to_delete = "temp.txt"
with open(file_to_delete, 'w') as file:
    file.write("This file will be deleted")

print(f"File '{file_to_delete}' created")

# Delete the file
os.remove(file_to_delete)
print(f"File '{file_to_delete}' deleted successfully!")