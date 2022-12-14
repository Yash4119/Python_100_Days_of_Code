#  if elif else in Python

a = int(input("Enterr your age :- "))
print("Your Age is :- ", a)

if(a < 18):
    print("You are a teen, You Cannot drive")
elif(a>=18 and a<=50):
    if(a==18):
        print("Congo Brother")
    if(a-18 >= 1):
        if(a-18 >= 10):
            print("Your have less life")
        else:
            print("Nay life jast ahe tula")
    print("You can Drive")
else:
    print("You are old enough, avoid driving")