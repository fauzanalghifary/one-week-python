### Tuples

# Tuples are similar to lists, but they are immutable,
# meaning that they cannot be changed.
# You would use a tuple to present collection of items that should not be changed,
# such as days of the week, or dates on a calendar.

dishes = ('pizza', 'pasta', 'salad', 'nachos')
print(dishes)  # ('pizza', 'pasta', 'salad', 'nachos')
# dishes[0] = 'burger'  # TypeError: 'tuple' object does not support item assignment
# dishes.pop()  # AttributeError: 'tuple' object has no attribute 'pop'

single_value_tuple = (1,)
print(single_value_tuple[0])  # 1
print(len(dishes))  # 4
print(dishes[:2])  # ('pizza', 'pasta')
print(dishes)  # ('pizza', 'pasta', 'salad', 'nachos')
print(dishes.count('pizza'))  # 1

### Why use tuples?

# Tuples are faster than lists.
# use them for data that doesn't change.
# some methods return tuples, like dict.items()


### Sets

# Sets are unordered collections of unique elements.

numbers = {1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4}
print(numbers)  # {1, 2, 3, 4}

unique_numbers = set([1, 2, 3, 4, 4, 4, 4, 4, 4, 4])
print(unique_numbers)  # {1, 2, 3, 4}

empty_set = set()

unique_numbers.add(5)  # {1, 2, 3, 4, 5}
unique_numbers.add(5)  # {1, 2, 3, 4, 5}
unique_numbers.add(-1)  # {1, 2, 3, 4, 5, -1}

unique_numbers.remove(3)  # {1, 2, 4, 5, -1}
# unique_numbers.remove(3)  # KeyError: 3
unique_numbers.discard(3)  # {1, 2, 4, 5, -1}

unique_numbers.pop()  # 1
print(unique_numbers)  # {2, 4, 5, -1}

unique_numbers.clear()  # set()

### Intersections, Unions, and Differences

odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 11}

print(odd.intersection(prime))  # {3, 5, 7, 11}
print(odd & prime)  # {3, 5, 7, 11}

print(odd.union(prime))  # {1, 2, 3, 5, 7, 9, 11}
print(odd | prime)  # {1, 2, 3, 5, 7, 9, 11}

print(odd.difference(prime))  # {1, 9}
print(odd - prime)  # {1, 9}
print(prime - odd)  # {2}

### When to use a set

# Fast to find an item
# Easy ways to remove duplicates from a list
