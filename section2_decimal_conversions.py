# Input
decimal = int(input("Enter a decimal number: "))

# Convert to binary, octal and hexadecimal
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

# Result
print(f"Binary equivalent of {decimal} is: {binary}")
print(f"Octal equivalent of {decimal} is: {octal}")
print(f"Hexadecimal equivalent of {decimal} is: {hexadecimal}")