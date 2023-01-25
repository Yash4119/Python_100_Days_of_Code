# Today we will learn about import statement in python

import math

print(math.floor(234.345))

print(math.sqrt(16))
print(round(math.pi*math.sqrt(1623.5),3))
print(dir(math))
print(math.nan, type(math.nan))

from Ex4 import encode,decode as d

print(encode("yash"))
print(d(encode("yash")))