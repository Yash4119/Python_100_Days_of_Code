# Tuples in Python
# Tuples in Python are immutable. i.e Once created they cannot be updated
# Elements of tuples are enclosed in () brackets and separated by commas

tup = ("Yash",1)

print(tup)
print(len(tup))
print(type(tup))
print(tup[0])
# print(tup[12])

print(tup[-1])

if "Yash" in tup:
    print("Present")
else:
    print("Not Present")

# We can perform slicing on tuple but however a new tuple is formed for that particular index slice
print(tup[:1])
print(tup[1:])