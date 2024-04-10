t1 = (1, 2, 3.5, 'abc', (12, 4.5, 'df'), [1, 2, 3.5, 'abc'])
l1 = [1, 2, 3.5,'abc']
l2 = [1, 2, 3.5, 2, 8, 9.5, 6]

print(t1)
print(l1)

print(type(t1))
print(type(l1))

print(type(t1[2]))
print(type(t1[1]))

print(type(t1[5][2]))
print(t1[5][2])

#t1[2] = 4 # cannot change tuple

l1[2] = 4
print(l1)

l1.append(8.6)
print(l1)

print(len(l1))

print(l2)
print(sorted(l2))  # doesnot have effect on original list

l2.sort()
print(l2)

del(l2[3])
print(l2)

l2.remove(2)
print(l2)