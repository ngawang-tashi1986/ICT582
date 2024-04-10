def next_char(nxtChar):
    # Check if the character is an English letter
    if nxtChar.isalpha():
        # Check if the character is 'z' or 'Z'
        if nxtChar == 'z':
            return 'a'
        elif nxtChar == 'Z':
            return 'A'
        else:
            return chr(ord(nxtChar) + 1) # Return the next character in the alphabet ord() 
                                         #get the ASCII value of alphabet
    else:
        return nxtChar # Return the character unchanged

in_char = input("Enter a character ==> ")
print("The next character is ==> ",next_char(in_char))

