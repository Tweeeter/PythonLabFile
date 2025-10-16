# Program for copying, moving, and renaming files

import shutil
import os

# Create a sample file first
with open("original.txt", 'w') as file:
    file.write("This is the original file content")

#Copy file
print("Copying file...")
shutil.copy("original.txt", "copied.txt")
print("File copied successfully!")

#Rename file
print("Renaming file...")
os.rename("copied.txt", "renamed.txt")
print("File renamed successfully!")

#Move file
print("Moving file...")
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
shutil.move("renamed.txt", "new_folder/moved.txt")
print("File moved successfully!")

print("Operations completed!")