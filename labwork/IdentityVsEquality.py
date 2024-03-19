# Equality operator
a=10
b=9

#Case 1:
# Return True because both a and b have the same value
print(a==b)

#Case 2:
# Return True because both a and b is pointing to the same object   
print(id(a))
2813000247664  

print(id(b))
2813000247664    

print(a is b)

c=a       
id(c)
2813000247664

print(a is c)   