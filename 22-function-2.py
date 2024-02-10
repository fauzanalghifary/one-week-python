### *args

def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


def average(*nums):
    return sum(nums) / len(nums)


print(average(1, 2, 3))


def silly(first, *args):
    print(f"The first parameter is {first}")
    print(f"The other parameters are {args}")


silly(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


### **kwargs (keyword arguments)

def demo(**kwargs):
    print(kwargs)


# demo(3)  # TypeError: demo() takes 0 positional arguments but 1 was given
demo(a=1, b=2, c=3, d=4, e=5)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


def print_ages(**ages):
    for name, age in ages.items():
        print(f"{name} is {age} years old.")


print_ages(John=25, Jane=24, Tom=26, Alice=23)


def add(x, y):
    return x + y, 'ok'


nums = {'x': 2, 'y': 3}
print(add(**nums))  # 5


### Parameter List Ordering (args, *args, default parameters, **kwargs)


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def apply(*args, operator):
    if operator == '+':
        return sum(args)
    elif operator == '*':
        return multiply(*args)
    else:
        return "Invalid operator"


apply(1, 2, 3, 4, 5, operator='+')  # 15
apply(1, 2, 3, 4, 5, operator='*')  # 120


def demo2(a, b, *args, c=10, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")


demo2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, d=11, e=12)


# a=1, b=2, args=(3, 4, 5, 6, 7, 8, 9, 10), c=10, kwargs={'d': 11, 'e': 12}

def display_info(person, *args, status="single", **kwargs):
    print(f"Person: {person}")
    print(f"Args: {args}")
    print(f"Status: {status}")
    print(f"Kwargs: {kwargs}")


display_info("John", 25, status="married", city="New York", country="USA")


# Person: John
# Args: (25,)
# Status: married
# Kwargs: {'city': 'New York', 'country': 'USA'}


### Mutable default arguments

def add_twice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    return lst


add_twice('hi', [1, 2, 3])  # ['hi', 'hi', 1, 2, 3]
add_twice('yay')  # ['yay', 'yay']
add_twice('hello')  # ['yay', 'yay', 'hello', 'hello'] ??????????


def add_twice_fix(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst


add_twice_fix('wow')  # ['wow', 'wow']
add_twice_fix('nice')  # ['nice', 'nice']


### Unpacking arguments

def sums(*nums):
    return sum(nums)


the_nums = [1, 2, 3, 4, 5]
print(sums(*the_nums))  # 15
# print(sums(the_nums))  # TypeError: unsupported operand type(s) for +: 'int' and 'list'

the_nums2 = [6, 7, 8, 9, 10]
combined_nums = [*the_nums, *the_nums2]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


### Practice

def contains_pickle(*args):
    return "pickle" in args


contains_pickle("apple", "banana", [])  # False
contains_pickle("apple", "banana", "pickle")  # True


def count_fails(*scores):
    count = 0
    for score in scores:
        if score < 50:
            count += 1
    return count


print(count_fails(80, 90, 40, 30, 60, 70))  # 2


def get_top_students(**students):
    top_students = []
    for name, score in students.items():
        if score > 90:
            top_students.append(name)
    return top_students


get_top_students(John=95, Jane=85, Tom=90, Alice=92)  # ['John', 'Alice']

### Lambda Functions

add = lambda x, y: x + y
print(add(2, 3))  # 5

print((lambda x, y: x + y)(2, 3))  # 5


def double(x):
    return x * 2


sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]  # [2, 4, 6, 8, 10]
doubled2 = [x * 2 for x in sequence]  # [2, 4, 6, 8, 10]

doubled3 = list(map(double, sequence))  # [2, 4, 6, 8, 10]
doubled4 = list(map(lambda x: x * 2, sequence))  # [2, 4, 6, 8, 10]

print(doubled)
print(doubled2)
