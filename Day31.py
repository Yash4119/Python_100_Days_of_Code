# Sets in Python
# A set is a collection of unique elements.
# values in a set are enclosed within {} curly brackets and separated by commas
# Set is a unordered collection of elements
# Sets are unchangable

s = {1,2,3,4,4,4,4,"Yash","Yash Ambekar","yash ambekar",True,False,1.1}
print(s)

# Try to create and empty set. check using the time functionwhether the type of your variable is set or not
harry = set()
print(type(harry))
print(type(set()))

# if we do harry = {} then we will be getting type as dictionary

for i in s:
    print(i)