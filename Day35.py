# While Loop and For Loop with else in Python

a = [1,2,3,4,5,6]
prev = a[0]

for i in a:
    print(i)
    if(i==4):
        break
else:
    print("Iterated Entire Array!!!")

i = 0
while(i<len(a)):
    print(a[i])
    i+=1

else:
    print("Also Did While Loop")