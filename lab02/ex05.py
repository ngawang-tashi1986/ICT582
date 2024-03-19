while True:
    val = input("Enter a temperature in Fahreinheit to convert it to Celsius or type end to exit: ")
    if val.upper() == 'END':
        print('Thank you!')
        break
    else:
        result = (float(val) - 32) * 5 / 9
        print("%s Fahreinheit = %0.2f" % (val, result) + " Celsius")
        #used string formatting 
