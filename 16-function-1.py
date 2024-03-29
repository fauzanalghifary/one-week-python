### Function

def greet_user():
    print("Hello!")


greet_user()


### Function with parameter

def greet_user(name):
    print(f"Hello, {name}!")


greet_user("John")


### Function with multiple parameters

def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_user("John", 25)


### Return

def greet_user(name, age):
    return f"Hello, {name}! You are {age} years old."


message = greet_user("John", 25)
print(message)  # Hello, John! You are 25 years old.


### Default parameter

def greet_user(name, age=18):
    return f"Hello, {name}! You are {age} years old."


message = greet_user("John")
print(message)  # Hello, John! You are 18 years old.


# def greet_user(name="John", age):  # SyntaxError: non-default argument follows default argument
#     return f"Hello, {name}! You are {age} years old."

### Keyword argument

def greet_user(name,
               age,
               location):
    return f"Hello, {name}! You are {age} years old."


message = greet_user(name="John",
                     age=25,
                     location="New York")
print(message)


### Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
