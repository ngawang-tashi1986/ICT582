while True:
    num = input("Enter a number : ")
    if num == 'q':
        break
    sum = 0
    for i in range(1, int(num)):
        sum = sum + i
    print("Sum of the number from 1 to "+ num + " is :" + str(sum))

    
   