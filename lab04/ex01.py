# defining a function to find average of two given number, takes 2 number as parameters
def find_average(a, b):
    average_num = float((a + b) / 2) #Calculating the average of two number
    return average_num #return the avarage number


no1 = int(input("Enter first number :"))  #input to get first number
no2 = int(input("Enter Second number :")) #input to get second number
print("The average is ", find_average(no1,no2)) #calling a function inside print statement
