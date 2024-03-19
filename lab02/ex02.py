num1 = int(input("Enter first number  :"))
num2 = int(input("Enter second number :"))

while True:
    if num2 == 0:
        print("Second number cannot be 0")
        break
    else: 
        result = num1 / num2
        remainder = num1 % num2
        print("Result of dividing " + str(num1) + " and " + str(num2) + " is: " +str(result))
        print(f"The remainder of {num1} and {num2} is : {remainder}" ) #using formatted string literals
        break



