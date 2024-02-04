### While loop

answer = input("please say hi: ")

while answer != "hi":
    answer = input("please say hi: ")
print("Thank you for saying hi")

num = 1
while num <= 10:
    print(num)
    num += 1
print("Blast off")

import random

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
while num1 != num2:
    print(num1, num2)
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
print(num1, num2)

### For loop

for char in "hello":
    print(char)

### Range function

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(1, 6, 2):
    print(i)  # 1, 3, 5

for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
