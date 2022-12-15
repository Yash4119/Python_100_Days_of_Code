# Exercise 2 We will be using the Time Module for Python
import time
import datetime
now = datetime.datetime.now()

hr = now.hour

if(hr>=5 and hr < 12):
    print("Good Morning Sir!!!")
elif(hr >= 12 and hr <= 18):
    print("Goor Afternoon!!!")
elif(hr>18 and hr<24):
    print("Good Evening!!!")
else:
    print("Good Night!!!")


# for i in range(1,10):
#     print(i)
#     time.sleep(2)

t = time.strftime("%Y , %D , %H:%M:%S")

print(t)

t = time.strftime("%H")
print(t)

t = time.strftime("%M")
print(t)

t = time.strftime("%S")
print(t)