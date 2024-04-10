# The following program will shif the input character/string to one position in alphabetical order.
# The function below moves or shift the input character to one position in aplhabeticial order. 
def shift_string(input_string):  # Takes input string as parameter    
    output_string = ""           # Initally assigning null value to shifted or new moved string 
    for char in input_string:    # Iterating for each character in a string
        if char.isalpha():
            if char.lower() == 'z':   # Check if the character is Z or z
                output_string += 'a' if char.islower() else 'A'
            else:
                output_string += chr(ord(char) + 1) # Shifting character by one position
        else:
            output_string += char
    return output_string         

while True:
    user_input = input("Enter a string or type 'stop' to exit : ")
    if user_input.lower() == "stop":
        print("Exiting the program!!!")
        break
    shifted_string = shift_string(user_input)  # Calling the function and sending the userinput string as parameter
    print(f"Shifted String: {shifted_string}")  

