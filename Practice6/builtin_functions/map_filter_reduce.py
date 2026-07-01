#MAP

s = ['1', '2', '3', '4']
res = map(int, s)        # map applies function to every element of one or more iterables and returns a map object(iterator)
                         # in this case function is int()
print(list(res))


def double(val):
    return val * 2
a = [1, 2, 3, 4]    
result = list(map(double, a))   # convert map object to list to work with results directly
print(result)   


a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a))       #lambda instead of def function
print(result) 

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)       # multiple iterables
print(list(res))

words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)            # first characters from words
print(list(res))


#FILTER

def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"] 
res = filter(starts_a, li)            # applies function to iterable
print(list(res)) 

def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b))            # Convert filter object to a list


a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 3 == 0, a)            # lambda instead of def 
print(list(b))


#REDUCE 

from functools import reduce
a = ["Geeks", "for", "Geeks"] 
r = reduce(lambda x, y: x + " " + y, a)        # applies function cumulatively to elements of iterable
print(r)                                       # single final value

a = [2, 4, 6, 8]
r = reduce(lambda x, y: x + y, a)
print(r)

a = [5, 9, 3, 12, 7]
r = reduce(lambda x, y: x if x > y else y, a)      # find largest number
print(r)


import functools
import operator
a = [1, 3, 5, 6, 2]

print(functools.reduce(operator.add, a))
print(functools.reduce(operator.mul, a)) 
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))    # sum,product and string concatenation