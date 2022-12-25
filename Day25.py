# Tuple Methods in Python

tup = ("Yash","Jayram","Ambekar",6,3,2002,True)

print(tup)

# If you wish to update a tuple simply copy contents of a tuple to list manipulate the list and then create a new tuple
tup2 = (23,34,6)

tup3 = tup + tup2

print(tup3)

print(tup3.count(23))

# tuple_name.index(element, start, end)

print(tup3.index(6))
# print(tup3.index("Y"))  # will generate an error if element is not present in the tuple

print(len(tup3))