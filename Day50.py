# read(), readline() and other methods for file handling in python

with open("My2.txt",'r') as f:
    while True:
        l = f.readline()
        if(not l):
            break
        print(l, " -> ", type(l))

with open("my1.txt",'w') as f:
    lines = ["line1\n","lin2\n","line3\n"]
    f.writelines(lines)