# Input
string = input("Enter a string: ")

# Function to generate permutations
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]
        remaining = s[0:i] + s[i+1:]
        permute(remaining, answer + ch)

# Result
print(f"All permutations of '{string}':")
permute(string)
