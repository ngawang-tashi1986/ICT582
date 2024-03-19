s = 'abcd'
a1 = ''
for i in range(len(s)-1,-1, -1):
    a1 = a1 + s[i]
    #print(a1)
print(a1)
a2 = s[::-1]

if a1 == a2:
    print("same")
else:
    print("Not same")
