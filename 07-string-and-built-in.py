### Len

animal = "cat"
print(len(animal))
# print(len(123)) # TypeError: object of type 'int' has no len()

### Input

# name = input("Enter your name: ")
# print("Hello, " + name)

### Type Casting

age = "19"
new_age = int(age)
# print(age + 1)  # TypeError: can only concatenate str (not "int") to str
print(new_age + 1)

print(int(2.3))
print(float(2))

### F String

name = "John"
age = 19
print(f"Hello, {name}. You are {age} years old.")
