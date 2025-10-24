# Input
string = input("Enter a string: ").lower()

# Check if palindrome
if string == string[::-1]:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
