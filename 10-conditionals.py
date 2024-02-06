### Conditionals

age = 77

if age >= 60:
    print("You are a senior")
elif age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
print("End of program")

match age:
    case x if x >= 60:
        print("You are a senior")
    case x if x >= 18:
        print("You are an adult")
    case _:
        print("You are a minor")

### Random numbers

__import__("random").randint(1, 6)  # Random number between 1 and 6

import random

print(random.randint(1, 6))  # Random number between 1 and 6
