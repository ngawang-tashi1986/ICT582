# Python program to read the line and report whether the line contains the word
while True:
    # Read a line from the user
    input_line = input("Enter a line (or type 'quit' to finish): ")
    
    # Check if the user wants to quit the program
    if input_line.lower() == "quit":
        print("Thank You ! Exiting the program.")
        break

    # Read a word from the user to search
    search_word = input("Enter a word to search for: ")

    # Use the find method to get the position of the word in the line
    position_of_word = input_line.find(search_word)

    # Report whether the line contains the word and its position if found
    if position_of_word != -1:
        print(f"The word '{search_word}' was found at position {position_of_word}.")
    else:
        print(f"The word '{search_word}' was not found in the line.")
