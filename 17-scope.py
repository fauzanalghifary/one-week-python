### Global Scope

movie = "The Matrix"


def scope_test():
    print(movie)  # The Matrix

    def do_local():
        print(movie)  # The Matrix

    do_local()

    return movie


print(movie)  # The Matrix
print(scope_test())  # The Matrix


### Local Scope

def scope_test():
    animal = "Dog"
    print(animal)  # Dog
    return animal


# print(animal)  # NameError: name 'animal' is not defined

### Scope for Loops and Conditionals

for char in "Python":
    color = "Blue"
    print(char, color)

print(color)  # Blue

if True:
    city = "San Francisco"

print(city)  # San Francisco


### Enclosing Scope

def outer_function():
    actor = "Keanu Reeves"

    def inner_function():
        print(actor)  # Keanu Reeves

    inner_function()


outer_function()

### Built-in Scope

num = 333
str(num)  # '333'

### Scope Precedence Rules (LEGB)

hobby = "Gardening"


def outer():
    hobby = "Reading"
    print(hobby)  # Reading

    def inner():
        hobby = "Coding"
        print(hobby)  # Coding

    inner()
    print(hobby)  # Reading


print(hobby)  # Gardening

### Global Keyword

score = 100


def double_score():
    global score
    score = score * 2
    print(score)  # 200


double_score()
