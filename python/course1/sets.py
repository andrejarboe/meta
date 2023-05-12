# sets
# sets do not allow duplicates
# sets have methods 
# can not do: set[0] or set[1] etc..
# because a set is nto a sequence 

setA = {1,2,3,4,5}
setA.add(6)
setA.remove(2)
setA.discard(5)
print(setA)


setB = {1,2,3,4,5}
setC = {4,5,6,7,8}

# union
print(setB.union(setC))
print(setB | setC)

# intersection
print('intersection: ')
print(setB.intersection(setC))
print(setB & setC)

# difference
# only in set B
print('Difference: ')
print(setB.difference(setC))
print(setB - setC)

# symmetric difference
print('Symmetric difference')
print(setB.symmetric_difference(setC))
print(setB ^ setC)


