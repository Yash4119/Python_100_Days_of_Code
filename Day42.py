# Enumerate function in Python

'''
suppose we want to find the index of an element in an array
'''

a = [1,2,3,4,5,6,7,78,7898,34]

# conventional method fort finding the index of an element using for each loop

# index = 0
# for marks in a:
#     print(marks)
#     print("Harry Bhai Mojj Me") if index == 8 else ""
#     index+=1

# Now we will be using Enumerate function for more simplicity

for index, marks in enumerate(a):
    print(index," -> ",marks)

# We can start the index of enumerate with some different start

for ind, mar in enumerate(a, start=10):
    print(ind," -> ",mar)

