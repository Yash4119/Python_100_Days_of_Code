# In this File we will be learning about the custom errors in python

try:
    a = str(input("Enter is Yes or No :- "))

    if(a.lower() != "yes" and a.lower() != "no"):
        raise ValueError("Value should be either 'Yes' or 'no'")
        
except ValueError as e:
        print("Error Occurred")
        print("Error :- ",e)