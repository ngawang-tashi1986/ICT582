s = '123456789'

for i in range(0, len(s)):
    a = ''
    for j in range(0, len(s)-i):
        a = a + s[j]
    print(a)
    
