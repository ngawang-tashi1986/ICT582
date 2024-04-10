def small_number():
    #global small
    small = None

    while(True):
        num = input("Enter a number of 'Stop': ")
        if num.lower() == 'stop':
            break
        else:
            if small is None or small > float(num):
                small = float(num)
            else:
                continue
    return small

#smallest = small_number()
#if smallest is  None:
#    print("Ypu have enter no number!!")
#else:
#    print("The smallest number is ", smallest)
