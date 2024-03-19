num1 = input("Enter first number  : ")
num2 = input("Enter second number : ")

sum = int(num1) + int(num2) # input is consider as srting, so we need to type cast to int2

print("The sun of "+num1+" and "+num2+" is ",sum)

#if sum < 10:
#    print("The sum is less then 10")
#else: 
#    print("The sum is greater then 10")  

if sum > 5 and sum < 10: #or
    print("The sum is less than 10")
else: 
    print("The sum of "+num1+" and "+num2+" is ",sum)




