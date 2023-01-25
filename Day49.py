# # File IO Handling in PYthon Programming

# f = open("myfile.txt",'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# # r mode is default for file handling

# f = open("My2.txt",'a')
# f.write("Lets meet")
# f.close()


with open("myfile.txt",'a') as f:
    f.write("Heloo")