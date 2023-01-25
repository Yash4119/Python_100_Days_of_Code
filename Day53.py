# Map and Filter in Python

def cube(x):
    return x*x*x

l = [1,2,3,4,5,6,7,8,9]
newl = []

# Conventional Method
for i in l:
    newl.append(cube(i))

print(newl)

# Map Method to do the same

newl = list(map(cube,l))
print(newl)
newl = list(map((lambda x:x*x*x),l))
print(newl)

# Filter method to do the same
def filter_func(x):
    return x>=5

newl = list(filter(filter_func, l))
print(newl)
newl = list(filter((lambda x: x<=5),l))
print(newl)

# Reduce method to do the same

# performs a given operation on all values of list

from functools import reduce

def num(x,y):
    return x+y

n = reduce(num,l)
print(n)

