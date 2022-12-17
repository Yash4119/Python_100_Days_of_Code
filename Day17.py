# For Loops in Python
'''
For Each Loop 
For in Loop
'''
import time

print("For In Loop")
for i in range(1,1000):
    print(i,end=" ")
    # time.sleep(0.5)

print()
print("While Loop")
i = 1
while(i<10):
    print(i,end=" ")
    i+=1
    time.sleep(0.5)

print()
print("For Each Loop")
a = [1,2,3,4,5,676,3,56,3,75,354,37,356534]
for i in a:
    print(i,end=" ")
    time.sleep(0.2)

# For in Loop using step variable
print()
print("Step Keyword")
for i in range(1,10000,5):
    print(i)