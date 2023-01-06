# Exception Handling in Python

'''
In Python we use Try Except block for Exception Handling

Exception 
AritmethicError
ValueError
IndexError
and so on.....
'''

a = [1,2,3,4,5]

try:
    for i in range(0,6):
        print(a[i]/i)
except ArithmeticError as ae:
    print(f"Arithmetic Error Occurred :- {ae}")
except Exception as e:
    print("Error :- ",e)

print("Finished Execution")