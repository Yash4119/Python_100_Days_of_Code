# Lambda Functions in Python
# In Python a lambda function is a small anonymous function without a name
# it is defined using lambda keyword


# Normal function
def sum(x,y):
    return x+y

sum(5,6)

# Lambda function

product = lambda x,y:x*y

product(5,6)

print(sum(5,6)," ",product(5,6))