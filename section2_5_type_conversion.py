# Input
string_value = input("Enter a number as string: ")
print(f"Original value: {string_value}, Type: {type(string_value)}")

# Convert to integer
int_value = int(string_value)
print(f"Converted to integer: {int_value}, Type: {type(int_value)}")

# Convert to float
float_value = float(string_value)
print(f"Converted to float: {float_value}, Type: {type(float_value)}")

# Convert integer to string
string_again = str(int_value)
print(f"Integer converted back to string: {string_again}, Type: {type(string_again)}")

# Convert to boolean
bool_value = bool(int_value)
print(f"Converted to boolean: {bool_value}, Type: {type(bool_value)}")