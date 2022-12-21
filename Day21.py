# Function Arguements in Python

# Printing average of 2 Numbers
def avg(a,b):
    print("Average of ",a," and ",b," is :- ", (a+b)/2)

# Printing average of 2 Numbers using default arguements
def avg2(a=0,b=1):
    print("Average of ",a," and ",b," is :- ", (a+b)/2)

# Printing Average of Number of an list
def avg3(arr):
    sum =0
    for i in arr:
        sum += i
    
    n = len(arr)
    return sum/n


avg(3,4)

avg2()

arr = [1,2,3,4,5,6,7,87,88,9]
print("Average of Numbers of the array is :- ", avg3(arr))


# Keyword Arguements

def avg4(a,b):
    print("Average of ",a," and ",b," is :- ", (a+b)/2)

avg4(b=34,a=12)

# Required Arguements

def avg5(a,b=12):
    print("Average of ",a," and ",b," is :- ", (a+b)/2)
# Here a is the required arguement while b is the default arguement
avg5(a=6)

# Variable length arguements
def avg6(*nums):
    sum=0;
    for i in nums:
        sum += i;

    print("Average is :- %0.2f" %(sum/len(nums)))
    print("Average is :- {0:.4f}".format(sum/len(nums)))

avg6(1,2,3,4,5,5,6)

