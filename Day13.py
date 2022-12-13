# String Operations in Python

a = "cccccc Yash Jayram Ambekar aaa"

print(len(a))

# String in python are immutable
# so whenever we use operations on strings a new string is generated

print(a.upper())
print(a.lower())
print(a.title())
print(a.lstrip("c").lstrip(" ").capitalize())
print(a.rstrip("a"))
print(a.lstrip("c"))
print(a.replace("Jayram",""))   # replaces all occurrunces of string with the new string
print(a.split(" "))     # splits the python string into a list based upon the separater

a = a.center(90)
print(a)

# here using these methods we cannot change the existing string instead we create a new string

# Count occurrences
print(a.count("yash"))

a = "yash aaaaaaA"

print(a.endswith("aaa"))
print(a.endswith("sh",1,4))

# Find method find the first occurrence of a string and returns its index
sen = "This is a temporary sentence"
print(sen.find("porary"))
print(sen.find("pnew"))
print(sen.index("sen"))
# print(sen.index("yash"))        #this will throw and exception

# isalnum -> checks if a string is alpha numeric

name = "Yash\n4119"
print(name.isalnum())
print(name.isalpha())
print(name.islower())
print(name)
print(name.isupper())
print(name.isprintable())
a = " "
print(name.isspace())
print(a.isspace())
print(name.istitle())
print(name.startswith("Yash"))
print(name.swapcase())