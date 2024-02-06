### Continue and Break

for letter in "Python":
    if letter == "h":
        continue
    elif letter == "n":
        break
    print("Current letter: ", letter)

### Nested Loops

for outer in range(1, 4):
    print("Outer: ", outer)
    for inner in range(1, 3):
        print("\tInner: ", inner)

import math

math.sqrt(3)
