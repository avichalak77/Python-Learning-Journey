a = {1,2,3,4,5}
b = {2,4,7,8,9}

c = a.union(b) # combines both sets 
print(c)

d = a.intersection(b)    # only common elements are combined
print(d)

e = b.difference(a)     #elements present in b but not in a
print(e)

r = a.symmetric_difference(b)
print(r)