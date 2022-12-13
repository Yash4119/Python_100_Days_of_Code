#  String Slicing in Python

name = "Yash Jayram Ambekar"
print(name[0:5])
print(name[:9]) # displays string upto the 8th index, character at 9th index is not displayed
print(name[5:]) 

# Negative slicing

print(name[:len(name)-3])
print(name[:-3])
print(name[-4:])    # negative indexes specify the indexes from the back of the string

# Length of a string
print("Length of the string is :- ",len(name))

# Quick Quiz

nm = "Harry"
print(nm[-4:-2])    #this will print "ar"