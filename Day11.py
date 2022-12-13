# Strings in Python

name = "Yash"
middle = "Jayram\nAmbekar"
city = 'Pune'

print(name,middle ," ", city)


c = '''
    this is 
    a multiline string
'''

print(c)

#  we can access characters of string by indexing and index slicing
# strings are LIKE array of characters

name = "Yash"

print(name[2])
print(name[0:3])

for i in name:
    print(i, end=" ")
print()
for i in range (0, len(name)):
    print(name[i],end=" ")