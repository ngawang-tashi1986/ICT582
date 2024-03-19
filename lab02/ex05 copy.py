while True:
    val = input("Enter a temperature in Fahreinheit to convert it to Celsius or type end to exit: ")
    if val.upper() == 'END':
        print('Thank you!')
        break
    else:
        result = (float(val) - 32) * 5 / 9
        print("%s Fahreinheit = %0.2f" % (val, result) + " Celsius")
        #The %s operator is put where the string is to be specified. 
        #The number of values you want to append to a string should be 
        #equivalent to the number specified in parentheses after the % 
        #operator at the end of the string value. 
