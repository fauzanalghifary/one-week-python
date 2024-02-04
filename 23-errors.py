### Syntax Error

# while 1<4 # This is a syntax error

### Name Error

# print(a) # This is a name error

### Index Error

lst = [1, 2, 3]
# print(lst[3]) # This is an index error

### Type Error

# print(3 + "4") # This is a type error

### Value Error

# int("a")  # This is a value error

### Key Error

d = {"a": 1, "b": 2}


# print(d["c"])  # This is a key error


### Raising an exception (force an error)

def greet_user(name):
    if len(name) < 3:
        raise ValueError("Name is too short")
    print(f"Hello, {name}!")


# greet_user("Jo") # ValueError: Name is too short

### Try and except

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

try:
    name = input("Name: ")
    if len(name) < 3:
        raise ValueError("Name is too short")
    print(f"Hello, {name}!")
except ValueError as e:
    print(e)
except (ZeroDivisionError, ArithmeticError):
    print("Something went wrong")
except:
    print("Something went wrong")

### LBYL (Look Before You Leap) vs
### EAFP (Easier to Ask for Forgiveness than Permission)

# LBYL (Non-Pythonic)

year = input("Year: ")
if year.isnumeric():
    print(int(year))
else:
    print("Invalid year")

# EAFP (Pythonic)

year = input("Year: ")
try:
    print(int(year))
except ValueError:
    print("Invalid year")
else:
    print("Valid year")
finally:
    print("Thank you!")


### Custom Error Classes

class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __str__(self):
        return f"{self.name}, read {self.page_read} out of {self.page_count} pages."

    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError("You can't read more than the total pages.")
        self.page_read += pages
        print(f"You have now read {self.page_read} pages out of {self.page_count}.")


book = Book("Harry Potter", 300)
print(book)

try:
    book.read(400)
except TooManyPagesReadError as e:
    print(e)
