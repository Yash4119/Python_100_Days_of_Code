# Set Methods in Python

'''
1. Union
2. Intersection
3. Symmetric_Difference
4. Difference
5. isdisjoint
6. issuperset
7. issubset
8. add
8. update. 
9. remove / discard
10. pop
11. del
12. clear
13. in
'''

s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10}

print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)

s3 = {11,12,13,14,1,2,3,5,6}
print(s1.intersection(s2.intersection(s3)))

s3.intersection_update(s2)
print(s3)

# Symmetric Difference
# symmetric diff(a,b)= union(a,b) - intersection(a,b) 
s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10}
print(s1.symmetric_difference(s2))

# Difference and difference update

s3 = {11,12,13,14,1,2,3,5,6}
print(s3.difference(s2))

print(s1.isdisjoint({49,99,123}))
print(s2.issuperset({5,6,7,8,9,10,11,12}))
print(s1.issubset({1,2,3,4,5,6,7,8,9,10,11,12,13}))
s3.add("Yash")
print(s3)
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
print(s3.pop())
del(s1)

s2.clear()
print(s2)