# List Methods

l1 = [1,5,3,2,4,6,7,8,9,"Yash","Jayram","Ambekar",True,False]
l2 = [2,1,4,3,5,2,56,4,2,5,47,3,54,47]

# Methods
'''
1.len(List_Name)
2.List_Name.append(Value)
3.List_Name.sort()
4.List_Name.sort(reverse=True/False)
5.List_Name.reverse()
6.List_Name.extend(Other_List_Name)
7.List_Name.index(value)
8.List_Name.copy()
9.List_Name.insert(index, value)
10. List_Name1 = List_Name2 + List_Name3 
'''

print(len(l1))

l1.append("End")
print(l1)

l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)

l1.reverse()
print(l1)

# return index of 1st occurrence
print(l1.index("Yash"))

m = l1
m[0] = "Start"
print(m)
print(l1)
# in Python the lists are not copied directly instead here an reference3 has been created and hence change occurred in the original list as well

m = l1.copy()
m[1] = "Yash"
print(l1)
print(m)

print(l1)
l1.insert(1,999)
print(l1)

m = [1,2,3]
print(m)
m.extend(l1)
print(m)

k = [100,200,300] + m
print(k)