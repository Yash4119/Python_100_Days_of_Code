# Lists in Python

# Lists are ordered collection of data items
# List items are separated by commas and enclosed within square brackets
# Lists in python can store heterogenous elements
l2 = [1,2,True,"Yash"]
l1 = [1,2,3,4,5]
print(l2)
print(l2[3])
print("Our List is :- ",l1)
print("Type of l1", type(l1))

# Indexing in Lists is similar to indexing of arrays used in c++

l3 = [1,2,3,4,5,6,8,7]

# index slicing in python lists
print(l3[2:4])

# Negative indexes represent the elements from the back hence the indexes are negative
print(l3[-4])
print(l3[-3:])

# in Keyword
if 5 in l3:
    print("Yes")
else:
    print("No")

# Finding substring python string
if "arry" in "HaRry":
    print("Yes")
else:
    print("No")

# Jump indexing
print(l3[::2])

# List Comprehension
# list comprehension is the process of creating a list  from other iterables list lists, tuples, dictionaries and even arrays and strings

l4 = [ele for ele in range(50) if(ele%2==0)]

print(l4)