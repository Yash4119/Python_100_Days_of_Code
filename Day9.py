# Typecasting In Python
# Conversion of one data type to another data type is called as type casting

'''
1. Implicit type casting :- Python performs this type casting
2. Explicit type casting :- User has to perform this type casting
'''

c = "27"

# a = int(input("Enter a :- "))
# b = int(input("Enter b :- "))

# c = a+b
c = "False"

print(bool(c))
print(type(c))

# Implicit Typecasting

c = 1.9
d = 10

print(c+d) # here the answer is implicitly converted to float