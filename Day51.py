# File Handling seek() and tell() function in Python

# in Python seek() and tell() functions are used to work with file objects and there relative positions within a file

with open("myfile.txt",'r') as f:
    f.seek(10)
    line = f.read(10)
    print(line)

    # tell function returns the current position withgin the file
    print(f.tell())

    # truncate function truncates the file to a specified size
with open("myfile.txt",'w') as f:
    f.truncate(5)
    f.seek(10)
    print(f.tell())
    f.write("Hello")

    # the seek function allows you to move the current position in a file at a spevific location
