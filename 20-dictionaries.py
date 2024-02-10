### Creating a dictionary

empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

order = {
    'starter': 'Salad',
    'main': 'Steak',
    'dessert': 'Ice Cream',
    'price': 20,
    'is_on_discount': False
}

num = {
    3: 'three',
}

### Accessing data in a dictionary

print(order['main'])  # Steak
print(order['price'])  # 20
# print(order['name'])  # KeyError: 'name'
print(num[3])  # three

### Adding and updating data in a dictionary

order['drinks'] = 'Tea'
order['price'] += 10

order.update({'drinks': 'Water', 'price': 30, 'name': 'John'})

### get() method and 'in' operator

print(order.get('drinks'))  # Tea
print(order.get('name'))  # None

if 'name' in order:
    print(order['name'])

### pop(), clear() and del

print(order.pop('drinks'))  # Tea
del order['dessert']
print(order)  # {'starter': 'Salad', 'main': 'Steak', 'price': 30, 'is_on_discount': False}
order.popitem()  # ('is_on_discount', False) - removes the last item
print(order)  # {'starter': 'Salad', 'main': 'Steak', 'price': 30}
order.clear()
print(order)  # {}

### Dictionary are mutable too!


new_order = {
    'starter': 'Salad',
    'main': 'Steak',
    'price': 20,
}

new_order2 = new_order
new_order2['price'] = 30
print(new_order)  # {'starter': 'Salad', 'main': 'Steak', 'price': 30}
print(new_order2 is new_order)  # True

### Iterating over a dictionary (keys, values, items)

print(new_order.keys())  # dict_keys(['starter', 'main', 'price'])
print(new_order.values())  # dict_values(['Salad', 'Steak', 30])
print(new_order.items())  # dict_items([('starter', 'Salad'), ('main', 'Steak'), ('price', 30)])

for key in new_order.keys():
    print(key)  # starter, main, price

for value in new_order.values():
    print(value)  # Salad, Steak, 30

for key, value in new_order.items():
    print(f'{key}: {value}')  # starter: Salad, main: Steak, price: 30

for key in new_order:
    print(key)  # starter, main, price

### Dictionary merging

dict1 = {
    'name': 'John',
    'age': 25
}

dict2 = {
    'name': 'Jane',
    'city': 'New York'
}

dict1.update(dict2)
print(dict1)  # {'name': 'Jane', 'age': 25, 'city': 'New York'}

dict3 = {**dict1, **dict2}
print(dict3)  # {'name': 'Jane', 'age': 25, 'city': 'New York'}

dict4 = dict1 | dict2
print(dict4)  # {'name': 'Jane', 'age': 25, 'city': 'New York'}

dict5 = dict2 | dict1
print(dict5)  # {'name': 'John', 'city': 'New York', 'age': 25}

### List and Dictionary

users = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30}
]

user = {
    'name': 'John',
    'age': 25,
    'hobbies': ['Tennis', 'Coding'],
    'address': {
        'city': 'New York',
        'street': 'Broadway'
    }
}

### Dictionary comprehension

new_users = [
    [0, 'Bob', 25],
    [1, 'Jane', 30],
    [2, 'Alice', 27],
]

username_mapping = {user[1]: user for user in new_users}
print(username_mapping)  # {'Bob': (0, 'Bob', 25), 'Jane': (1, 'Jane', 30), 'Alice': (2, 'Alice', 27)}
