def shift_by_one(input_string):
    output_string = ""
    for char in input_string:
        if char.isalpha():
            if char.lower() == 'z':
                output_string += 'a' if char.islower() else 'A'
            else:
                output_string += chr(ord(char) + 1)
        else:
            output_string += char
    return output_string

# Test the function
print(shift_by_one("xyZ"))
