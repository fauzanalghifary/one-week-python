def divide(dividend, divisor):
    if divisor == 0:
        return "You fool!"
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)  # 5.0


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Jill", "age": 35},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "John", get_friend_name))  # {'name': 'John', 'age': 25}
