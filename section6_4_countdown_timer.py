import time

# Input
seconds = int(input("Enter time in seconds: "))

# Countdown
for i in range(seconds, 0, -1):
    print(f"Time remaining: {i} seconds")
    time.sleep(1)

# Result
print("Time's up!")
