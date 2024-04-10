def fahrenheitToCelsius(temp):
    return (temp - 32) * 5/9

def readTemperature():
    while True:
        temp = float(input("Enter a temperature in Fahrenheit: "))
        if temp < -60 or temp > 130:
            print("Temperature value must be between -60 and 130, please try again")
        else:
            return temp

while True:
    val = input("Type 'Continue' or 'end': ")
    if val.isalpha():
        if val.lower() == 'end':
            print("Thank You!!")
            break
        elif val.lower() == 'continue':
           temp = readTemperature()
           tempInCelsius = fahrenheitToCelsius(temp)
           print("%s Fahreinheit = %0.2f" % (temp, tempInCelsius) + " Celsius")
        else:
            print("Invalid input")
