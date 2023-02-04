# Clear the clutter within the folder using os module.

import os

def changeNames(files, path, type):
    cnt = 1
    for f in files:
        if(f.endswith(f".{type}")):
            source = path + '\\' + f
            dest = path + f'\\{cnt}.{type}'
            os.rename(source,dest)
            cnt += 1


print(os.name)
print(os.getcwd())
print(os.listdir())


path = os.getcwd()

files = os.listdir(path)

type = str(input("enter the type of file you want to clear clutter of :- "))

changeNames(files, path, type)