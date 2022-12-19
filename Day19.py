# Break And Continue Statements

# break is used to end an iteration
# continue is used to skip a particular iteration

print("Odd Numbers from 1 to 10")
for i in range(1,11):
    if(i%2==0):
        continue;
    print(i," ",end=" ")
print()

print("Even Numbers from 1 to 10")
for i in range(1,11):
    if(i%2 == 1):
        continue;
    print(i," ",end=" ")
print()

i=1
print("Odd Numbers from 1 to 10 using continue and break statement")
while(True):
    if(i>10):
        break
    if(i%2==0):
        i+=1
        continue
    print(i," ",end=" ")
    i+=1

i=1
print()
print("Even Numbers from 1 to 10 using continue and break statement")
while(True):
    if(i>10):
        break
    if(i%2==1):
        i+=1
        continue
    print(i," ",end=" ")
    i+=1