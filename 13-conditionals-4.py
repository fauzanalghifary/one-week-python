### Truthy and Falsy

# color = input("Enter a color: ")
#
# if color:  # truthy
#     print(f"The color is {color}")
# else:
#     print("No color was entered")

### Operator Precedence

day = "Saturday"
is_vet = True
age = 10
# Veterans get a discount on Saturday
# Infants under 2 always get a discount

if age < 2 or (day == "Saturday" and is_vet):
    print("This person gets a discount")
else:
    print("This person does not get a discount")

print(False and not True or True)  # True

### Ternary Operator

age = 12
message = "Eligible" if age >= 18 else "Not eligible"

'''
JS TERNARY
let age = 12;
let message = age >= 18 ? "Eligible" : "Not eligible";
'''

### Logical OR

name = ""
print(name or "Guest")  # Guest

'''
JS Logical OR
let name = "";
console.log(name || "Guest");  // Guest

JS Nullish Coalescing Operator
console.log(name ?? "Guest");  // ""
'''
