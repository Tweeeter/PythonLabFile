# Create a class
class MyClass:
    x = 5
    y = "Hello"

# Create an object
obj = MyClass()
print(f"Object exists: {obj}")
print(f"x = {obj.x}")

# Delete the object
del obj

# Try to access deleted object
try:
    print(obj.x)
except NameError:
    print("Object has been deleted")
