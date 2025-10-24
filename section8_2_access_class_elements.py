# Create a class
class Student:
    name = "John"
    age = 20
    grade = "A"
    subjects = ["Math", "Science"]

# Create an object
student = Student()

# Access all elements
print("Accessing all elements of the class:")
for attribute in dir(student):
    if not attribute.startswith('__'):
        value = getattr(student, attribute)
        print(f"{attribute}: {value}")
