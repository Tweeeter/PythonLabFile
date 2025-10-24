# Input
string = input("Enter a string: ").lower()
char = input("Enter a character to count: ").lower()

# Count occurrences
count = string.count(char)

# Result
print(f"The character '{char}' appears {count} times in '{string}'")
