# The following program reads in the sequence of strings and prints out the number represented
# digits if present. The program will be terminated if the user types in 'stop'

# The following function takes in string as parameter and extract the number
def extract_digits_to_number(input_string):
    result = ''                  # Assigning result to null. This will hold the concatenates the string/number
    for char in input_string:    # Iterating through string
        if char.isdigit():       # Checking if the iterated character in the string is a number
           result += char        # If the number is found it will concatenates to represent number            
    return result                # Returning result


while True:
        user_input_string = input("Enter a string or 'stop' to end the program : ")
        if user_input_string.lower() == "stop":
            print("Stopping the program!!!")
            break
        extrated_digits = extract_digits_to_number(user_input_string) # Calling function extract_digits_to_number() with userstring as input
        # Check whether string is empty before printing and print 0 if it is null
        print(f"The number of digits in the string is: {int(extrated_digits) if extrated_digits else 0}")

