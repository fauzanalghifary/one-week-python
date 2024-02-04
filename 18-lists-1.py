### Create Lists

tasks = ["Install Python", "Learn Python", "Take a break"]
stuff = ["Install Python", 3, 5.6, "Learn Python", 7, 8.9, "Take a break", True]

a = list('hello')
print(a)  # ['h', 'e', 'l', 'l', 'o']

### Access Elements

print(tasks[0])  # Install Python
print(tasks[1])  # Learn Python
print(tasks[-1])  # Take a break

### Update Elements

tasks[0] = "Install Python 3"

### Append and Extend

tasks.append("Forget Python")  # ['Install Python 3', 'Learn Python', 'Take a break', 'Forget Python']

people = ["Alice", "Bob", "Charlie"]
people.extend(["David", "Eve"])  # ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

char = ["a", "b", "c"]
char.extend('def')  # ['a', 'b', 'c', 'd', 'e', 'f']

### Insert

nums = [1, 3, 4, 5]
nums.insert(1, 2)  # [1, 2, 3, 4, 5]

### Slices

print(nums[1:3])  # [2, 3]
print(nums[:2])  # [1, 2]
print(nums[2:])  # [3, 4, 5]
print(nums[::2])  # [1]

nums[1:3] = ['a', 'c']  # [1, 'a', 'c', 4, 5]
nums[1:3] = ['w', 'x', 'y', 'z']  # [1, 'w', 'x', 'y', 'z', 4, 5]

### Delete Elements

nums.clear()  # []
new_nums = [11, 12, 13, 14, 15]
new_nums.remove(13)  # [11, 12, 14, 15]
new_nums.pop()  # [11, 12, 14]
new_nums.pop(1)  # [11, 14]
del new_nums[0]  # [14]
del new_nums[0:2]  # []

### Looping Through Lists

for task in tasks:
    print(task)

idx = 0
while idx < len(tasks):
    print(tasks[idx])
    idx += 1

### List and Loop Patterns

lando_2021_results = [4, 4, 5, 8, 3, 14, 4, 2, 1, 3, 14, 5, 16, 7, 8, 9, 10, 1, 2, 13, 4]


def average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


def find_min(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
