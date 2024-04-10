def print_triangle(number):
    get_sequence = ''.join(str(i) for i in range(1, number+1))
    for i in range(len(get_sequence), 0, -1):  # Decrement to print in reverse
        for j in range(i):                     # Inner loop for printing each digit in a row
            print(get_sequence[j], end='')     # Print digit with no newline
        print()





        
