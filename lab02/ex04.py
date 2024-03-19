speed_limit = 60 #Declaring the speed limit.
fine_message = 'Your speeding fine is: ' #Delcare fine message
speed = int(input("Enter the recorded speed of the vehicle (in km/h): ")) #Get speed values from user
if speed < 0:   #Check whether speed is a negative value
    print("Vehicle speed cannot be a less then 0")
else:    
    if speed > speed_limit:  #check if the speed is more than 60 km/h
        print("Speeding")
        if speed >= 61 and speed <= 65:
            print("Warning")
        elif speed >= 66 and speed <= 70:
            print(fine_message + "$100")
        elif speed >= 71 and speed <= 80:
            print(fine_message + "$200")
        elif speed >= 81:
            print(fine_message + "$500")
    else:
        print("Not speeding") #print default value if the speed is below 60 km/h


