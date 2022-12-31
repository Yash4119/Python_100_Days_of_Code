# Recursion in Python

def func(a):
    if(a <= 1):
        return 1
    
    return a * func(a-1)

# num = int(input("Enter the number to find factorial of :- "))
# print(f"Factorial of {num} is {func(num)}.")

def fibo(n):
    if(n==0 or n==1):
        return n
    
    return fibo(n-1)+fibo(n-2)


num = int(input("Enter the Nth fibonacci number you want to find :- "))
print(f"{num}th Fibonacci number is {fibo(num)}.")