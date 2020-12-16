"""
Functional Programming
Separate/organize of concerns. Also separate data and functions.
Objectives:
- Clear + Understandable
- Easy to Extend
- Easy to Maintain
- Memory Efficient
- DRY
Pilars:
- Pure Functions - Separate data from the behaviour
    - Given the same input, always return same output
    - It should not produce any side effect (outside the function)
"""
from functools import reduce


def multiply_by2(item):
    """Pure Function example"""
    return item*2


def only_odd(item):
    return item % 2 != 0


# map, filter, zip, and reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]
print(list(map(multiply_by2, my_list)))  # map(function, *iterables)
print(my_list)  # The original list was not affected

# Return expressions evaluated to True
print(list(filter(only_odd, my_list)))  # filter(function, *iterable)

# Return a tuple for each element in the iterable
# zip(iterable, iterable, ...)
print(list(zip(my_list, your_list, their_list)))


def accumulator(acc, item):
    """acc is the initial value passed to the function 'reduce'"""
    return acc + item


# reduce(function, iterable, initial_value)
print(reduce(accumulator, my_list, 0))

funct_list = [lambda x: x+1, lambda x: x*2, lambda x: int(x/2)]
print(funct_list[0](2), end=",")
print(funct_list[1](2), end=",")
print(funct_list[2](2))

# Exercice:
# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda li: li.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda li: li > 50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
total1 = reduce(lambda acc, li: acc + li, my_numbers, 0)
total2 = reduce(lambda acc, li: acc + li, scores, 0)
print(total1 + total2)


# List/Set/ictionary comprehensions
my_list = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list)
my_list = [num**2 if num % 2 == 0 else 'x' for num in range(0, 100)]
print(my_list)
my_set = {num**2 for num in range(0, 100) if num % 2 == 0}
print(my_set)
my_set = {num**2 if num % 2 == 0 else 'x' for num in range(0, 100)}
print(my_set)
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()
           if value % 2 == 0}
print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates)
