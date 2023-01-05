# Dictionary in Python
# Dictionaries are ordered collection of items
# Heteregenous data type

dict = {
    "Name":"Yash Jayram Ambekar",
    "Age":29,
    "Gender":"Male",
    "Marital Status":False
}

print(dict)

for i in dict:
    print(i," :- ",dict[i])

print(dict.get("Gender"))
print(dict.keys())
print(dict.values())
print(len(dict))

print(dict.items())

for key, value in dict.items():
    print(key," :- ",value)