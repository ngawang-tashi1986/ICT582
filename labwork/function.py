def f_name(a,b):
    c = a + b
    d = a - b
    return c, d
    #print('sum is ', c)


#f_name(10,7)
#f_name(11.5, 8.2)
#f_name('abc','def')

#x = f_name(10,7)
#print('sum is ', x)
#x = f_name(11.5, 8.2)
#print('sum is ', x)
#x = f_name('abc','def')
#print('sum is ', x)

x, y = f_name(10,7)
print('sum is ', x)
print('Dif is ', y)