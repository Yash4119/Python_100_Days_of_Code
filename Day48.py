# Local and Global variables in Python

x = 10

def func():
    # x = 12
    y = 10
    print(y)
    global x
    x +=12

print(x)
func()
print(x)