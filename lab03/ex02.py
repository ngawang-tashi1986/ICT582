#Python program to check for the largest number from the user input and display the largest in
#3 place decimal value.
#The program will go into infinite loop until user entered stop/STOP

# Initialize the largest number variable with negative infinity
largest_number = float('-inf')

# Start a loop that runs until the user enters "stop"
while True:
    user_input = input("Enter a decimal number or 'stop' to finish: ")

    # Check if the user wants to stop the input process
    if user_input.lower() == "stop":
        break
    
    # Check if the user input is int for float
    if user_input.replace(".", "").isnumeric():
        number = float(user_input)    # if the user input is float, then assign it to a variable 'number' and
        if number > largest_number:   # assign the next largest_number to variable number  
            largest_number = number
    else:
        print("That's not a valid decimal number. Please try again.")

# Check if the user has entered any numbers
if largest_number == float('-inf'):
    print("No numbers were entered.")
else:
    # Output the largest number formatted to the 3rd decimal place
    print(f"The largest number entered, accurate to the 3rd decimal place, is: {largest_number:.3f}")
