# Dictionary Methods in Python

'''
update
clear
pop
popitem (clears the last item)
'''

stud = {
    "TCOB20":"Omkar JAdhav",
    "TCOB24":"Yash Shinde",
    "TCOB27":"Tejas Bhandvalkar",
    "TCOB33":"Yash Ambekar"
}

up = {
    "TCOB34":"Satyam Ji",
    "TCOB47":"Swami Ji"
}

print(stud.items())

stud.update(up)
stud.pop("TCOB34")
print(stud.items())

print(up.items())
up.clear()
print(up.items())

stud.popitem()
print(stud.items())

del stud["TCOB20"]
print(stud)