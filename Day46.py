# OS Module in Python

import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,10):
#     if(not os.path.exists(f"data/Day{i+1}")):
#         os.mkdir(f"data/Day{i+1}")

# # for i in range(0,10):
# #     os.mkdir(f"Data/Day{i+1}/main.py")

# for i in range(0,10):
#     os.rename(f"data/Day{i+1}/main.py",f"data/Day{i+1}/this.py")


# folders = os.listdir("data")
# print(folders)

# for folder in folders:
#     print
#     print(os.listdir(f"data/{folder}"))
# os.mkdir("H")
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd)

# os.removedirs("Data/Day2/this.py")

for i in(7,9):
    os.removedirs(f"Data/Day{i+1}/this.py")