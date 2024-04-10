# The following program reads the sequence of numbers from the user and display the largest after 
# user terminates the program. 
# Function to calculate the largest number from the sequence
def find_largest_number():

    largest_number_function = float('-inf')  # Initially, we don't have a largest number
    
    # Start a loop that runs until the user enters "stop"
    while True:
        user_input = input("Enter a sequence of decimal number or 'stop' to finish: ")
         # Check if the user wants to stop the input process
        if user_input.lower() == "stop":
            break
        
        # Check if the user input is int for float
        if user_input.replace(".", "").isnumeric():
            number = float(user_input)    # if the user input is float, then assign it to a variable 'number' and
            if number > largest_number_function:   # assign the next largest_number to variable number  
                largest_number_function = number
        else:
            print("That's not a valid decimal number. Please try again.")
    
    return largest_number_function
    
largest_number = find_largest_number() # Calling the function 'find_largest_number()' to calculate the largest number.
    
if largest_number == float('-inf'):
    print("No numbers were entered.")
else:
    # Output the largest number formatted to the 3rd decimal place
    print(f"The largest number entered, accurate to the 3rd decimal place, is: {largest_number:.3f}")
