### Nested Lists

nested = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(nested[0][1])  # 2

for arr in nested:
    for val in arr:
        print(val)

### List Operators

print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]
print(1 in [1, 2, 3])  # True

### Sort, Reverse, Count

num = [11, 22, 13, 14, 15]
print(num.count(11))  # 1
num.reverse()  # [15, 14, 13, 12, 11]
num.sort()  # [11, 12, 13, 14, 15]
print('after sort', num)
num.sort(reverse=True)  # [15, 14, 13, 12, 11]

### List are Mutable

nums1 = [11, 12, 13, 14, 15]
nums2 = nums1
nums1[0] = 99  # [99, 12, 13, 14, 15]
print(nums2)  # [99, 12, 13, 14, 15]
nums2[1] = 88
print(nums1)  # [99, 88, 13, 14, 15]

### == vs is

print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] is [1, 2, 3])  # False
print(nums1 is nums2)  # True

### Join and Split

birthday = "11/12/1999"
print(birthday.split("/"))  # ['11', '12', '1999']
print(birthday.split(" "))  # ['11/12/1999']
print(birthday.split("."))  # ['11/12/1999']

date = ["11", "12", "1999"]
print("/".join(date))  # 11/12/1999
print(".".join(date))  # 11.12.1999
print("".join(date))  # 11121999
print(" ".join(date))  # 11 12 1999
# print(date.join("/"))  # AttributeError: 'list' object has no attribute 'join'

new_birthday = "11/12/1999"
print(new_birthday.replace("/", "-"))  # 11-12-1999
print("-".join(new_birthday.split('/')))  # 11-12-1999

letters = ["a", "b", "c", "d"]
print("".join(letters))  # abcd

### List Unpacking

user = ["John", "Doe", 30]
first_name, last_name, *other = user

item = [4, "Pizza", "Plain", 8.99]
quantity, product, *others = item
print(quantity, product, others)  # 4 Pizza ['Plain', 8.99]

item2 = [4, "Pizza", "Plain", "Extra Cheese", "Garlic Bread", 8.99]
quantity, product, *extras, price = item2

### Copying a List

nums3 = [11, 12, 13, 14, 15]
nums4 = nums3.copy()
print(nums3 == nums4)  # True
print(nums3 is nums4)  # False

list1 = [2, 9, ['a', 'b', 'c']]
list2 = list1.copy()
list1[2][0] = 'x'
print(list2)  # [2, 9, ['x', 'b', 'c']]

import copy

list3 = [2, 9, ['a', 'b', 'c']]
list4 = copy.deepcopy(list3)
list3[2][0] = 'x'
print(list4)  # [2, 9, ['a', 'b', 'c']]

### List comprehension

squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

names = ["John", "Doe", "Jane", "Smith"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'John': 4, 'Doe': 3, 'Jane': 4, 'Smith': 5}
