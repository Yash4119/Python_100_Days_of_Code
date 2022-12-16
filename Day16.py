# Match Case Statements in Python

ch=0

while(ch!=3):
    print("********** SELECT ANY **********")
    print("1. One")
    print("2. Two")
    print("3. Exit")

    ch = int(input("Enter Your choice :- "))

    match ch:
        case 1:
            print("You Selected One")
        case 2:
            print("Your Selected Two")
        case 3:
            print("Thank You For using my Program")
        case _ if ch<=0:
            print("Enter Values Greater than 0")
        case _ if ch>3:
            print("Enter Values Smaller than or equal to 3")
    

print("See You Next Time")