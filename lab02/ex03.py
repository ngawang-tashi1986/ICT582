#Declared a message variable ("output_message") to store common message

output_message = 'You have selected: '
num_of_day = int(input("Enter a number between 1 and 7: ")) #integer variable to store input values
if num_of_day == 1:
    print(output_message + "Monday")
elif num_of_day == 2:
    print(output_message + "Tuesday")
elif num_of_day == 3:
    print(output_message + "Wednesday")
elif num_of_day == 4:
    print(output_message + "Thursday")
elif num_of_day == 5:
    print(output_message + "Friday")
elif num_of_day == 6:
    print(output_message + "Saturday")
elif num_of_day == 7:
    print(output_message + "Sunday")
else:     #default else to handle error for out of range number
    print("Inalid input, please enter number between 1 and 7")
