# The following program reads in the sequence of strings and prints out the number of
# digits if present. The program will be terminated if the user types in 'stop'

# The following function takes in string as parameter and counts the number of digits
def count_digits(input_string):
    count = 0                   # Assigning count to 0
    for char in input_string:   # Iterating through string
        if char.isdigit():      # Checking if the iterated character in the string is a number
            count += 1          # Increamenting the count if a number is found
    return count                # Returning count value


while True:
        user_input_string = input("Enter a string or 'stop' to end the program : ")
        if user_input_string.lower() == "stop":
            print("Stopping the program!!!")
            break
        num_of_digits = count_digits(user_input_string) # Calling function count_digits() with userstring as input
        print(f"The number of digits in the string is: {num_of_digits}")


