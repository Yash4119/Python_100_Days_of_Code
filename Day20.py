# Python Functions in python

# Basic Void Function
def temp():
    print("In the Function")

# temp()

# function to print multiplication table of a number
def multi(a):
    print("Multiplication Table of ",a)
    for i in range(1,11):
        print(a,'*',i," = ",a*i);

# multi(2)
# multi(3)
# multi(77)

# Function that returns average of elements in an array
def avg(arr):
    sum=0;
    n = len(arr)
    for i in arr:
        sum += i
    
    return sum/n

a = [1,2]
print(avg(a))