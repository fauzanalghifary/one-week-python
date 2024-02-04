### Boolean

isRaining = True
isSunny = False
print(type(isRaining))  # <class 'bool'>

### Comparison Operators

print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False
print(2 != '2')  # True

### Comparison Accross Data Types

print(10 == '10')  # False
print(10 == 10.0)  # True
print(10 == int('10'))  # True

### Truty and Falsy Values

"""
Falsy Values:
- False
- 0
- 0.0
- ''
- []
- {}
- ()
- None
"""

print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool(None))  # False

print(bool(True))  # True
print(bool(1))  # True
print(bool(0.1))  # True
print(bool(' '))  # True
print(bool('False'))  # True
print(bool([1]))  # True

### In Operator

print("---IN OPERATOR---")
print('a' in 'apple')  # True
print('p' in 'apple')  # True
print('b' in 'apple')  # False
print('ap' in 'apple')  # True
print('pa' in 'apple')  # False

### Comparing Strings

print("---COMPARING STRINGS---")
print("a" < "b")  # True
print("a" < "A")  # False
print("aaaa" < "AAA")  # False

print(ord("a"))  # 97
print(ord("A"))  # 65
print(ord("b"))  # 98

print(chr(97))  # a
print(chr(65))  # A

print('100' < '2')  # True
