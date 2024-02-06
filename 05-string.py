first_name = "Jurgen"
last_name = 'Klopp'

print(first_name, last_name)
print(type(first_name))

age = 85
print(age)
age = "eighty five"
print(age)

print(first_name + " " + last_name)
print(age * 2)

### String Indexing

print(first_name[0])  # J
print(first_name[-1])  # n
print(first_name[0:3])  # Jur
print(first_name[:3])  # Jur
print(first_name[3:])  # gen
print(first_name[0:5:1])  # Jurge 0,1,2,3,4
print(first_name[0:5:2])  # [start:stop:step]  Jre 0,2,4
print(first_name[0:5:3])  # Jg 0,3
# print(first_name[100])  # IndexError: string index out of range

### None

user = None
print(user)
