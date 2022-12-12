#  Exercise no 1 :- 

# Operators in python
'''
    Addition        - +
    Subtraction     - -
    Multiplication  - *
    Exponential     - **
    Modulus         - %
    Division        - /
    Floor Division  - //
'''

# Python Calculator
ch=0

while True:
    print("1. Addition       => a + b")
    print("2. Subtraction    => a - b")
    print("3. Multiplication => a * b")
    print("4. Division       => a / b")
    print("5. Floor Division => a // b")
    print("6. Modulus        => a  b")
    print("7. Exponential    => a ^ b")
    print("8. Exit")

    ch = input("Enter your choice :- ")
    ch = int(ch)

    if(ch==8):break

    a = int(input("Enter Num 1 :- "))
    b = int(input("Enter Num 2 :- "))

    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    elif ch==5:
        print(a//b)
    elif ch==6:
        print(a%b)
    elif ch==7:
        print(a**b)

print("Successfully Done Operations!!!")

'''
a = int(input("Enter num1 :- "))
b = int(input("Enter num2 :- "))

print("Addition of ", a ," and ", b ," is : ", a+b)
print("Subtraction of ", a ," and ", b ," is : ", a-b)
print("Multiplication of ", a ," and ", b ," is : ", a*b)
print("Division of ", a ," and ", b ," is : %.4f"% (a/b))
print("Division of ", a ," and ", b ," is : {0:.3f}". format(a/b))
print("Floor Division of ", a ," and ", b ," is : ", a//b)
print("Exponential of ", a ," and ", b ," is : ", a**b)
print("Modulus of ", a ," and ", b ," is : ", a%b)
'''