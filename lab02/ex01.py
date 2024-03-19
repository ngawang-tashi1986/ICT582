num1 = int(input("Enter first number  :"))
num2 = int(input("Enter second number :"))

while True:
    if num2 == 0:
        print("Second number cannot be 0")
        break
    else: 
        result = num1 / num2
        print("Result of dividing " + str(num1) + " and " + str(num2) + " is: " +str(result))
        break











